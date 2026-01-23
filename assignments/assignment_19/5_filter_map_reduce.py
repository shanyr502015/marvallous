"""
Program : Filter, Map, and Reduce operations
Filter: prime numbers
Map: multiply each number by 2
Reduce: maximum number

Input List = [2, 70, 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62
"""
from functools import reduce
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def multiply_by_two(x):
    return x * 2
def find_maximum(x, y):
    return x if x > y else y
def filter_map_reduce_program(input_list):
    # Filter: prime numbers
    filtered_list = list(filter(is_prime, input_list))
    # Map: multiply each number by 2
    mapped_list = list(map(multiply_by_two, filtered_list))
    # Reduce: find maximum number
    reduced_result = reduce(find_maximum, mapped_list)
    return filtered_list, mapped_list, reduced_result
def main():
    try:
        # Given input list
        input_list = [2, 70, 11, 10, 17, 23, 31, 77]
        # Call the filter_map_reduce function
        filtered_list, mapped_list, reduced_result = filter_map_reduce_program(input_list)
        # Display results
        print(f"List after filter = {filtered_list}")
        print(f"List after map = {mapped_list}")
        print(f"Output of reduce = {reduced_result}")
    except ValueError as ve:
        print(f"Error: Value error occurred - {ve}")
    except TypeError as te:
        print(f"Error: Type error occurred - {te}")
    except ZeroDivisionError:
        print("Error: Division by zero occurred")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()