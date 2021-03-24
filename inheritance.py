# INHERITANCE AND COMPOSITIONG: A PYTHON OOP GUIDE.
# in this article, you'll explore inheritance and compostition in Python
# Inheritance and composition are two important concepts in object oriented programming
# that model the relationship between two classes.
# They are the building blocks of object oriented design,
# and they help programmers to write resuable code.
# By the end of this article, you will know how to:
# Use inheritance in Python
# Model calss hierarchies using inheritance
# Use multiple inheritance in Python and understand its drawbacks
# Use compostiont to creat complex objects
# Resuse existing code by applying composition
# change application behaviour at run-time through compostition
# WHAT ARE INHERITANCE AND COMPOSITION?
# Inheritance and composition are two major concepts in oop that
# model the relationship between two classes.
# They drive the design of an application and determine
# how the application should evolve as new features are added 
# or requirements changes.
# Both of them enable code reuse, but they do it in different ways.
# WHAT IS INHERITANCE?
# Inheritance models what is called an is a relationship.

# This means that when you have a Derived class that inherits from a Base call,
# you created a relationship where Derived is a specialized version of Base.







# CREATING CLASS HIERARCHIES 
# Inheritance is the mechanism you will use to create hierarchies of related classes.
# These related classes will share a common interface that will be defined
# in the base classes.
# Derived classes can specialize the interface by providing a particular
# implementation where applies.
# In this section, you will start modeling an HR system.
# The example will demonstrate the use of inheritance 
# and how derived classes can provide a concrete implementation of the base class interface.

# The HR system needs to process payroll for the company's employees, 
# but there are different types of employees depending on how their payroll is calculated.

# You start by implementing a PayrollSystem class that processes payroll:

class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('------------')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {emloyee.name}')
            print(f' - Check amount: {employee.calculate_payroll()}')
            print('')
# The PayrollSystem implements a.calculate_payroll() method 
# that takes a collection of employees and prints their id, name, and
# check amount using the .calculate_payroll() method
# exposed on each employee object.

# Now, you implement a base class Employee that handles the common interface
# for every employee type:

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
# Employee is the base class for all employee types
# It is constructed with an id and name.
# what you are saying is that every Employee must have an id assigned as well as a name.
# 
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)        
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary
# You create a derived class SalaryEmployee that inherits Employee 
# The class is initialized with the id and name required by the base class, 
# and you use super() to initialize the members of the base class.
# You can read all about super() in Superchange your classes with python super()

# SalaryEmployee also requires a weekly_salary initialization parameter that
# represents the amount the employee makes per week.
# The class provides the required .calculate_payroo() method used by the HR system.
# The implementation just returns the amount stored in weekly_salary.
# the company also employs manufacturing workers that are paid by the hour,
# so you add an HourlyEmployee HR system:

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked 
        self.hour_rate = hour_rate
    
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

# The HourlyEmployee class is initialized with id and name,
# like the base class plus the 
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission
    
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.compostition




You derive CommissionEmployee from SalaryEmployee
because both classes have a weekly_salary to consider.
at the same time, CommissionEmployee is initialized with
a commission value that is based on the sales for the employee.

calculate_payroll() leverages the implementation of the base class
to retrieve the fixed salary and adds the commission value.









The diagram shows the inheritance hierarchy of the classes.
The derived classes implement the IPayrollCalculator interface,
which is required by the PayrollSystem.
The PayrollSystem.calculate_payroll() implementation requires
that the employee objects passed contain an id, name, and calculate_payroll() implementation.
Interfaces are represented similarly to classes with the word interface above the interface name.
Interface names are usually prefixed with a capital I.

The application creates its employees and passes them to the payroll system to process payroll:
You can run the program in the command line and see the results:
