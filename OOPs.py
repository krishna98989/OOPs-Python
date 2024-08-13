# the class variables , instance variables , class methods , static & Regular methods , 
# Making objects out of STR using class methods

class Employee():

    raise_percent = 2.5 #class variable
    Number_of_Employee = 0
    def __init__(self,fname,lname,pay) -> None:
        self.fname = fname
        self.lname = lname
        self.pay = pay

        Employee.Number_of_Employee+=1

    #Regular Method
    def full_name(self):
        return '{} {}'.format(self.fname,self.lname)
    
    @classmethod
    def change_raise_amount(cls,amount):
        cls.raise_percent = amount
    
    def raise_amount(self): 
        self.pay = self.pay*Employee.raise_percent
        return self.pay
    
    @classmethod
    def new_object(cls,str1):
        fname,lname,pay = str1.split("-")
        return Employee(fname,lname,pay)
    
    @staticmethod
    def is_weekend(My_day):
        if My_day == 6:
            return "Its a weeekend"
        else:
            return "Please work for world"
    

# emp1 = Employee("krishna","Mishra",20000)
# emp2 = Employee("Rjesh","Kkanna",30000)
# emp1.change_raise_amount(3.5)
# # print(emp1.full_name())
# print(emp1.raise_amount())
# # print(emp1.fname)
# # print(emp2.pay)
# # print(Employee.__dict__)
# print(Employee.Number_of_Employee)

# #creating objects using class methods
# New_emp1 = Employee.new_object("Harmanpreet-Paji-70000")
# print(New_emp1.fname)

# import datetime

# My_day = datetime.date(1900,4,3)
# print(Employee.is_weekend(My_day))
