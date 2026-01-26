"""Write a Python program to implement a class named Numbers with the following specifications:
• The class should contain one instance variable: Value
• Define a constructor (__init__) that accepts a number from the user and initializes Value.
• Implement the following instance methods:
        o ChkPrime() : returns True if the number is prime, otherwise returns False
        o ChkPerfect() : returns True if the number is perfect, otherwise returns False
        o Factors() : displays all factors of the number
        o SumFactors() : returns the sum of all factors
          (You may use this method as a helper in ChkPerfect() if required)
• Create multiple objects and call all methods.
"""

class Numbers:
    def __init__(self, value):
        self.value = value

    def ChkPrime(self):
        if self.value <= 1:
            return False
        for i in range(2, int(self.value ** 0.5) + 1):
            if self.value % i == 0:
                return False
        return True
    
    def ChkPerfect(self):
        if self.value <= 1:
            return False
        sum_factors = self.SumFactors()
        if sum_factors == self.value:
            return True
        else:
            return False
        
    def Factors(self):
        print(f"factors of {self.value:} are : ", end=" ")
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        sum_val=0
        for i in range(1,self.value):
            if self.value % i == 0:
                sum_val += i
        return sum_val
    


obj1 = Numbers(11)
print("Instance variable:", obj1.value)

obj1.Factors()
sum1 = obj1.SumFactors()
print(f"sum of factors: {sum1}")

is_prime1 = obj1.ChkPrime()
print(f"Is {obj1.value} prime ? {is_prime1}")

is_perfect1 = obj1.ChkPerfect()
print(f"Is {obj1.value} perfect ? {is_perfect1}")