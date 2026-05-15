import os
import shutil
from invoke import task
from invoke.exceptions import Exit


@task
def release(c):
    r = c.run("git status --porcelain -uno", hide=True)
    if r.stdout.strip():
        raise Exit("Refusing to release: there are uncommitted changes to tracked files.")
    if os.path.exists('dist'):
        print('removing dist/')
        shutil.rmtree('dist')
    c.run('python setup.py sdist bdist_wheel')
    c.run('twine upload dist/*')
    version = c.run('python src/fog/buildtools/buildtools.py load_version .').stdout.strip()
    c.run(f'git tag -a v{version} -m "Release v{version}"')
    c.run(f'git push origin v{version}')

@task
def test(c):
    c.run('python -m pytest tests/ -v')
