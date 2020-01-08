from inspect import cleandoc
from typing import Dict


class Changelog:
    def __init__(self, changelog: Dict[str, str]):
        self._changelog = changelog

    def __str__(self):
        return str(self._changelog)

    @property
    def _header(self):
        return "# Changelog\n\n"

    def to_markdown(self):
        """Simple implementation - do not support identifiers like [Added] [Fixed]"""
        content = self._header
        for k, v in self._changelog.items():
            content += f"## {k}\n{cleandoc(v)}\n\n"
        return content
