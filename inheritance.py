class Animal:
    def __init__(self):
        self.num_eyes =2

    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self): #if you want to change somenthing or add in breathe function inside fish
        # class call breathe function from animal class using
        # super and add the lines below it see the example below
        super().breathe()
        print("under water")

    def swim(self):
        print("Moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

