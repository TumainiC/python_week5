# **Assignment 1: Design Your Own Class!** 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

# **Activity 2: Polymorphism Challenge! 🎭**

# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() 
# differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).


class TheBoys:
    # During class definition, no brackets
    # constructor - allows each instance of the class to have unique atributes
    def __init__(self, name, role):
        # unique attributes
        self.name = name
        self.role = role

    # method    
    def capture_supe(self, supe_name):
        print(f"{self.name}, you're the {self.role} and that's {supe_name}! We got em boys!") 

    # encapsulation 
    def clean(self):
        if self.role.lower() == "guns":
            print("This place is a mess! I gotta do everything myself")
        else:
            print("Hell no, MM is gonna do it anyway.")

# calling an instance of a class
boys1 = TheBoys("Kimiko", "muscle")
boys1.capture_supe("Homelander")

boys1.clean()

# Defining subclass with inheritance
class Frenchie(TheBoys):
    # polymorphism
    def capture_supe(self, supe_name):
        print(f"Merde! I'm not high, I promise. I've got {supe_name}!") 

    

boys2 = Frenchie("Frenchie", "chemicals")
boys2.capture_supe("Neuman")

# encapsulation
boys3 = TheBoys("MM", "guns")
boys3.clean()