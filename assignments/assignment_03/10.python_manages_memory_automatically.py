#  Explain how Python manages memory automatically.Why does the programmer not need to explicitly allocate or free memory?

# How Python manages memory automatically
    # Python has automatic memory manager.
    # When we create variable, Python automatically allocates memory for it.
    # When variable is no longer used, Python automatically frees memory.
    # Programmer does not need to manage memory manually.

x = 10    # Python allocates memory
x = None  # Python can free memory automatically

# Why programmer does not need to explicitly allocate or free memory
    # Python uses garbage collection to manage memory.
    # It tracks objects and their references.
    # When object has no references, Python automatically reclaims memory.
    # This reduces memory leaks and errors.

# Role of Garbage Collection
    # Python uses a system called Garbage Collection.
    # Garbage Collector:
        # Finds objects that are no longer needed
        # Frees their memory automatically
    # This happens in background.