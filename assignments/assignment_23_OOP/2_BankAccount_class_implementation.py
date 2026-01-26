""" Write a Python program to implement a class named BankAccount with the following requirements:
• The class should contain two instance variables:
        o Name (Account holder name)
        o Amount (Account balance)
• The class should contain one class variable:
        o ROI (Rate of Interest), initialized to 10.5
• Define a constructor (__init__) that accepts Name and initial Amount.
• Implement the following instance methods:
        o Display() : displays account holder name and current balance
        o Deposit() : accepts an amount from the user and adds it to balance
        o Withdraw() : accepts an amount from the user and subtracts it from balance
          (Ensure withdrawal is allowed only if sufficient balance exists)
        o CalculateInterest() : calculates and returns interest using formula:
          Interest = (Amount * ROI) / 100
• Create multiple objects and demonstrate all methods. """

class BankAccount :
    ROI = 10.5

    def __init__(self,Name,Amount) :
        self.Name = Name
        self.Amount = Amount

    def Display(self) :
        print(f"Account Holder is : {self.Name} AND {self.Name} Balance is : {self.Amount}")

    def Deposit(self, amount):
        self.Amount += amount
        print(f"deposited : {amount}  --> BankAccount new balance : {self.Amount}")
        
    def Withdraw(self, amount):
        if amount <= self.Amount:
            self.Amount -= amount
            print(f"withdraw : {amount} --> BankAccount new balance : {self.Amount}")
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest
    
print("Class Variable ROI :", BankAccount.ROI)

acc1 = BankAccount("Rajesh",5000)
acc1.Display()
print("Instance Variable:",acc1.Name,acc1.Amount)

acc1.Deposit(2000)
acc1.Display()

acc1.Withdraw(1500)
acc1.Display()

Interest1 = acc1.CalculateInterest()
print(f"Interest calculated: {Interest1}")

acc1.Withdraw(10000)

print("-"*60)
acc2 = BankAccount("Shantaram",10000)
acc2.Display()
print(f"Instance variable:",acc2.Name, acc2.Amount)

acc2.Deposit(5000)
acc2.Display()

acc2.Withdraw(2000)
acc2.Display()

Interest2 = acc2.CalculateInterest()
print(f"Interest calculated: {Interest2}")
acc2.Withdraw(20000)