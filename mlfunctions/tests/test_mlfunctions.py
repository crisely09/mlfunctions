"""
Unit and regression test for the mlfunctions package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import mlfunctions


def test_mlfunctions_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "mlfunctions" in sys.modules
