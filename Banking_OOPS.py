class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show_details(self):
        print("Personal Details\n")
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("Amount balance updated : ",self.balance)
    def withdraw(self,amount):
        self.amount = amount
        if(self.amount > self.balance):
            print("Insufficient Balance.")
        else:
            self.balance = self.balance - self.amount
            print("Current Balance: ", self.balance)
    def view_balance(self):
        self.show_details()
        print("Current Balance: ", self.balance)
        

Customer = Bank("Vatson",20,"Male")
Customer.show_details()
Customer.deposit(1000)
Customer.deposit(500)
Customer.withdraw(2000)
Customer.withdraw(600)
Customer.view_balance()