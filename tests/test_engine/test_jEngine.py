import os
import pandas as pd
import pytest
from formatflick.engine import jEngine


def build_jEnfine(ext):
    file = os.path.join(os.getcwd(), "tests", "sample_files", "sample" + ext)
    engine = jEngine.jEngine(source=file, mode='file', source_extension=ext)
    return engine


def test_read_file():
    engine = build_jEnfine(".json")
    headers, data = engine.read_file()
    print(data)
    print(headers)
    assert isinstance(data, list)
    assert data == [{'a': 'b', 'c.d.0': 'a', 'c.d.1': 'b', 'c.e.f': 'f-1'}]
    assert sorted(headers) == sorted(['c.d.0', 'a', 'c.d.1', 'c.e.f'])


def test_to_csv():
    engine = build_jEnfine(".json")
    headers, data = engine.read_file()
    df = engine.to_csv(data)
    assert type(df) is pd.DataFrame


def test_to_tsv():
    engine = build_jEnfine(".json")
    headers, data = engine.read_file()
    df = engine.to_tsv(data)
    assert type(df) is pd.DataFrame


def test_to_xlsx():
    engine = build_jEnfine(".json")
    headers, data = engine.read_file()
    df = engine.to_xlsx(data)
    assert type(df) is pd.DataFrame


def test_to_xml():
    engine = build_jEnfine(".json")
    headers, data = engine.read_file()
    df = engine.to_xml(data)
    assert b'<Result><a>b</a><c.d.0>a</c.d.0><c.d.1>b</c.d.1><c.e.f>f-1</c.e.f></Result>' == df


def test_to_destination():
    json_data = '{"name": "John", "age": 30, "city": "New York"}'
    destination = os.path.join(os.getcwd(), "tests", "sample_files", "result.json")
    d_engine = jEngine.dest_jEngine(json_data, destination)
    d_engine.to_destination()
    assert os.path.exists(destination)
    os.remove(destination)
