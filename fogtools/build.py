import pathlib
from typing import Dict


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
