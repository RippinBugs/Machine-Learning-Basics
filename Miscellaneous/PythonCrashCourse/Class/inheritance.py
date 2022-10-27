class Car():
    """A simple attempt to represent a car"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " "+ self.model
        return long_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self,mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't rollback an odometer")
    
    def increment_odometer(self,miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("Fill the gas tank")


#instances as attributes
class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"this car has a batter of size {self.battery_size}")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 90:
            range = 270

        message = "this car can go " + str(range)
        message += " on a full charge"
        print(message)

#inheritance
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes to the parent class"""
        super().__init__(make, model, year)
        #self.battery_size = 70
        self.battery = Battery()
    
    # def describe_battery(self):
    #     print(f"this car has a battery of {self.battery_size}")

    def fill_gas_tank(self):
        #here we use overriding
        #in overriding child class will get the priority always. So when calling 
        #this method it will execute the codes inside the child class
        """For electric cars you don't need to fill the gas tank"""
        print("This car doesn't need a gas tank")
    

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
# my_tesla.fill_gas_tank()
print(my_tesla.battery.battery_size)
my_tesla.battery.get_range()
my_tesla.battery.battery_size= 90
my_tesla.battery.get_range()
        