"""nlp basic module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path

import toml

__author__ = "@britodfbr"  # pragma: no cover
projconf = Path(__file__).parents[3] / "pyproject.toml"
versionfile = Path(__file__).parent / "version.txt"

versionfile.write_text(f"{toml.load(projconf)['tool']['poetry']['version']}\n")

__version__ = versionfile.read_text().strip()
