# #class name should always start with capital letter.
# class Dog():
#     """
#     Basics of class
#     """
#     def __init__(self,name,age):
#         #this name and age are attributes
#         self.name = name
#         self.age = age
    
#     #the functions are called method
#     def sitting(self):
#         print(f"{self.name} sits rn")

#     def age_for_sports(self):
#         if self.age > 5 :
#             print(f"applicable for sport with age of {self.age}")
#         else:
#             print(f"not applicable for sport with age of {self.age}")


# my_dog = Dog('henry',35)
# my_dog.sitting()
# my_dog.age_for_sports()



class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #setting a default value

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " +self.model
        return long_name

    def read_odometer(self):
        print("this car has " + str(self.odometer_reading)+" miles on it")
        
    def update_odometer(self,mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
            print(f"odometer rating is now {self.odometer_reading}")
        else:
            print("you can't roll back an odometer")

    
    def increment_odemeter(self,miles):
        self.odometer_reading += miles
    
    

my_new_car = Car('Audi','a4',2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer(20)
# my_new_car.read_odometer(19)

#three ways to modify attribute values
#1 - modifying attribute's value directly
#my_new_car.odometer_reading = 40
#my_new_car.update_odometer(39) 

#2 - modifying an attribute's value through a method
my_new_car.update_odometer(41) 
my_new_car.read_odometer()

#incrementing an attribute's value through a method
my_new_car.increment_odemeter(105)
print(my_new_car.odometer_reading)
my_new_car.read_odometer()

