import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

say_hello() # use decorated function delay_decorator
say_bye() # use decorated function delay_decorator
say_greeting() # does not use decorated function delay_decorator