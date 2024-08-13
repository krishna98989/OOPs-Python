class Employee():

    raise_percent = 2.5 #class variable
    Number_of_Employee = 0
    def __init__(self,fname,lname,pay) -> None:
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def full_name(self):
        return '{} {}'.format(self.fname,self.lname)
    
    def raise_amount(self): 
        self.pay = self.pay*Employee.raise_percent
        return self.pay
    

class Devoloper(Employee):
    def __init__(self, fname, lname, pay, prog_lang):
        self.prog_lang = prog_lang
        super().__init__(fname, lname, pay) # ----->>> shortcut of not declaring individuals again

class Manager(Employee):
    def __init__(self, fname, lname, pay, Dev_List=None):
        super().__init__(fname, lname, pay)
        self.Dev_List = Dev_List
        if Dev_List == None:
            self.Dev_List = []
        else:
            Dev_List

    def add_dev(self,x):
        if x not in self.Dev_List:
            self.Dev_List.append(x)
        else:
            return "Can not add"

    def remove_dev(self,x):
        if x in self.Dev_List:
            self.Dev_List.remove(x)
        else:
            return "Can't remove"

    def print_man(self):
        for a in self.Dev_List:
            print(a.full_name())
            

# emp1 = Devoloper("krishna","Mishra",20000,"Python")
# emp2 = Devoloper("Rjesh","Kkanna",30000,"Sad-ke-java")

# man1 = Manager("Jemish","Kevadiya",30000, [emp1])
# # print(emp1.prog_lang )

# #print(help(Devoloper))

# man1.remove_dev(emp1)
# man1.add_dev(emp1)
# man1.print_man()
