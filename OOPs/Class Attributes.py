class Car:
    """This is a simple class to represent a car."""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Accessing built-in class attributes
print("Documentation:", Car.__doc__)
print("Module:", Car.__module__)
print("Dictionary:", Car.__dict__)
print("Name:", Car.__name__)
print("Bases:", Car.__bases__)
