import pytest


from main import calculate_package_wrappings, calculate_ribbons_in_feet


def test_calculate_package_wrappings_shuld_return_58_square_feet():
    data = "2x3x4"
    actual = calculate_package_wrappings(data)
    assert actual == 58


def test_calculate_package_wrappings_shuld_return_43_square_feet():
    data = "1x1x10"
    actual = calculate_package_wrappings(data)
    assert actual == 43


def test_calculate_ribbons_in_feet_shuld_be_34():
    data = "2x3x4"
    actual = calculate_ribbons_in_feet(data)
    assert actual == 34


def test_calculate_ribbons_in_feet_shuld_be_14():
    data = "1x1x10"
    actual = calculate_ribbons_in_feet(data)
    assert actual == 14

