import os

import pytest
from src.formatflick.engine import cEngine
import pandas as pd


def build_cEngine(ext):
    file = os.path.join(os.getcwd(), "tests", "sample_files", "sample" + ext)
    engine = cEngine.cEngine(source=file, mode='file_mode', source_extension=ext)
    return engine


def test_read_file():
    for ext in [".csv", ".tsv"]:
        engine = build_cEngine(ext)
        data = engine.read_file()
        assert isinstance(data, pd.DataFrame)


def test_to_json():
    for ext in [".csv", ".tsv"]:
        engine = build_cEngine(ext)
        obj = engine.read_file()
        json_data = cEngine.cEngine.to_json(obj)
        assert {'a': ['a-1', 'a-2', 'a-3'], 'b': ['b-1', 'b-2', 'b-3'], 'c': ['c-1', 'c-2', 'c-3']} == json_data


def test_to_xml():
    for ext in [".csv", ".tsv"]:
        engine = build_cEngine(ext)
        obj = engine.read_file()
        xml_data = cEngine.cEngine.to_xml(obj)
        print(xml_data)
        assert b"<Result><1><a>a-1</a><b>b-1</b><c>c-1</c></1><2><a>a-2</a><b>b-2</b><c>c-2</c></2><3><a>a-3</a><b>b-3</b><c>c-3</c></3></Result>" in xml_data
