# Exercises from Chapter 9 of Python Crash Course - Classes

# Exercise 9-1 & 9-2
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
        print(f"It serves {self.cuisine_type} cuisine\n")

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


"""Create three instances of restaurants and call both methods for each"""
restaurant_1 = Restaurant("Mario's Pizza", "Pizza and Pasta")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_1.set_customers_served(20)
restaurant_1.increment_customers_served(100)
restaurant_1.customers_served()
restaurant_1.increment_customers_served(100)
restaurant_1.customers_served()
