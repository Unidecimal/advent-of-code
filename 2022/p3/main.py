# data = "vJrwpWtwJgWrhcsFMMfFFhFp"
# hlen = int(len(data)/2)
# set1 = set(data[:hlen])
# set2 = set(data[hlen:])
# set3 = list(set1.intersection(set2))[0]


def find_item_type_that_appears_in_both_compartments(rucksack_items):

    hlen = int(len(rucksack_items) / 2)
    comp_a = set(rucksack_items[:hlen])
    comp_b = set(rucksack_items[hlen:])
    return list(comp_a.intersection(comp_b))[0]


def load_list_of_rucksacks():
    list_of_rucksacks = list()
    with open("data", "r") as file:
        lines = file.readlines()
        for line in lines:
            list_of_rucksacks.append(line.strip("\n"))
        return list_of_rucksacks


def search_rucksacks_compartments(list_of_rucksacks):
    list_of_items = list()
    for rucksack in list_of_rucksacks:
        list_of_items.append(find_item_type_that_appears_in_both_compartments(rucksack))
    return list_of_items


def sum_priorities_item(list_of_items):
    total_value = 0
    priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for item in list_of_items:
        total_value += priority.rfind(item) + 1
    return total_value


def load_list_of_rucksacks_in_groups():
    list_of_groups = list()
    rucksacks_group = list()
    with open("data", "r") as file:
        lines = file.readlines()
        grope_size = 0
        for line in lines:
            if grope_size < 3:
                rucksacks_group.append(line.strip("\n"))
                grope_size += 1
                if grope_size > 2:
                    list_of_groups.append(rucksacks_group)
                    rucksacks_group = list()
                    grope_size = 0

        return list_of_groups


def find_item_type_that_appears_in_rucksack_group(rucksack_group):

    rucksack_1 = set(rucksack_group[0])
    rucksack_2 = set(rucksack_group[1])
    rucksack_3 = set(rucksack_group[2])
    return list(rucksack_1.intersection(rucksack_2, rucksack_3))[0]


def search_rucksacks_in_group(list_of_groups):
    list_of_items = list()
    for rucksack_group in list_of_groups:
        list_of_items.append(find_item_type_that_appears_in_rucksack_group(rucksack_group))
    return list_of_items


# part one
print(sum_priorities_item(search_rucksacks_compartments(load_list_of_rucksacks())))

# part two
print(sum_priorities_item(search_rucksacks_in_group(load_list_of_rucksacks_in_groups())))
