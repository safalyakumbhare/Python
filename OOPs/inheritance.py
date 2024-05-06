# Define the superclass
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Define a subclass inheriting from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

# Define another subclass inheriting from Animal
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

# Create instances of the subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method of each instance
dog.speak()  # Output: Buddy barks
cat.speak()  # Output: Whiskers meows
