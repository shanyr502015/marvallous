# Range vs Slice - Ticket Counter Analogy

# 🎫 Ticket Counter Analogy
    # RANGE = Ticket Number Generator** (creates sequence of numbers)
    # SLICE = Scissors (cuts/extracts portion from existing data)


#🔑 KEY DIFFERENCE
# ----------------------------------------------------------------------------------------------
# | Feature | RANGE                                | SLICE                                     |
# |---------|--------------------------------------|-------------------------------------------|
# | Purpose | Generates new sequence of numbers    | Extracts portion from existing data       |
# | Returns | `range` object (sequence of numbers) | Same type as original (string/list/tuple) |
# | Usage   | Create numbers for loops, indexing   | Get subset of existing data               |
# | Analogy | Ticket machine printing 1,2,3,4,5... | Cutting a piece from existing ticket roll |
# ----------------------------------------------------------------------------------------------

## 1️⃣ STRING (Movie Name)
movie = "AVENGERS"
#        01234567

# RANGE - Generate ticket numbers (numbers only!)
tickets = range(0, 8)  # Generates: 0,1,2,3,4,5,6,7
print(list(tickets))   # [0, 1, 2, 3, 4, 5, 6, 7]

# Using RANGE to access string characters
for i in range(0, 5):
    print(movie[i], end=' ')  # A V E N G
print()

# SLICE - Extract portion of string (actual characters!)
portion = movie[0:5]
print(portion)         # 'AVENG' - actual text extracted
print(type(portion))   # <class 'str'>

# COMPARISON
print(range(2, 6))     # range(2, 6) - just a number generator
print(movie[2:6])      # 'ENGE' - actual extracted text

# Key Point:
    # range(0, 5)` → Creates numbers: 0,1,2,3,4
    # movie[0:5]` → Extracts text: 'AVENG'

# 2️⃣ LIST (Cinema Seats)
seats = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']
#         0     1     2     3     4     5     6

# RANGE - Generate position numbers
positions = range(0, 7)
print(list(positions))  # [0, 1, 2, 3, 4, 5, 6] - just numbers!

# Using RANGE to iterate and access
print("Using RANGE:")
for i in range(2, 5):
    print(seats[i], end=' ')  # A3 A4 A5
print()

# SLICE - Extract actual seats
print("Using SLICE:")
booked_seats = seats[2:5]
print(booked_seats)     # ['A3', 'A4', 'A5'] - actual seat names!
print(type(booked_seats))  # <class 'list'>

# COMPARISON
print(list(range(1, 4)))   # [1, 2, 3] - numbers
print(seats[1:4])          # ['A2', 'A3', 'A4'] - actual seats

# Key Point:
# `range(1, 4)` → Numbers: 1,2,3
# `seats[1:4]` → Seats: ['A2', 'A3', 'A4']

# 3️⃣ TUPLE (VIP Tickets)
vip_tickets = ('V1', 'V2', 'V3', 'V4', 'V5', 'V6')
#               0     1     2     3     4     5

# RANGE - Generate counter numbers
counters = range(0, 6)
print(list(counters))   # [0, 1, 2, 3, 4, 5] - counter numbers

# Using RANGE to loop through
print("Using RANGE:")
for i in range(1, 4):
    print(vip_tickets[i], end=' ')  # V2 V3 V4
print()

# SLICE - Extract VIP tickets
print("Using SLICE:")
selected_vip = vip_tickets[1:4]
print(selected_vip)     # ('V2', 'V3', 'V4') - actual tickets!
print(type(selected_vip))  # <class 'tuple'>

# COMPARISON
print(tuple(range(2, 5)))  # (2, 3, 4) - numbers only
print(vip_tickets[2:5])    # ('V3', 'V4', 'V5') - actual VIP tickets

# Key Point:
    # `range(2, 5)` → Numbers: 2,3,4
    # `vip_tickets[2:5]` → Tickets: ('V3', 'V4', 'V5')

#4️⃣ SET (Lucky Draw Numbers)

lucky_draw = {10, 20, 30, 40, 50, 60}

# RANGE - Generate sequential numbers
sequence = range(10, 61, 10)
print(list(sequence))   # [10, 20, 30, 40, 50, 60]
print(set(sequence))    # {10, 20, 30, 40, 50, 60} - creates set from range

# ❌ SLICE - NOT SUPPORTED on sets
# print(lucky_draw[0:3])  # TypeError! Sets are unordered

# Convert to list first for slicing
lucky_list = sorted(lucky_draw)  # [10, 20, 30, 40, 50, 60]
print(lucky_list[0:3])  # [10, 20, 30] - sliced from list

