from findex.tokenize import tokenize

def test_tokenize_nfc_cafe():
    assert list(tokenize("café")) == list(tokenize("cafe\u0301"))

def test_tokenize_rules():
    text = "Комп'ютер-програма 123"
    assert list(tokenize(text)) == ["комп'ютер-програма", "123"]