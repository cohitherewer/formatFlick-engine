import os

import pytest

from formatflick.engine import cEngine
import pandas as pd
import numpy as np


def build_cEngine(ext):
    file = os.path.join(os.getcwd(), "tests", "sample_files", "sample" + ext)
    engine = cEngine.cEngine(source=file, mode='file', source_extension=ext)
    return engine


def test_read_file():
    for ext in [".csv", ".tsv", ".xlsx"]:
        engine = build_cEngine(ext)
        data = engine.read_file()
        assert isinstance(data, pd.DataFrame)


def test_to_json():
    for ext in [".csv", ".tsv", ".xlsx"]:
        engine = build_cEngine(ext)
        obj = engine.read_file()
        json_data = engine.to_json(obj)
        assert {'a': ['a-1', 'a-2', 'a-3'], 'b': ['b-1', 'b-2', 'b-3'], 'c': ['c-1', 'c-2', 'c-3']} == json_data


def test_to_xml():
    for ext in [".csv", ".tsv", ".xlsx"]:
        engine = build_cEngine(ext)
        obj = engine.read_file()
        xml_data = cEngine.cEngine.to_xml(obj)
        print(xml_data)
        assert b"<Result><1><a>a-1</a><b>b-1</b><c>c-1</c></1><2><a>a-2</a><b>b-2</b><c>c-2</c></2><3><a>a-3</a><b>b-3</b><c>c-3</c></3></Result>" in xml_data


def test_to_destination():
    for ext in [".csv", ".tsv", ".xlsx"]:
        # we expect a dataframe here
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        destination = os.path.join(os.getcwd(), "tests", "sample_files", "result" + ext)
        d_engine = cEngine.dest_cEngine(df, destination, destination_extension=ext)
        d_engine.to_destination()
        assert os.path.exists(destination)
        os.remove(destination)
