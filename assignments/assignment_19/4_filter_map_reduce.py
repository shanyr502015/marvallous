"""
Program: Filter, Map, and Reduce operations
Filter: even numbers
Map: calculate square of each number
Reduce: sum of all numbers

Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204
"""

from functools import reduce
def filter_map_reduce_program(input_list):
    # Filter: even numbers
    filtered_list = list(filter(lambda x: x % 2 == 0, input_list))
    # Map: calculate square of each number
    mapped_list = list(map(lambda x: x ** 2, filtered_list))
    # Reduce: sum of all numbers
    reduced_result = reduce(lambda x, y: x + y, mapped_list)
    return filtered_list, mapped_list, reduced_result


def main():
    try:
        # Given input list
        input_list = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
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