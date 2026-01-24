"""
Program : Lambda function to return power of two
Input: 4    Output: 16
Input: 6    Output: 64
"""
def power_of_two():
    power_of_two = lambda x: x ** 2
    return power_of_two

def main():
    try:
        power_of_2 = power_of_two()
        
        num1 = int(input("Enter first number: "))
        result1 = power_of_2(num1)
        print(f"Input: {num1}, Output: {result1}")
        
        num2 = int(input("Enter second number: "))
        result2 = power_of_2(num2)
        print(f"Input: {num2}, Output: {result2}")
        
    except ValueError:
        print("Error: Please enter a valid integer number")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()