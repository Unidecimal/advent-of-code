def read_strategy_plan_and_return_score_list(rigged=False):
    round_scores = []
    with open("data", "r") as file:
        lines = file.readlines()
        for line in lines:
            if rigged:
                round_scores.append(match_point_rigged_matches(line.strip("\n")))
            else:
                round_scores.append(match_point(line.strip("\n")))

    return round_scores


def match_point(string):

    shapes = string.split(" ")
    elf_shape = shapes[0]
    you_shape = shapes[1]
    return shape_score(you_shape) + round_score(elf_shape, you_shape)


def match_point_rigged_matches(string):

    strategy = string.split(" ")
    elf_shape = strategy[0]
    match_result = strategy[1]
    return round_and_shape_score_if_rigged(match_result, elf_shape)


def shape_score(shape):

    if shape in "AX":
        return 1
    if shape in "BY":
        return 2
    if shape in "CZ":
        return 3


def round_score(elf_shape, you_shape):

    if elf_shape == "A" and you_shape == "X":
        return 3
    if elf_shape == "A" and you_shape == "Y":
        return 6
    if elf_shape == "A" and you_shape == "Z":
        return 0
    if elf_shape == "B" and you_shape == "X":
        return 0
    if elf_shape == "B" and you_shape == "Y":
        return 3
    if elf_shape == "B" and you_shape == "Z":
        return 6
    if elf_shape == "C" and you_shape == "X":
        return 6
    if elf_shape == "C" and you_shape == "Y":
        return 0
    if elf_shape == "C" and you_shape == "Z":
        return 3


def round_and_shape_score_if_rigged(match_result, elf_shape):

    if match_result == "Z" and elf_shape == "A":
        return 6 + shape_score("B")
    if match_result == "Z" and elf_shape == "B":
        return 6 + shape_score("C")
    if match_result == "Z" and elf_shape == "C":
        return 6 + shape_score("A")
    if match_result == "X" and elf_shape == "A":
        return 0 + shape_score("C")
    if match_result == "X" and elf_shape == "B":
        return 0 + shape_score("A")
    if match_result == "X" and elf_shape == "C":
        return 0 + shape_score("B")
    if match_result == "Y" and elf_shape == "A":
        return 3 + shape_score("A")
    if match_result == "Y" and elf_shape == "B":
        return 3 + shape_score("B")
    if match_result == "Y" and elf_shape == "C":
        return 3 + shape_score("C")


list = read_strategy_plan_and_return_score_list(True)
print(f"{sum(list)}, {len(list)}")

