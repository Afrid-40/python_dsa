##4-PILLARS OF OOPS
#
#access modifiers
class A:
    def __init__(self, name, age, gender):
        #constructor
        self.__name = name #private variable can be accessed inside of the same class which defines with __
        self.__age = age    #protected variable can be accessed inside of same class which defines with _ 
        self.__gender = gender  #public variable can be accessed inside of same class and outside of the class which defines with no prefix
    def display(self):
        print("Name:", self.__name)
        print("Age:", self.__age)
        print("Gender:", self.__gender)
    def get_name(self):
        return self.__name      
    def get_age(self):
        return self.__age   
    def get_gender(self):
        return self.__gender
    def set_name(self, name):   
        self.__name = name
    def set_age(self, age):
        self.__age = age                
    def set_gender(self, gender):
        self.__gender = gender
a1 = A("Sahil", 21, "Male")
a2= A("Afridi", 22, "Male")
print(a1.get_name())
print(a2.get_age())
print(a2.get_gender())

# Abstraction
from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, balance):
        self.__balance = balance  # private variable to store the account balance
    def deposit(self, amount):
        self.__balance += amount  # method to deposit money into the account
    def withdraw(self, amount):
        self.__balance -= amount  # method to withdraw money from the account
    def getBalance(self):
        return self.__balance  # method to get the current account balance
    @abstractmethod
    def interestcalc(self):
        pass

class SavingsAccount(BankAccount):
    def interestcalc(self):
        return self.getBalance() * 0.05  # method to calculate interest for savings account
    
    #Inheritance
class clan:
    print("this is a clan class")
class Dragon(clan):
    def sound(self):
        print("this is a dragon class")
class Luffy(Dragon):
    def sound(self):
        print("this is a luffy class")