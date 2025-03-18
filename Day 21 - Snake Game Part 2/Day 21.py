class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()

#Python slicing
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys[2:5]) # return c, d, e. Sliced list for 3 items
print(piano_keys[2:]) # return c and everything to the end of the list
print(piano_keys[::2]) # skip second items
