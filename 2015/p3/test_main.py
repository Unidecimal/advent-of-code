import pytest
from unittest import TestCase
from main import result_of_present_delivery, receive_coordinates


def test_result_of_present_delivery_should_return_two_houses_visited_and_two_presents_delivered():
    data = ">"
    actual = result_of_present_delivery(data)
    assert actual == (2, 2)


def test_result_of_present_delivery_should_return_four_houses_visited_and_five_presents_delivered():
    data = "^>v<"
    actual = result_of_present_delivery(data)
    assert actual == (4, 5)


def test_result_of_present_delivery_should_return_two_houses_visited_and_eleven_presents_delivered():
    data = "^v^v^v^v^v"
    actual = result_of_present_delivery(data)
    assert actual == (2, 11)


def test_receive_coordinates():
    data_east = ">"
    data_west = "<"
    data_north = "^"
    data_south = "v"
    actual_east = receive_coordinates(data_east, 0, 0)
    actual_west = receive_coordinates(data_west, 0, 0)
    actual_north = receive_coordinates(data_north, 0, 0)
    actual_south = receive_coordinates(data_south, 0, 0)
    assert actual_east == (1, 0)
    assert actual_west == (-1, 0)
    assert actual_north == (0, 1)
    assert actual_south == (0, -1)


