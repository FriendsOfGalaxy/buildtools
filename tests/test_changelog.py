from unittest.mock import patch, mock_open

from src.fog.buildtools import dump_changelog


def test_changelog():
    changelog = {
        "0.1.1": "- fix1\n- fix2",
        "0.1.0": "another log"
    }
    with patch('builtins.open', mock_open()):
        with open('CHANGELOG.md', 'r') as f:
            dump_changelog(changelog, f)
    f.write.assert_called_once_with(
"""# Changelog

## 0.1.1
- fix1
- fix2

## 0.1.0
another log

"""
    )


def test_changelog_dedent():
    changelog = {
        "0.1": """
            - fix1
            - fix2
        """
    }
    with patch('builtins.open', mock_open()):
        with open('CHANGELOG.md', 'r') as f:
            dump_changelog(changelog, f)
    f.write.assert_called_once_with(
"""# Changelog

## 0.1
- fix1
- fix2

"""
    )