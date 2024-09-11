class Vehicle:
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class bus(Vehicle):
    pass

obj = bus("School Bus", 100, 200)
print("Bus name", obj.name, "Maximum speed", obj.maxspeed, "Mileage", obj.mileage)