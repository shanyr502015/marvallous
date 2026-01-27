# no access specifier in python but we can mimic
class demo:
    def __init__(self):
        self.no1 = 10           # public
        self._no2 = 20          # protected --> demo chi child can see
        self.__no3 = 30         # private   --> 100% abstraction (even child not know it)
obj = demo
######################################################################################################################################################
"""
I'll explain Python's access modifiers with a comprehensive example 
Access Modifiers in Python: Python doesn't have true access specifiers like Java/C++, but uses naming conventions to indicate intended access levels:
    1. Public (no underscore)
        - Accessible from anywhere
        - Convention: `variable_name`
    2. Protected (single underscore `_`)
        - Accessible within class and subclasses
        - Convention: `_variable_name`
        - Not enforced, just a signal to developers
    3. Private (double underscore `__`)
        - Name mangling makes it harder to access from outside
        - Convention: `__variable_name`
        - Python mangles it to `_ClassName__variable_name`
"""
class BankAccount:
    def __init__(self, account_holder, balance):
        # PUBLIC - Anyone can access
        self.account_holder = account_holder
        
        # PROTECTED - Should only be used by class and subclasses
        self._account_number = "ACC123456"
        
        # PRIVATE - Strong encapsulation (name mangling)
        self.__balance = balance
        self.__pin = 1234
    
    # Public method
    def get_balance(self):
        """Public interface to access private data"""
        return self.__balance
    
    # Public method to modify private data safely
    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                return f"Withdrawn {amount}. New balance: {self.__balance}"
            return "Insufficient funds"
        return "Invalid PIN"
    
    # Protected method
    def _generate_statement(self):
        """Internal method for generating statements"""
        return f"Statement for {self._account_number}"


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        # Can access PROTECTED member from parent
        print(f"Account: {self._account_number}")
        
        # Can access PROTECTED method from parent
        print(self._generate_statement())
        
        # CANNOT directly access PRIVATE member from parent
        # print(self.__balance)  # This will cause AttributeError
        
        # Must use public method instead
        current_balance = self.get_balance()
        interest = current_balance * self.interest_rate / 100
        return f"Interest earned: {interest}"


# DEMONSTRATION
print("=" * 50)
print("TESTING ACCESS MODIFIERS")
print("=" * 50)

# Create objects
account = BankAccount("John Doe", 10000)
savings = SavingsAccount("Jane Doe", 15000, 5)

print("\n1. PUBLIC ACCESS:")
print(f"Account holder: {account.account_holder}")  # ✓ Works

print("\n2. PROTECTED ACCESS:")
print(f"Account number: {account._account_number}")  # ✓ Works but not recommended
print(f"From child class: {savings._account_number}")  # ✓ Works

print("\n3. PRIVATE ACCESS:")
# print(account.__balance)  # ✗ AttributeError
print(f"Balance via public method: {account.get_balance()}")  # ✓ Correct way

print("\n4. NAME MANGLING (accessing private forcefully):")
print(f"Accessing private via mangling: {account._BankAccount__balance}")  # ✓ Works but BAD practice

print("\n5. CHILD CLASS ACCESSING PARENT:")
print(savings.add_interest())  # Can access protected, not private

print("\n6. SECURE OPERATIONS:")
print(account.withdraw(2000, 1234))  # ✓ Correct PIN
print(account.withdraw(2000, 9999))  # ✗ Wrong PIN

"""
Output:
==================================================
TESTING ACCESS MODIFIERS
==================================================

1. PUBLIC ACCESS:
Account holder: John Doe

2. PROTECTED ACCESS:
Account number: ACC123456
From child class: ACC123456

3. PRIVATE ACCESS:
Balance via public method: 10000

4. NAME MANGLING (accessing private forcefully):
Accessing private via mangling: 10000

5. CHILD CLASS ACCESSING PARENT:
Account: ACC123456
Statement for ACC123456
Interest earned: 750.0

6. SECURE OPERATIONS:
Withdrawn 2000. New balance: 8000
Invalid PIN


Key Interview Points to Mention:

| Access Type | Syntax       | Accessible From    | Use Case                |
|-------------|--------------|--------------------|-------------------------|
| Public      | `self.var`   | Everywhere         | API, general access     |
| Protected   | `self._var`  | Class + Subclasses | Internal implementation |
| Private     | `self.__var` | Only within class  | Sensitive data          |

Why This Design?
1. Encapsulation: Hide internal implementation
2. Security: Protect sensitive data (PIN, balance)
3. Maintainability: Change internals without breaking external code
4. Inheritance: Protected allows subclass access, private prevents it

Interview Bonus Point: Python's philosophy is 'We're all consenting adults' - it trusts developers to follow conventions rather than enforcing strict access control. 
The underscore is a signal, not a lock."
"""