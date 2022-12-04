def read_assignments_list(file_name):
    list_of_sets = list()
    with open(f"{file_name}", "r") as file:
        lines = file.readlines()
        for line in lines:
            set_a, set_b = transform_line_in_to_sets(line)
            list_of_sets.append([set_a, set_b])
    return list_of_sets


def transform_line_in_to_sets(line):
    pairs = line.strip("\n").split(",")
    range_a = pairs[0].split("-")
    range_b = pairs[1].split("-")
    set_a = {*range(int(range_a[0]), int(range_a[1]) + 1)}
    set_b = {*range(int(range_b[0]), int(range_b[1]) + 1)}
    return set_a, set_b


def count_assignment_pairs_fully_contain_the_other(list_of_assigments):
    counter = 0
    for pairs in list_of_assigments:
        if is_fully_contains_the_other(pairs[0], pairs[1]):
            counter += 1
    return counter


def is_fully_contains_the_other(set_a, set_b):
    if set_a.issubset(set_b):
        return True
    if set_b.issubset(set_a):
        return True
    return False


# --- part 2
def is_overlapping_the_other(set_a, set_b):
    if len(set_a.intersection(set_b)) > 0:
        return True
    return False


def count_assignment_pairs_overlaps_the_other(list_of_assigments):
    counter = 0
    for pairs in list_of_assigments:
        if is_overlapping_the_other(pairs[0], pairs[1]):
            counter += 1
    return counter


# part 1
list_of_pairs_p1 = read_assignments_list("data")
print(count_assignment_pairs_fully_contain_the_other(list_of_pairs_p1))

# part 2
list_of_pairs_p2 = read_assignments_list("data")
print(count_assignment_pairs_overlaps_the_other(list_of_pairs_p2))
