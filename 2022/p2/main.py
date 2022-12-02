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

    handsigns = string.split(" ")
    elf_handsign = handsigns[0]
    your_handsign = handsigns[1]
    return shape_score(your_handsign) + round_score(elf_handsign, your_handsign)


def match_point_rigged_matches(string):

    strategy = string.split(" ")
    elf_handsign = strategy[0]
    match_result = strategy[1]
    return round_and_shape_score_if_rigged(match_result, elf_handsign)


def shape_score(handsign):

    if handsign in "AX":
        return 1
    if handsign in "BY":
        return 2
    if handsign in "CZ":
        return 3


def round_score(elf_handsign, your_handsign):

    if elf_handsign == "A" and your_handsign == "X":
        return 3
    if elf_handsign == "A" and your_handsign == "Y":
        return 6
    if elf_handsign == "A" and your_handsign == "Z":
        return 0
    if elf_handsign == "B" and your_handsign == "X":
        return 0
    if elf_handsign == "B" and your_handsign == "Y":
        return 3
    if elf_handsign == "B" and your_handsign == "Z":
        return 6
    if elf_handsign == "C" and your_handsign == "X":
        return 6
    if elf_handsign == "C" and your_handsign == "Y":
        return 0
    if elf_handsign == "C" and your_handsign == "Z":
        return 3


def round_and_shape_score_if_rigged(match_result, elf_handsign):

    if match_result == "Z" and elf_handsign == "A":
        return 6 + shape_score("B")
    if match_result == "Z" and elf_handsign == "B":
        return 6 + shape_score("C")
    if match_result == "Z" and elf_handsign == "C":
        return 6 + shape_score("A")
    if match_result == "X" and elf_handsign == "A":
        return 0 + shape_score("C")
    if match_result == "X" and elf_handsign == "B":
        return 0 + shape_score("A")
    if match_result == "X" and elf_handsign == "C":
        return 0 + shape_score("B")
    if match_result == "Y" and elf_handsign == "A":
        return 3 + shape_score("A")
    if match_result == "Y" and elf_handsign == "B":
        return 3 + shape_score("B")
    if match_result == "Y" and elf_handsign == "C":
        return 3 + shape_score("C")


list = read_strategy_plan_and_return_score_list(True)
print(f"{sum(list)}, {len(list)}")

