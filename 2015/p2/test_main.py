import pytest


from main import calculate_package_wrappings


def test_calculate_package_wrappings_shuld_return_58_square_feet():
    data = "2x3x4"
    actual = calculate_package_wrappings(data)
    assert actual == 58


def test_calculate_package_wrappings_shuld_return_43_square_feet():
    data = "1x1x10"
    actual = calculate_package_wrappings(data)
    assert actual == 43

