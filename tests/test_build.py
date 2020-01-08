from unittest.mock import patch, mock_open
import pytest

from buildtools.build import dump_changelog


def test_changelog():
    destination = 'there/CHANGELOG.md'
    changelog = {
        "0.1.1": "- fix1\n- fix2",
        "0.1.0": "another log"
    }
    with patch('builtins.open', mock_open()) as mopen:
        dump_changelog(changelog, dest=destination)
    mopen.assert_called_with(destination, 'w')
    handle = mopen()
    handle.write.assert_called_once()
