class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)

    def give_raise(self, increase=5000):
        """Raise the annual salary of the employee by $5000 or given amount."""
        self.salary = self.salary + increase


