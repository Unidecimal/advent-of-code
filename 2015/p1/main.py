def find_position_of_caracter_at_floor(data_1, target_floor):
    current_floor = 0

    for index, caracter in enumerate([*data_1]):
        if caracter in "(":
            current_floor += 1
        if caracter in ")":
            current_floor -= 1
        if current_floor == target_floor:
            return index + 1
    return


def find_target_floor(data):
    count_up = data.count("(")
    count_down = data.count(")")
    return count_up - count_down

with open('data', 'r') as file:
    data = file.read()

print(find_target_floor(data))
print(find_position_of_caracter_at_floor(data, -1))