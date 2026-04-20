# 9-m
class Laptop:
    def __init__(self, model, ram):
        self.model = model
        self.ram = ram

    def show_specs(self):
        print(f"{self.model} {self.ram} RAM")

l1 = Laptop("My Laptop", 512)
l1.show_specs()

