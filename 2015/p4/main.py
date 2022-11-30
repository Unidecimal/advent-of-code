import hashlib


def mine_advent_coins(secret_key, zero_num, start_num):
    # key_part_1 = "abcdef"

    i = start_num
    zeros_to_reach = f"{'0'*zero_num}"
    current_number = None
    result = None
    while current_number != zeros_to_reach:
        i += 1
        teststring = f"{secret_key}{i}"
        result = hashlib.md5(teststring.encode()).hexdigest()
        current_number = result[:zero_num]

    return f"Hex hash: {result}, Mined key: {i}, Complete coin: {secret_key + str(i)}"


print(mine_advent_coins("bgvyzdsv", 5, 3000))
print(mine_advent_coins("bgvyzdsv", 6, 250000))
