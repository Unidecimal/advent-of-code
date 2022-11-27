def calculate_package_wrappings(box_size):
    l, w, h = [int(x) for x in box_size.split("x")]
    total_area = [(2 * l * w), (2 * w * h), (2 * h * l)]
    extra = min(total_area)/2
    total_area.append(extra)
    return sum(total_area)


def calculate_ribbons_in_feet(box_size):
    messurments = [int(x) for x in box_size.split("x")]
    lowest_nums = sorted(messurments)[0:2]
    bow = 1
    for value in messurments:
        bow *= value

    return sum([x + x for x in lowest_nums]) + bow


def openfile_and_count():
    with open("data", "r") as file:
        total_area = 0
        total_ribbon = 0
        lines = file.readlines()
        for line in lines:
            total_area += calculate_package_wrappings(line.strip("\n"))
            total_ribbon += calculate_ribbons_in_feet(line.strip("\n"))

    return f"Area of wrapping needed: {total_area} square feet, Length of ribbon needed: {total_ribbon} feet"


print(openfile_and_count())
