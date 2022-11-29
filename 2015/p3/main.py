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


def result_of_delivery_robo_and_santa(route):
    houses_visited = {"0,0": 1}
    snt_x = 0
    snt_y = 0
    rob_x = 0
    rob_y = 0

    for index, direction in enumerate(route):
        if index % 2 == 0:
            snt_x, snt_y = receive_coordinates(direction, snt_x, snt_y)
            snt_house = f"{snt_x},{snt_y}"
            check_if_house_got_a_visit(snt_house, snt_x, snt_y, houses_visited)
        else:
            rob_x, rob_y = receive_coordinates(direction, rob_x, rob_y)
            rob_house = f"{rob_x},{rob_y}"
            check_if_house_got_a_visit(rob_house, rob_x, rob_y, houses_visited)

    return len(houses_visited), count_delivered_presents(houses_visited)


def check_if_house_got_a_visit(house, x, y, houses_visited):
    if house in houses_visited:
        houses_visited[house] += 1
    else:
        houses_visited.update({house: 1})


print(f"Only santa: {result_of_present_delivery(directions)}")
print(f"Santa and Robo-Santa{result_of_delivery_robo_and_santa(directions)}")


