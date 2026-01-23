"""
Program: Accept N numbers from user and return minimum number
Input: Number of elements : 4
Input Elements: 13   5   45   7
Output: 5
"""
def find_minimum(numbers_list):
    min_num = numbers_list[0]
    for num in numbers_list:
        if num < min_num:
            min_num = num
    return min_num
def main():
    try:
        n = int(input("Number of elements: "))
        # Get list elements from user
        numbers_list = []
        print(f"Enter {n} elements:")
        for i in range(n):
            num = int(input(f"Element {i + 1}: "))
            numbers_list.append(num)
        # Find minimum
        result = find_minimum(numbers_list)
        # Display output
        print(f"Output: {result}")
    except ValueError as ve:
        print(f"Error: Please enter valid integer numbers - {ve}")
    except TypeError as te:
        print(f"Error: Type error occurred - {te}")
    except IndexError:
        print("Error: List is empty, cannot find minimum")
    except KeyboardInterrupt:
        print("\nError: Program interrupted by user")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()