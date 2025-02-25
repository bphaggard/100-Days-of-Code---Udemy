def add (*args): #with *args we can use as many arguments as we want. We can use any name and not args
    return sum(args)

print(add(2, 5, 8, 12, 3, 10))

def calculate(**kwargs): #kwargs means many keyword arguments
    print(kwargs) #return dictionary

calculate(add=3, multiply=5)

class Car:

    def __init__(self, **kwargs): #optional arguments
        self.make = kwargs.get("make") #with get() it will return None if we will not specify value. Without it, it will return error
        self.model = kwargs.get("model")

my_car = Car(make="Ford")
print(my_car.make)