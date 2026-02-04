class vehical:
    def move(self):
        print("these vehicle is moving.")


class car(vehical):
    def move(self):
        print("driving on the road")


class bicycle(vehical):
    def move(self):
        print("pedaling on the road")


vehicles = [car(), bicycle()]
for vehicle in vehicles:
    vehicle.move()