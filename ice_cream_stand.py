# Exercises from Chapter 9 of Python Crash Course - Classes


# Exercise 9-6
class Restaurant:
    """Modelling the description of Restaurants and their cuisines"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise restaurant information with two key attributes,
        the restaurant name and the cuisine it serves"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Announces the name of the restaurant and the cuisine served"""
        print(f"This restaurant is named {self.restaurant_name}")
        print(f"It serves {self.cuisine_type}\n")

    def open_restaurant(self):
        """Announces that the restaurant is open"""
        print(f"{self.restaurant_name} is open.\n")

    def customers_served(self):
        """Print the number of customers served in the restaurant"""
        print(f"{self.restaurant_name} "
              f"has served {self.number_served} customers.")

    def set_customers_served(self, customers):
        """Allow user to set the number of customers served"""
        self.number_served = customers

    def increment_customers_served(self, increment):
        self.number_served += increment


class IceCreamStand(Restaurant):
    """A subclass of Restaurant that represents elements of an Ice Cream Stand"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialise attributes of the parent class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'raspberry', 'blood orange']

    def show_ice_cream(self):
        print(f"These ice cream flavors are available:")
        print(self.flavors)


# Creating an instance called ice_cream that represents an Ice Cream Stand
ice_cream = IceCreamStand("I Scream", "Ice Cream")
ice_cream.describe_restaurant()
ice_cream.open_restaurant()
print("")
ice_cream.show_ice_cream()


