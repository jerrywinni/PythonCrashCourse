# Here we import the Battery class from the battery module
from batteries import Battery

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # assigned a default value
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """Set the odemeter reading to the given value.
           Rejct the change if it attempts to roll the odometer back.
           Returns True if the update was successful, and False otherwise.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            return True
        else:
            print("You cannot roll back an odometer!")
            return False
        
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading +=miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.   
        """
        super().__init__(make, model, year) # The super() function in Python is used to call a method from a parent class in a child class. 
        self.battery = Battery() # create a new instance of Battery and assign that instance to the attribute self.battery.  
                                 # This will happen every time the __init__() method is called; any ElectricCar instance will now have a Battery instance created automatically.