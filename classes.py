class Point():

    def __init__(self, input1,input2):
        self.x = input1
        self.y = input2


p = Point(4,8)
print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity= capacity
        self.passengers=[]

    def add_passenger(self, person):
        if not self.open_seats() :
            return False
        else:
            self.passengers.append(person)
            return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
            

flight = Flight(3)

people = ["Anderson", "Rounds", "Costa", "Jackson"]

for person in people:
     
    if flight.add_passenger(person):
        print(f"{person} added to the flight")
    else:
        print(f"No available seat in the flight for {person}.")