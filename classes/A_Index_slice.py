# Index vs Slice in Python 

# 1. INDEX (Single Element Access)
    # Syntax: `collection[index]`
        # - Returns a single element
        # - Uses a single number inside square brackets []
        # - Index can be positive (0, 1, 2...) or negative (-1, -2, -3...)

## 2. SLICE (Multiple Elements Access)
    # Syntax: `collection[start:stop:step]`
        # - Returns a range of elements
        # - Uses colon (:) notation
        # - Creates a new object of the same type
        # - `start`: Starting index (inclusive)
        # - `stop`: Ending index (exclusive)
        # - `step`: Interval between elements (optional)


# Index vs Slice in Python - With explain tcinema hall analogy 
#🎬 Cinema Hall Analogy
    # INDEX = Getting a specific seat (one seat number)
    # SLICE = Booking a range of seats (from seat X to seat Y)

# 1. STRING (Movie Title)
# SYNTAX
    # Index: `string[position]` → Returns single character
    # Slice: `string[start:stop:step]` → Returns substring

movie = "AVENGERS"
#        01234567  (index positions)

# INDEX - Get one character (one seat)
print(movie[0])      # 'A' - First seat
print(movie[3])      # 'N' - 4th seat
print(movie[-1])     # 'S' - Last seat

# SLICE - Get multiple characters (range of seats)
print(movie[0:3])    # 'AVE' - Seats 0 to 2 (3 excluded)
print(movie[2:6])    # 'ENGE' - Seats 2 to 5
print(movie[:4])     # 'AVEN' - From start to seat 3
print(movie[4:])     # 'GERS' - From seat 4 to end
print(movie[::2])    # 'AEGS' - Every alternate seat
print(movie[::-1])   # 'SREGNEVA' - Reverse all seats


# 2. LIST (Seat Row A)
# SYNTAX
    # Index: `list[position]` → Returns single element
    # Slice: `list[start:stop:step]` → Returns new list

row_A = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']
#         0     1     2     3     4     5     6

# INDEX - Get one seat
print(row_A[0])      # 'A1' - First seat
print(row_A[3])      # 'A4' - 4th seat
print(row_A[-1])     # 'A7' - Last seat

# SLICE - Get range of seats
print(row_A[0:3])    # ['A1', 'A2', 'A3'] - First 3 seats
print(row_A[2:5])    # ['A3', 'A4', 'A5'] - Middle seats
print(row_A[:4])     # ['A1', 'A2', 'A3', 'A4'] - From start
print(row_A[4:])     # ['A5', 'A6', 'A7'] - Till end
print(row_A[::2])    # ['A1', 'A3', 'A5', 'A7'] - Alternate seats
print(row_A[::-1])   # ['A7', 'A6', 'A5', 'A4', 'A3', 'A2', 'A1'] - Reverse



#3. TUPLE (VIP Row - Immutable)
# SYNTAX
    # Index: `tuple[position]` → Returns single element
    # Slice: `tuple[start:stop:step]` → Returns new tuple
vip_row = ('V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7')
#           0     1     2     3     4     5     6
# INDEX - Get one VIP seat
print(vip_row[0])      # 'V1' - First VIP seat
print(vip_row[3])      # 'V4' - 4th VIP seat
print(vip_row[-1])     # 'V7' - Last VIP seat

# SLICE - Get range of VIP seats
print(vip_row[0:3])    # ('V1', 'V2', 'V3') - First 3 VIP
print(vip_row[2:5])    # ('V3', 'V4', 'V5') - Middle VIP
print(vip_row[:4])     # ('V1', 'V2', 'V3', 'V4') - From start
print(vip_row[4:])     # ('V5', 'V6', 'V7') - Till end
print(vip_row[::2])    # ('V1', 'V3', 'V5', 'V7') - Alternate
print(vip_row[::-1])   # ('V7', 'V6', 'V5', 'V4', 'V3', 'V2', 'V1')


# 4. SET (Available Seats - Unordered)
available = {'S1', 'S3', 'S5', 'S7', 'S9'}

# ❌ INDEX - NOT SUPPORTED (no specific position in unordered seats)
# print(available[0])  # TypeError!

# ❌ SLICE - NOT SUPPORTED
# print(available[0:3])  # TypeError!

