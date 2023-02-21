import re

import pytest

from incolumepy.prospect.nlp_basic import __version__, projconf, versionfile

__author__ = "@britodfbr"  # pragma: no cover


@pytest.mark.parametrize(
    "entrance", (projconf, versionfile,),
)
def test_file_exist(entrance):
    assert entrance.is_file()


@pytest.mark.parametrize(
    ["entrance", "expected"],
    (
        (__version__, True),
        ("1", False),
        ("1.0", False),
        ("0.1", False),
        ("1.1.1-rc0", False),
        ("1.1.1-rc-0", False),
        ("1.0.1-dev0", False),
        ('1.1.1-a0', False),
        ('1.1.1-a.0', True),
        ("0.0.1", True),
        ("0.1.0", True),
        ("1.0.0", True),
        ("1.0.1", True),
        ("1.1.1", True),
        ("1.1.1-rc.0", True),
        ("1.0.1-dev.0", True),
        ("1.0.1-dev.1", True),
        ("1.0.1-dev.2", True),
        ("1.0.1-alpha.0", True),
        ("1.0.1-alpha.266", True),
        ("1.0.1-dev.0", True),
        ("1.0.1-beta.0", True),
        ("1.1.1-alpha.99999", True),
        ("11111.1.1-rc.99999", True),
        ("1.1.99999", True),
        ("1.999999.1", True),
    ),
)
def test_version(entrance, expected):
    assert bool(
        re.fullmatch(r"\d+\.\d+\.\d+(-\w+\.\d+)?", entrance, flags=re.I)
    ) == expected
