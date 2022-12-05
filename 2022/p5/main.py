stacks = {
    "1": ["V", "N", "F", "S", "M", "P", "H", "J"],
    "2": ["Q", "D", "J", "M", "L", "R", "S"],
    "3": ["B", "W", "S", "C", "H", "D", "Q", "N"],
    "4": ["L", "C", "S", "R"],
    "5": ["B", "F", "P", "T", "V", "M"],
    "6": ["C", "N", "Q", "R", "T"],
    "7": ["R", "V", "G"],
    "8": ["R", "L", "D", "P", "S", "Z", "C"],
    "9": ["F", "B", "P", "G", "V", "J", "S", "D"],
}
# [V]     [B]                     [F]
# [N] [Q] [W]                 [R] [B]
# [F] [D] [S]     [B]         [L] [P]
# [S] [J] [C]     [F] [C]     [D] [G]
# [M] [M] [H] [L] [P] [N]     [P] [V]
# [P] [L] [D] [C] [T] [Q] [R] [S] [J]
# [H] [R] [Q] [S] [V] [R] [V] [Z] [S]
# [J] [S] [N] [R] [M] [T] [G] [C] [D]
#  1   2   3   4   5   6   7   8   9

# test stacks
test_stacks = {
            "1": ["N", "Z"],
            "2": ["D", "C", "M"],
            "3": ["P"],
}

#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2


def read_moves_from_file(file):
    move_list = list()
    with open(f"{file}", "r") as file:
        lines_with_moves = file.readlines()
        for line in lines_with_moves:
            move_list.append(parce_moves(line))
    return move_list


def parce_moves(line):
    m_move = line.strip("\n").split(" ")[1]
    m_from = line.strip("\n").split(" ")[3]
    m_to = line.strip("\n").split(" ")[5]
    return m_move, m_from, m_to


def move_all_crates(moves, stacks):
    for move in moves:
        m_move, m_from, m_to = move
        for i in range(0, int(m_move)):
            move_a_crate_from_a_to_b(stacks[m_from], stacks[m_to])


def move_a_crate_from_a_to_b(stack_a, stack_b):
    crate = stack_a[0]
    del stack_a[0]
    stack_b.insert(0, crate)


def get_the_top_crates_as_string(stacks):
    top_crates = str()
    for key in stacks.keys():
        top_crates += stacks[key][0]
    return top_crates

# part 2:


def new_move_all_crates(moves, stacks):
    for move in moves:
        m_move, m_from, m_to = move
        move_multiple_crates_from_a_to_b(stacks[m_from], stacks[m_to], int(m_move))


def move_multiple_crates_from_a_to_b(stack_a, stack_b, number):
    crates = stack_a[0:number]
    del stack_a[0:number]
    for i, crate in enumerate(crates):
        stack_b.insert(i, crate)


# part 1
print(get_the_top_crates_as_string(test_stacks))
move_all_crates(read_moves_from_file("test_move_data"), test_stacks)
print(get_the_top_crates_as_string(test_stacks))

# part 2
new_move_all_crates(read_moves_from_file("move_data"), stacks)
print(stacks)
print(get_the_top_crates_as_string(stacks))
