# Why are tuples faster than lists?
    # Tuples are immutable (cannot be changed)/(not growing/not shrinking).
    # Because they never change, Python does not need to manage extra memory for resizing (not growing/not shrinking).
    # so, Tuples have simpler internal structure: Less overhead → faster access & iteration.
# In short: No modification + fixed size = faster execution

# In which real-world scenarios would you prefer a tuple over a list? --> We prefer tuple when data should not change.
# Examples: Database records : user = ("Shantaram", 38, "Pune")