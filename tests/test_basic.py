from src.builder_intelligence.builders import normalize_builder_name

def test_normalize_builder_name():
    assert normalize_builder_name(" lennar ") == "Lennar"
