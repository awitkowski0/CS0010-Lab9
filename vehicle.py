class Vehicle:
    """
    Inside of our __init__ function, we're going to declare all of our variables we previously went over:

    color: “Red”
    (this is a string)

    wheels: 4
    (this is an int)

    gear: “Park”
    (this is a string)
    
    We need the cars “speed”
    speed: 0
    (this is an int)

    This cars location… assuming a 2D flat land
    location_x: 0
    (this is an int)

    Every __init__ function needs a self variable to access it's own variables
    The color and wheels here say we're letting whoever declares this variable to assign these values

    Think back to when you declare an integer

    var1 = 10

    this would be defined as
    def __init__(self, number):
        self.number = number

    so for us we have to think of this
    
    Tesla = Car("Red", 4)
    """
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

        # By having these three here always set to something, we have "constants" or values that will always be initialized as the same thing
        self.gear = "P"
        self.speed = 0
        self.location_x = 0
    

    # We need a function represent stepping on the gas pedal
    def gas_pedal(self):
        if self.gear == "D" or self.gear == "R":
            self.speed += 1
    # Needs to be able to break
    def break_pedal(self):
        # If we're breaking, decrease the speed
        if self.speed > 0:
            self.speed -= 1
        else:
            self.speed = 0

    # Assuming automatic, needs a gear selector
    def change_gears(self, gear):
        self.gear = gear
    # Tick is basically just a way we keep our object constantly running, as in time passing
    def tick(self):
        if not(self.speed == 0):
            # If our car is in park or neutral... the gas does nothing
            if self.gear == "P" or self.gear == "N":
                self.speed = 0
            # If we're in drive, speed should increase
            elif self.gear == "D":
                self.location_x += (self.speed * self.wheels)
            # If we're in reverse, speed should be negative
            elif self.gear == "R":
                self.location_x -= (self.speed * self.wheels)
