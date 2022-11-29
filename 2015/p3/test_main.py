from main import result_of_present_delivery


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


