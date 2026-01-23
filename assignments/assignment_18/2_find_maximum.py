"""
Program: Accept N numbers from user and return maximum number
Input: Number of elements : 7
Input Elements: 13   5   45   7   4   56   34
Output: 56
"""
def find_maximum(numbers_list):
    max_num = numbers_list[0]
    for num in numbers_list:
        if num > max_num:
            max_num = num
    return max_num

def main():
    try:
        n = int(input("Number of elements: "))
        numbers_list = []
        for i in range(n):
            num = int(input(f"Element {i + 1}: "))
            numbers_list.append(num)
        
        # Find maximum
        result = find_maximum(numbers_list)
        # Display output
        print(f"Output: {result}")
    except ValueError as ve:
        print(f"Error: Please enter valid integer numbers - {ve}")
    except TypeError as te:
        print(f"Error: Type error occurred - {te}")
    except IndexError:
        print("Error: List is empty, cannot find maximum")
    except KeyboardInterrupt:
        print("\nError: Program interrupted by user")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()