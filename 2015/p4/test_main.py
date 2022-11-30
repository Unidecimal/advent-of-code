from main import mine_advent_coins


def test_mine_advent_coin_should_be_609043():
    secret_key = "abcdef"
    number_of_zeros = 5
    start_number = 600000
    expected = f"Hex hash: 000001dbbfa3a5c83a2d506429c7b00e, Mined key: 609043, Complete coin: abcdef609043"

    real = mine_advent_coins(secret_key, number_of_zeros, start_number)
    assert real == expected


def test_mine_advent_coin_should_be_1048970():
    secret_key = "pqrstuv"
    number_of_zeros = 5
    start_number = 600000
    expected = f"Hex hash: 000006136ef2ff3b291c85725f17325c, Mined key: 1048970, Complete coin: pqrstuv1048970"

    real = mine_advent_coins(secret_key, number_of_zeros, start_number)
    assert real == expected

