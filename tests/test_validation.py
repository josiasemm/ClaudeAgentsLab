from src.validation import validate_title


def test_empty_title_is_invalid():
    assert validate_title("") is False
