from django.test import TestCase


# Create your tests here.
class Employee(object):

    employee_raise = 1.15

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@comapny.com'
        self.pay = pay

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.employee_raise)


class Developer(Employee):
    employee_raise = 1.25


emp1 = Developer('Mazz', 'Ahmed', 4000)
emp2 = Developer('Irtaza', 'Ali', 4400)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