# COMPARISON
print(set(range(5, 10)))  # {5, 6, 7, 8, 9} - creates new set
# Sets don't support slicing directly

# Key Point:
    # `range()` can CREATE a set
    # Sets DON'T support slicing (use after converting to list)

# 5️⃣ DICTIONARY (Seat Bookings)

bookings = {
    'S1': 'John',
    'S2': 'Emma',
    'S3': 'Mike',
    'S4': 'Sara',
    'S5': 'Tom',
    'S6': 'Lisa'
}

# RANGE - Generate seat numbers to create/access dict
print("Using RANGE to create seats:")
for i in range(1, 4):
    seat_key = f'S{i}'
    print(f"{seat_key}: {bookings[seat_key]}")
# Output: S1: John, S2: Emma, S3: Mike

# Creating dict using RANGE
new_bookings = {f'B{i}': f'Person{i}' for i in range(1, 4)}
print(new_bookings)  # {'B1': 'Person1', 'B2': 'Person2', 'B3': 'Person3'}

# ❌ SLICE - NOT directly supported on dict
# print(bookings[0:3])  # TypeError!

# SLICE on dict keys/values after conversion
keys_list = list(bookings.keys())
print(keys_list[0:3])  # ['S1', 'S2', 'S3'] - sliced keys

values_list = list(bookings.values())
print(values_list[1:4])  # ['Emma', 'Mike', 'Sara'] - sliced values

# COMPARISON
seats_from_range = [f'S{i}' for i in range(1, 4)]
print(seats_from_range)  # ['S1', 'S2', 'S3'] - created using range

seats_from_slice = list(bookings.keys())[0:3]
print(seats_from_slice)  # ['S1', 'S2', 'S3'] - extracted using slice

# Key Point:
    # - `range()` helps CREATE dict keys
    # - Slicing needs conversion to list first


# 📊 Complete Comparison Table
# ----------------------------------------------------------------------------------------
# | Data Type | RANGE Usage                          | SLICE Usage                       |
# |-----------|--------------------------------------|-----------------------------------|
# | String    | `for i in range(0,5):` → loop        | `s[0:5]` → extract substring ✅  |
# | List      | `for i in range(len(l)):` → iterate  | `l[0:5]` → extract sublist ✅    |
# | Tuple     | `for i in range(len(t)):` → iterate  | `t[0:5]` → extract subtuple ✅   |
# | Set       | `set(range(1,10))` → create set      | ❌ Direct slice not supported    |
# | Dict      | `for i in range(1,5):` → create keys | ❌ Need list conversion first    |
# ---------------------------------------------------------------------------------------

# 🎯 Key Differences Summary
# ----------------------------------------------------------------------------------
# | Aspect       | RANGE                             | SLICE                        |
# |--------------|-----------------------------------|------------------------------|
# | Syntax       | `range(start, stop, step)`        | `[start:stop:step]`          |
# | Returns      | `range` object (numbers)          | Same type as original        |
# | Use Case     | Generate numbers, loops           | Extract data portions        |
# | Example      | `range(0, 5)` → 0,1,2,3,4         | `list[0:5]` → first 5 items  |
# | Standalone?  | ✅ Yes (creates its own sequence) | ❌ No (needs existing data) |
# ----------------------------------------------------------------------------------

#💡 Easy Memory Tricks
# 🎫 Ticket Counter Analogy:

# RANGE = 🎰 Number Dispenser Machine
    # Generates ticket numbers: 1, 2, 3, 4, 5...
    # `range(1, 6)` creates numbers 1,2,3,4,5

# SLICE = ✂️ Scissors
    # - Cuts portion from existing ticket roll
    # - `tickets[1:6]` extracts actual tickets from roll


# 🎬 Cinema Hall Example
# RANGE - Generate seat numbers (the counter machine)
print("Counter generates:")
for num in range(1, 8):
    print(f"Ticket #{num}", end=' ')
# Output: Ticket #1 Ticket #2 Ticket #3 ... Ticket #7

print("\n")

# SLICE - Cut portion from existing seats (the scissors)
all_seats = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']
print("Cut from existing:")
print(all_seats[1:4])  # ['A2', 'A3', 'A4']
print("Cut from existing:")
print(all_seats[4:7])  # ['A5', 'A6', 'A7']

# 🎭 Final Catchphrase:
# "RANGE banata hai (creates), SLICE kaatta hai (cuts)!" 🎬
    # Or in English:
    # - RANGE → Number Generator (makes new sequence)
    # - SLICE → Data Extractor (takes from existing)

# Think:
    # - RANGE = Factory producing numbers 🏭
    # - SLICE = Knife cutting a cake 🔪🍰