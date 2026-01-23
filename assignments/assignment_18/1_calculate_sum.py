"""
Program 6: Accept N numbers from user and return sum of all elements
Input: Number of elements : 6
Input Elements: 13   5   45   7   4   56
Output: 130
"""
# def calculate_sum(numbers_list):
#     total_sum = sum(numbers_list)
#     return total_sum
# def main():
#     try:
#         # Get number of elements from user
#         n = int(input("Number of elements: "))
#         if n <= 0:
#             print("Error: Number of elements must be positive")
#             return
#         # Get list elements from user
#         numbers_list = []
#         print(f"Enter {n} elements:")
#         for i in range(n):
#             num = int(input(f"Element {i + 1}: "))
#             numbers_list.append(num)
#         # Calculate sum
#         result = calculate_sum(numbers_list)
#         # Display output
#         print(f"Output: {result}")
#     except ValueError as ve:
#         print(f"Error: Please enter valid integer numbers - {ve}")
#     except TypeError as te:
#         print(f"Error: Type error occurred - {te}")
#     except KeyboardInterrupt:
#         print("\nError: Program interrupted by user")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
# if __name__ == "__main__":
#     main()


############ using for loop #############

def calculate_sum(numbers_list):
    total_sum = 0
    for num in numbers_list:
        total_sum += num
    return total_sum

def main():
    try:
        n = int(input("Number of elements: "))
        if n <= 0:
            print("Error: Number of elements must be positive")
            return
        # Get list elements from user
        numbers_list = []
        for i in range(n):
            num = int(input(f"Element {i + 1}: "))
            numbers_list.append(num)

        # Calculate sum
        result = calculate_sum(numbers_list)
        # Display output
        print(f"Output: {result}")

    except ValueError as ve:
        print(f"Error: Please enter valid integer numbers - {ve}")
    except TypeError as te:
        print(f"Error: Type error occurred - {te}")
    except KeyboardInterrupt:
        print("\nError: Program interrupted by user")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()