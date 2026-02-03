class Transport:
    def action(self):
        print("Transport is in motion.")

class Sedan(Transport):
    def action(self):
        print("Car is driving forward.")

class Cycle(Transport):
    def action(self):
        print("Bicycle is being pedaled.")

objects = [Sedan(), Cycle()]

for item in objects:
    item.action()
