"""
Program : Lambda function to return multiplication of two parameters
Input: 4   3    Output: 12
Input: 6   3    Output: 18
"""
def multiplication_program():
    multiply = lambda x, y: x * y
    return multiply

def main():
    try:
        multiply = multiplication_program()
        
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result1 = multiply(num1, num2)
        print(f"Input: {num1}   {num2}, Output: {result1}")
    
        num3 = int(input("\nEnter third number: "))
        num4 = int(input("Enter fourth number: "))
        result2 = multiply(num3, num4)
        print(f"Input: {num3}   {num4}, Output: {result2}")
        
    except ValueError:
        print("Error: Please enter valid integer numbers")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()