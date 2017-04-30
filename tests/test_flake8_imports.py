
from flake8_imports import ImportsPlugin


def test_integration(tmpdir):
    tmpdir.join('module.py').write("""
import os
import sys
    """.strip())
    ImportsPlugin.parse_options(None)
    obj = ImportsPlugin(None, tmpdir.join('module.py').strpath)
    errors = obj.run()
    errors = list(errors)

    assert len(errors) == 0


def test_failures(tmpdir):
    tmpdir.join('module.py').write("""
from sys import path, modules
import os
    """.strip())
    ImportsPlugin.parse_options(None)
    obj = ImportsPlugin(None, tmpdir.join('module.py').strpath)
    errors = obj.run()
    errors = list(errors)

    assert len(errors) == 1, errors
    assert errors[0][0] == 1, errors
