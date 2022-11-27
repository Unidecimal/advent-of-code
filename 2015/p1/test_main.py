import pytest
from main import find_target_floor, find_position_of_caracter_at_floor

def test_find_target_floor_should_return_zero():
    data_1 = "(())"
    data_2 = "()()"
    real_1 = find_target_floor(data_1)
    real_2 = find_target_floor(data_2)
    assert real_1 == 0
    assert real_2 == 0


def test_find_target_floor_should_return_tree():
    data_1 = "((("
    data_2 = "(()(()("
    data_3 = "))((((("
    real_1 = find_target_floor(data_1)
    real_2 = find_target_floor(data_2)
    real_3 = find_target_floor(data_3)
    assert real_1 == 3
    assert real_2 == 3
    assert real_3 == 3


def test_find_target_floor_should_return_minus_one():
    data_1 = "())"
    data_2 = "))("

    real_1 = find_target_floor(data_1)
    real_2 = find_target_floor(data_2)
    assert real_1 == -1
    assert real_2 == -1


def test_find_target_floor_should_return_minus_tree():
    data_1 = ")))"
    data_2 = ")())())"

    real_1 = find_target_floor(data_1)
    real_2 = find_target_floor(data_2)
    assert real_1 == -3
    assert real_2 == -3

def test_find_position_of_caracter_specified_should_return_one():
    data_1 = "(()))()"
    floor = 1
    real_1 = find_position_of_caracter_at_floor(data_1, floor)
    assert real_1 == 1

def test_find_position_of_caracter_specified_should_return_five():
    data_1 = "()())(()))()"
    floor = -1
    real_1 = find_position_of_caracter_at_floor(data_1, floor)
    assert real_1 == 5

