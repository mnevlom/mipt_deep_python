import io
from file_filter import file_filter


def test_file_filter_base():
    fake_file_rus = io.StringIO("первая строка\nвторая строка с ключом\nтретья строка\n")
    fake_file_eng = io.StringIO("first string\nsecond string with key\nthird string\n")
    res_rus = list(file_filter(fake_file_rus, ["ключом"], []))
    res_eng = list(file_filter(fake_file_eng, ["key"], []))
    assert res_rus == ["вторая строка с ключом\n"]
    assert res_eng == ["second string with key\n"]


def test_file_filter_stop_words():
    fake_file = io.StringIO("первая строка\nвторая строка с ключом\nтретья строка\n")
    res = list(file_filter(fake_file, ["строка"], ["первая"]))
    assert res == ["вторая строка с ключом\n", "третья строка\n"]


def test_file_filter_case():
    fake_file = io.StringIO("пеРВая СТроКа\nвторая СТРОКА с клЮЧоМ\nтретья строка\n")
    res = list(file_filter(fake_file, ["строка"], []))
    assert res == ["пеРВая СТроКа\n", "вторая СТРОКА с клЮЧоМ\n", "третья строка\n"]


def test_file_filter_real_file(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("а Роза упала на лапу Азора\n", encoding="utf-8")
    res_go = list(file_filter(str(file_path), ["роза"], []))
    res_stop = list(file_filter(str(file_path), ["роза"], ["азора"]))
    assert res_go == ["а Роза упала на лапу Азора\n"]
    assert res_stop == []
