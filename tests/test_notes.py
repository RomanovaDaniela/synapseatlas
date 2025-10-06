from synapseatlas.core.notes import extract
def test_parse():
    s="Тест [[Связь]] и #tag1 #tag2"
    meta = extract(s)
    assert "Связь" in meta["links"]
    assert "tag1" in meta["tags"] and "tag2" in meta["tags"]
