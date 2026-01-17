# map() Function:
    # Applies a function to every item in an iterable
    # Returns a map object (convert to list using list())
    # Syntax: map(function, iterable)

# filter() Function:
    # Filters items based on a condition (returns True/False)
    # Returns only items where the function returns True
    # Syntax: filter(function, iterable)

# reduce() Function:
    # Applies a function cumulatively to items from left to right
    # Reduces the iterable to a single value
    # Must import from functools module
    # Syntax: reduce(function, iterable)

# Important Notes:
    # map() and filter() return iterators, so wrap with list() to see results
    # reduce() requires from functools import reduce
    # Lambda functions work perfectly with these higher-order functions
    # These functions promote functional programming style