# ✅ Only way to access: Convert to list first
available_list = list(available)
print(available_list[0])     # First element (unpredictable order)
print(available_list[0:3])   # First 3 elements (unpredictable order)

# Note: Sets are unordered - like a lottery bucket where seats have no fixed position!

# 5. DICTIONARY (Seat Bookings)
# SYNTAX
    # Index: `dict[key]` → Returns value for that key   
    # Slice: Not directly supported, convert to list first

bookings = {
    'B1': 'John',
    'B2': 'Emma', 
    'B3': 'Mike',
    'B4': 'Sara',
    'B5': 'Tom'
}

# INDEX - Access by KEY (seat number), not position
print(bookings['B1'])    # 'John' - Who's in B1?
print(bookings['B3'])    # 'Mike' - Who's in B3?
# print(bookings[0])     # ❌ KeyError! (no numeric index)

# SLICE - Works on keys(), values(), items() after conversion
keys_list = list(bookings.keys())
print(keys_list[0:3])    # ['B1', 'B2', 'B3'] - First 3 seat numbers

values_list = list(bookings.values())
print(values_list[1:4])  # ['Emma', 'Mike', 'Sara'] - 3 customers

items_list = list(bookings.items())
print(items_list[0:2])   # [('B1', 'John'), ('B2', 'Emma')]



## 📊 Quick Comparison Table
# ---------------------------------------------------------------------------------
# | Data Type | Index Support  | Slice Support          | Cinema Analogy          |
# |-----------|----------------|------------------------|-------------------------|
# | String    | ✅ `s[3]`      | ✅ `s[1:5]`           | Movie title letters     |
# | List      | ✅ `l[3]`      | ✅ `l[1:5]`           | Regular row seats       |
# | Tuple     | ✅ `t[3]`      | ✅ `t[1:5]`           | VIP row (can't change)  |
# | Set       | ❌ Unordered   | ❌ Unordered          | Lottery bucket          |
# | Dict      | ✅ `d[key]`    | ❌ (needs conversion) | Seat → Customer mapping |
# ---------------------------------------------------------------------------------

## 🎯 Key Differences
# ------------------------------------------------------------------
# | Feature      | INDEX                  | SLICE                  |
# |--------------|------------------------|------------------------|
# | Returns      | Single element         | Multiple elements      |
# | Syntax       | `[position]`           | `[start:stop:step]`    |
# | Result Type  | Original element type  | Same container type    |
# | Cinema Hall  | One specific seat      | Range of seats         |
# | Example      | `movie[3]` → `'N'`     | `movie[2:5]` → `'ENG'` |
# ------------------------------------------------------------------

#💡 Memory Tips
    # INDEX = 📍 Point to ONE thing (like a finger pointing to one seat)
    # SLICE = ✂️ Cut a PORTION (like cutting a pizza slice - you get multiple pieces)

# Remember: 
# Index gives you one item
# Slice gives you a new collection of items!

#########################🎬 Cinema Hall - Index vs Slice Summary################################
#################################################################################################
# Key Takeaways
    # 1. INDEX = Single seat using `[number]` → `row_A[0]` = "A1"
    # 2. SLICE = Multiple seats using `[start:stop:step]` → `row_A[0:3]`
    # 3. Negative indexing works backward → `row_A[-1]` = last seat
    # 4. Sets: No indexing/slicing (like lottery - seats have no fixed position)
    # 5. Dicts: Index by key (seat number), not position number

# Remember:
    # Index = Book ONE seat in the cinema hall 🎟️
    # Slice = Book MULTIPLE seats in a row 🎟️🎟️🎟️

# 🎭 Cinema Style Catchphrase:
# Index ek seat, Slice poori row! 🎬
# Or in English:
    # Index → "I want seat A5" (one specific seat)
    # Slice → "I want seats A3 to A7" (range of seats)

#📍 Visual Memory Aid
# Cinema Hall Row:
# [A1] [A2] [A3] [A4] [A5] [A6] [A7]
#   0    1    2    3    4    5    6
    # Index → 👉 [A3]  (pointing to one seat)
    # Slice → 👈 [A2] [A3] [A4] 👉 (selecting range)

# Think of it like:
    # INDEX = Laser pointer 🔴 (points to ONE seat)
    # SLICE = Rope barrier 🪢 (blocks off MULTIPLE seats)