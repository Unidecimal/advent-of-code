
def read_and_store_data():
    elfs_list = {}
    elf_calories = []
    with open("data", "r") as file:
        lines = file.readlines()
        elf = 0
        for line in lines:

            if line.strip() == "":
                elf += 1
                elfs_list[elf] = sum(elf_calories)
                elf_calories = []
            else:
                elf_calories.append(int(line))
    print(elfs_list)
    return elfs_list


def find_snackiest_elf(elf_list):
    max_elf = 0
    max_value = 0

    for elf, value in elf_list.items():
        #print(f"{elf},{value=}")
        if value > max_value:
            max_value = value
            max_elf = elf

    return max_elf, max_value


def find_the_tree_snackiest_elf(elf_list):
    elf_list_modified = elf_list
    the_three = []
    elf = ()
    for i in range(3):
        elf, value = find_snackiest_elf(elf_list)
        the_three.append((elf, value))
        elf_list_modified[elf] = 0
    return the_three


def sum_the_three(elf_list):
    elf_sum = 0
    for i in elf_list:
        elf, value = i
        elf_sum += value
    return elf_sum


print(find_snackiest_elf(read_and_store_data()))

print(sum_the_three(find_the_tree_snackiest_elf(read_and_store_data())))


