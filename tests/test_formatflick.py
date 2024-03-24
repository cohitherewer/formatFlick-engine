"""
Unit tests for formatflick and its associated functions
"""
import os
import pytest
from formatflick import formatflick as ff
from formatflick.global_var import *

invalid_source = os.path.join(os.getcwd(), "tests", "sample_files", "sample-1.csv")
valid_source = os.path.join(os.getcwd(), "tests", "sample_files", "sample.csv")


def test_with_invalid_source():
    with pytest.raises(Exception) as err:
        obj = ff.formatflick(
            source=invalid_source,
            destination=None,
            destination_extension=None,
            verbosity=None,
            mode='file'
        )
    assert str(err.value) == "The source path dont exits"


def test_with_no_dest_no_destExt():
    with pytest.raises(Exception) as err:
        obj = ff.formatflick(
            source=valid_source,
            destination=None,
            destination_extension=None,
            verbosity=None,
            mode='file'
        )
    assert str(err.value) == "destination and destination_extension both cannot be None."


def test_with_invalid_destExt():
    with pytest.raises(Exception) as err:
        obj = ff.formatflick(
            source=valid_source,
            destination=None,
            destination_extension=".py",
            verbosity=None,
            mode='file'
        )
    assert str(err.value) == f".py is not valid. The valid extensions are {VALID_EXTENSIONS}"


def test_with_invalid_dest():
    with pytest.raises(Exception) as err:
        obj = ff.formatflick(
            source=valid_source,
            destination="sample.py",
            destination_extension=None,
            verbosity=None,
            mode='file'
        )
    assert str(err.value) == f".py is not valid. The valid extensions are {VALID_EXTENSIONS}"
