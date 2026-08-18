class Product:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Product: {self.name}")

class Electronic(Product):

    def __init__(self, name, warranty_years):
        super().__init__(name)
        self.warranty_years = warranty_years

    def display(self):
        print(f"Product: {self.name}")
        print(f"Warranty: {self.warranty_years} years")

def main():

    item = Product("Notebook")
    item.display()

    print()

    laptop = Electronic("Laptop", 3)
    laptop.display()

if __name__ == "__main__":
    main()