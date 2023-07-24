class Employee:
    """Set up a model for employee information."""

    def __init__(self, first_name, last_name, annual_salary):
        """intial model for employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_default_raise(self):
        """add money to the annual salary by default."""
        self.annual_salary += 5000
    
    def give_custom_raise(self, raise_amount):
        """annual salary increased by customise."""
        self.annual_salary += raise_amount