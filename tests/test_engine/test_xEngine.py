import json
import os

import pandas as pd
import pytest
from formatflick.engine import xEngine


def build_xEngine(ext):
    file = os.path.join(os.getcwd(), "tests", "sample_files", "sample" + ext)
    engine = xEngine.xEngine(source=file, mode='file', source_extension=ext)
    return engine


def test_read_file():
    engine = build_xEngine(".xml")
    data = engine.read_file()
    assert isinstance(data, dict)
    assert data == {'A': {'B': ['B', 'B'], 'C': {'D': 'D'}}}


def test_to_json():
    engine = build_xEngine(".xml")
    obj = engine.read_file()
    json_data = engine.to_json(obj)
    assert json.dumps({"A": {"B": ["B", "B"], "C": {"D": "D"}}}, indent=4) == json_data


def test_to_csv():
    engine = build_xEngine(".xml")
    obj = engine.read_file()
    df = engine.to_csv(obj)
    assert isinstance(df, pd.DataFrame)
    assert (df == pd.DataFrame([{'A.B.0': 'B', 'A.B.1': 'B', 'A.C.D': 'D'}])).all().all()


def test_to_tsv():
    engine = build_xEngine(".xml")
    obj = engine.read_file()
    df = engine.to_tsv(obj)
    assert isinstance(df, pd.DataFrame)
    assert (df == pd.DataFrame([{'A.B.0': 'B', 'A.B.1': 'B', 'A.C.D': 'D'}])).all().all()


def test_to_xlsx():
    engine = build_xEngine(".xml")
    obj = engine.read_file()
    df = engine.to_xlsx(obj)
    assert isinstance(df, pd.DataFrame)
    assert (df == pd.DataFrame([{'A.B.0': 'B', 'A.B.1': 'B', 'A.C.D': 'D'}])).all().all()


def test_to_destination():
    # form a xml datatype
    obj = "<a><b>b</b></a>"
    destination = os.path.join(os.getcwd(), "tests", "sample_files", "result.xml")
    d_engine = xEngine.dest_xEngine(obj, destination)
    d_engine.to_destination()
    assert os.path.exists(destination)
    os.remove(destination)