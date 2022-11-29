def result_of_present_delivery(route):
    for direction in route:
        



class House:
    def __init__(self, x, y, presents=1):
        self.x = x
        self.y = y
        self.presents = presents

    def get_house_coordinates(self):
        return self.x, self.y

    def deliver_present(self, number):
        self.presents += number
