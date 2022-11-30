from main import naughty_string_identifier, is_nice_or_naughty


def test_string_should_be_nice():
    suspect_string_no_1 = "ugknbfddgicrmopn"

    actual_1 = is_nice_or_naughty(suspect_string_no_1)

    assert actual_1 == "nice"


def test_string_should_be_nice_naughty_no_double_letters():
    suspect_string_no_2 = "jchzalrnumimnmhp"
    actual_2 = is_nice_or_naughty(suspect_string_no_2)
    assert actual_2 == "naughty"


def test_string_should_be_nice_naughty_contains_xy():
    suspect_string_no_3 = "haegwjzuvuyypxyu"
    actual_3 = is_nice_or_naughty(suspect_string_no_3)
    assert actual_3 == "naughty"


def test_string_should_be_nice_naughty_no_vowel():
    suspect_string_no_4 = "dvszwmarrgswjxmb"
    actual_4 = is_nice_or_naughty(suspect_string_no_4)
    assert actual_4 == "naughty"


