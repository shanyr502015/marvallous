"""
Program 3: Filter, Map, and Reduce operations
Filter: numbers >= 70 and <= 90
Map: increase each number by 10
Reduce: product of all numbers

Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000
"""
from functools import reduce

def filter_map_reduce_program(input_list):
    filtered_list = list(filter(lambda x: 70 <= x <= 90, input_list))
    mapped_list = list(map(lambda x: x + 10, filtered_list))
    reduced_result = reduce(lambda x, y: x * y, mapped_list)
    return filtered_list, mapped_list, reduced_result

def main():
    try:
        input_list = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
        filtered_list, mapped_list, reduced_result = filter_map_reduce_program(input_list)
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