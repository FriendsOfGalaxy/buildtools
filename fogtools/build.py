import os
import sys
import glob
import shutil
import pathlib
import tempfile
import shlex
import subprocess
from typing import Dict


RELEASE_FILE ="current_version.json"


def _run(*args, **kwargs):
    cmd = list(args)
    if len(cmd) == 1:
        cmd = shlex.split(cmd[0])
    kwargs.setdefault("capture_output", True)
    kwargs.setdefault("text", True)
    print('executing', cmd)
    out = subprocess.run(cmd, **kwargs)
    try:
        out.check_returncode()
    except subprocess.CalledProcessError as e:
        err_str = f'{e.output}\n{e.stderr}'
        print('><', err_str)
        raise e
    else:
        print('>>', out.stdout)
    return out


def dump_changelog(changelog: Dict[str, str], dest='.'):
    """Creates CHANGELOG.md based on given `changelog` dict. Keeps given order.
    :param changelog: keys are versions (eg. '0.3.4')
                      values are release notes (in markdown)
    :param dest:      path where CHANGELOG.md should be created
    """
    content = '# Changelog\n'
    for k, v in changelog.items():
        content += f"## {k}\n{v}\n"
    with open(pathlib.Path(dest) / 'CHANGELOG.md') as f:
        f.write(content)


def build(src='src', output='build', third_party_output='.', requirements='requirements/app.txt', ziparchive=None):

    src_path = pathlib.Path(src).resolve()
    out_path = pathlib.Path(output).resolve()
    req_path = pathlib.Path(requirements)

    try:
        out_path.relative_to(src_path)
    except ValueError:
        pass
    else:
        raise RuntimeError("dist (output) cannot be part of src")

    if out_path.exists():
        shutil.rmtree(out_path)

    to_ignore = shutil.ignore_patterns(RELEASE_FILE, '.*', 'test_*.py', '*_test.py', '*.pyc', '__pycache__')
    shutil.copytree(src_path, output, ignore=to_ignore)

    if sys.platform == "win32":
        pip_platform = "win32"
    elif sys.platform == "darwin":
        pip_platform = "macosx_10_13_x86_64"
    else:
        raise RuntimeError(f'Platform {sys.platform} not supported')
    pip_target = (out_path / third_party_output).as_posix()

    try:
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp:
            _run(f'pip-compile {req_path.as_posix()} --output-file=-', stdout=tmp, stderr=subprocess.PIPE, capture_output=False)
            _run('pip', 'install',
                '-r', tmp.name,
                '--platform', pip_platform,
                '--target', pip_target,
                '--python-version', '37',
                '--no-compile',
                '--no-deps'
            )
    finally:
        os.unlink(tmp.name)

    print('clean up dist directories and tests')
    for dir_ in glob.glob(f"{str(out_path)}/*.dist-info"):
        shutil.rmtree(dir_)
    for test in glob.glob(f"{str(out_path)}/**/test_*.py", recursive=True):
        os.remove(test)
    for test in glob(f"{str(out_path)}/**/*_test.py", recursive=True):
        os.remove(test)
