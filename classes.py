class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(2,8)
print(p.x)
print(p.y)

# same more easy without class
p.x = 6
p.y = 4

print(p.x)
print(p.y)

# Booking passangers in the flight, but non more than places in the that plane.

class Flight():
    # Create a new flight
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    # Add new passengers to that flight
    def add_passanger(self, name):
        if not self.open_seats():
            return False
        self.passangers.append(name)
        return True

    # Verifing now many seats are free
    def open_seats (self):
        return self.capacity - len(self.passangers)

flight = Flight(3)

# People list to the flight, and reservation is successfull added
people =["Henry", "Adam", "Marry", "Arian"]
for person in people:
    if flight.add_passanger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No avaliable seats for {person}.")