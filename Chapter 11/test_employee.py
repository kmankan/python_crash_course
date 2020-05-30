from employee_info import Employee
import unittest


class EmployeeTestCase(unittest.TestCase):
    """Tests the employee_info.py functions"""

    def setUp(self):
        """"Create an employee model to use in below tests"""
        self.employee = Employee("Miko", "Bear", "1000000")
        self.employee_copy = Employee("Miko", "Bear", "1000000")

    def test_give_default_raise(self):
        """Test giving a default raise of $5000"""
        original_salary = self.employee.salary
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, original_salary + 5000)

    def test_give_custom_raise(self):
        """Test giving a custom raise of $77888"""
        original_salary = self.employee.salary
        increase = 77888
        self.employee.give_raise(increase)
        self.assertEqual(self.employee.salary, original_salary + 77888)


if __name__ == '__main__':
    unittest.main()
