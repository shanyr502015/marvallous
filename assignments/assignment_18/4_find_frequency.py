"""
Program: Accept N numbers from user and return frequency of a specific number
Input: Number of elements : 11
Input Elements: 13   5   45   7   4   56   5   34   2   5   65
Element to search: 5
Output: 3
"""
def find_frequency(numbers_list, search_element):
    frequency = 0
    for num in numbers_list:
        if num == search_element:
            frequency += 1
    return frequency

def main():
    try:
        n = int(input("Number of elements: "))
        numbers_list = []
        print(f"Enter {n} elements:")
        for i in range(n):
            num = int(input(f"Element {i + 1}: "))
            numbers_list.append(num)
        
        # Get element to search
        search_element = int(input("Element to search: "))
        # Find frequency
        result = find_frequency(numbers_list, search_element)
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