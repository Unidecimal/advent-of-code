def calculate_package_wrappings(box_size):
    l, w, h = [int(x) for x in box_size.split("x")]
    total_area = [(2 * l * w), (2 * w * h), (2 * h * l)]
    extra = min(total_area)/2
    total_area.append(extra)
    return sum(total_area)


def calculate_ribbons_in_feet(box_size):
    pass


with open("data", "r") as file:
    total_area = 0
    lines = file.readlines()
    for line in lines:
        print(f"{line}")
        total_area += calculate_package_wrappings(line.strip("\n"))


print(total_area)