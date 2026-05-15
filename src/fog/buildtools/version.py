__version__ = "1.0.2"

__changelog__ = {
    "1.0.3":"""
        - Changed default pip platform to macosx_11_0_universal2 on macOS
        - Changed default pip platform to win_amd64 on Windows
        - Added pip_platform parameter to build function to allow overriding the default platform
    """,
    "1.0.2":"""
        - Added python_version parameter to build function
    """,
    "1.0.1":"""
        - update required minimal pip-tools version to support pip 20.1 see https://github.com/open-zaak/open-zaak/issues/585#issuecomment-626666736
    """,
    "1.0": """
        - Removed dump_changelog
        - Added load_version utility
        - Added update_changelog_file
    """
}
