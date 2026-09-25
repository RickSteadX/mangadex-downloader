# MIT License

# Copyright (c) 2022-present Rahman Yusuf

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import subprocess
import logging
from packaging.version import parse as parse_version

from .network import Net
from . import __version__, __repository__, __url_repository__

current_version = parse_version(__version__)

log = logging.getLogger(__name__)


# Helper functions
def _get_api_tags():
    versions = []
    r = Net.requests.get(
        f"https://api.github.com/repos/{__repository__}/git/refs/tags"
    )

    # Repository has no tags yet (GitHub returns 404 with error message)
    if not r.ok:
        return versions

    for version_info in r.json():
        versions.append(version_info["ref"].replace("refs/tags/", ""))
    return versions


def _get_latest_tag():
    """Return the latest version tag from the repository, or ``None``"""
    versions = _get_api_tags()
    if not versions:
        return None

    return max(versions, key=parse_version)


def check_version():
    # Get latest version
    latest_tag = _get_latest_tag()
    if latest_tag is None:
        return None

    latest_version = parse_version(latest_tag)
    if latest_version > current_version:
        return latest_version

    return None


def update_app():
    try:
        latest_tag = _get_latest_tag()
    except Exception as e:
        log.error(f"Failed to check update, reason: {e}")
        sys.exit(1)

    if latest_tag is None or parse_version(latest_tag) <= current_version:
        log.info("This version mangadex-downloader is up-to-date")
        return

    log.info("Found latest version mangadex-downloader (%s)" % latest_tag)

    # Install the latest tagged version from the repository
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-U",
            f"git+{__url_repository__}/{__repository__}.git@{latest_tag}",
        ]
    )
