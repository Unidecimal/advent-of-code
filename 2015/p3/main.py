def result_of_present_delivery(route):
    houses_visited = {"0,0": 1}
    x = 0
    y = 0

    for direction in route:
        x, y = receive_coordinates(direction, x, y)
        house = f"{x},{y}"
        if house in houses_visited:
            houses_visited[house] += 1
        else:
            houses_visited.update({house: 1})
    return len(houses_visited), count_delivered_presents(houses_visited)


def receive_coordinates(direction, x, y):
    if direction == ">":
        x += 1
    if direction == "<":
        x -= 1
    if direction == "^":
        y += 1
    if direction == "v":
        y -= 1
    return x, y


def count_delivered_presents(houses_visited):
    number_of_presents = 0
    for key in houses_visited:
        number_of_presents += houses_visited[key]
    return number_of_presents


with open("data", "r") as file:
    directions = file.readline()


print(result_of_present_delivery(directions))
