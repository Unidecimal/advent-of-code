import pytest
from unittest import TestCase
from main import result_of_present_delivery, receive_coordinates, result_of_delivery_robo_and_santa


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

    # ^v delivers presents to 3 houses, because Santa goes north, and then Robo - Santa goes south.
    # ^>v< now delivers presents to 3 houses, and Santa and Robo - Santa end up back where they started.
    # ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.


def test_result_delivers_presents_to_3_houses_because_santa_goes_north_and_then_robo_santa_goes_south():
    data = "^v"
    actual = result_of_delivery_robo_and_santa(data)
    assert actual == (3, 3)


def test_result_now_delivers_presents_to_3_houses_and_santa_and_robo_santa_end_up_back_where_they_started():
    data = "^>v<"
    actual = result_of_delivery_robo_and_santa(data)
    assert actual == (3, 5)


def test_result_now_delivers_presents_to_11_houses_with_santa_going_one_direction_and_robo_santa_going_the_other():
    data = "^v^v^v^v^v"
    actual = result_of_delivery_robo_and_santa(data)
    assert actual == (11, 11)
