# 🍽️ Restaurant Analogy
    # PRINT = Waiter announcing the dish (shows you, but you can't take it home)
    # RETURN = Takeaway box (gives you the food to use later)

    # 🔑 THE BIG DIFFERENCE
# ----------------------------------------------------------------------------------------
# | Feature               | PRINT                           | RETURN                     |
# |-----------------------|---------------------------------|----------------------------|
# | What it does          | Displays on screen              | Sends value back to caller |
# | Can you use it again? | ❌ NO (just shows, disappears) | ✅ YES (stores for reuse)  |
# | Where it works        | Anywhere in code                | Only inside functions      |
# | Analogy               | Waiter says "Here's pizza!"     | Waiter hands you pizza box |
# | Result                | You SEE it                      | You GET it                 |
# ----------------------------------------------------------------------------------------
# 🏬 Shopping at the Mall
# ❌ WINDOW SHOPPING (Print) - Just Looking
def window_shop_phone():
    phone = "📱 iPhone 15"
    price = 80000
    print(f"🪟 Wow! {phone} costs ₹{price}")
    print("😍 Looks amazing through the glass!")
    # No return = You don't buy it
my_phone = window_shop_phone()
print("What I bought:", my_phone)  # What I bought: None
# Can't use it at home!
# send_message = my_phone + " sending WhatsApp"  # TypeError!
# You just looked, didn't buy! 😢
print("\n" + "="*60 + "\n")

# ✅ ACTUAL PURCHASE (Return) - Really Buying
def buy_phone():
    phone = "📱 iPhone 15"
    price = 80000
    print(f"🛒 Buying {phone}") 
    print(f"💳 Paying ₹{price}") 
    return phone  # 🎁 Shopkeeper hands you the box!
my_phone = buy_phone()
print("What I bought:", my_phone)  # What I bought: 📱 iPhone 15
# ✅ Now you can use it!
print(f"📞 Calling from {my_phone}")
print(f"📸 Taking selfie with {my_phone}")
print(f"🎮 Playing games on {my_phone}")
# Can show to friends
friend = f"Friend jealous of my {my_phone}"
print(friend)
# Output:
# 🪟 Wow! 📱 iPhone 15 costs ₹80000
# 😍 Looks amazing through the glass!
# What I bought: None
# ===========================================================
# 🛒 Buying 📱 iPhone 15
# 💳 Paying ₹80000
# What I bought: 📱 iPhone 15
# 📞 Calling from 📱 iPhone 15
# 📸 Taking selfie with 📱 iPhone 15
# 🎮 Playing games on 📱 iPhone 15
# Friend jealous of my 📱 iPhone 15


# 📊 Quick Comparison Table
# ------------------------------------------------------------------------
# | Aspect      | PRINT (Window Shopping)  | RETURN (Actual Purchase)   |
# |-------------|--------------------------|----------------------------|
# | Action      | 🪟 Look through glass    | 🛒 Buy and take home      |
# | Result      | 👀 See it                | 🎁 Own it                 |
# | In your bag | ❌ Nothing (None)        | ✅ Product (actual value) |
# | Use later?  | ❌ Can't use             | ✅ Use anytime            |
# | Real life   | Window shopping at mall  | Buying and taking home     |
# ------------------------------------------------------------------------

## 💡 The ONE Line You Need to Remember:
#🎯 PRINT = Window Shopping 🪟, RETURN = Actual Purchase 🛍️
# Simple Translation:
    # - PRINT → You SEE it (but go home empty-handed) 👀
    # - RETURN → You GET it (take it home in your bag) 🎁

# ✅ Final Test
# Question: What's in my shopping bag?
def shop_A():
    print("👕 T-Shirt")  # Window shopping
def shop_B():
    return "👕 T-Shirt"  # Actual buying
bag_A = shop_A()  # What's in bag_A?
bag_B = shop_B()  # What's in bag_B?
print("Bag A:", bag_A)  # Bag A: None (empty! just looked)
print("Bag B:", bag_B)  # Bag B: 👕 T-Shirt (you bought it!)

# 🎬 Final Mantra: देखा है तो PRINT, लिया है तो RETURN!" ✨ If you just SAW it = PRINT, If you GOT it = RETURN!"

#############################`Difference between `return x`, `return x, y`, and `return`###############################
#######################################################################################################################
# The `return` statement is used to send a value from a function back to the caller.
# What you write after `return` decides **what type of value is returned.
# Python always returns one object, even when multiple values appear.

# `return x`
    # Returns one value (`x`).
    # Type of returned value is the type of `x`.
# `return x, y`
    # Returns multiple values as a tuple.
    # Internally, Python packs values into a tuple: `(x, y)`.
# `return`
    # Returns nothing explicitly.
    # Python returns `None` by default.
# If `return` is not written at all, Python also returns `None`.

# Example 1: return x
def square(n):
    return n * n
result = square(5)
print(result)
# Output: 25

# Example 2: return x, y
def calc(a, b):
    return a + b, a - b
result = calc(10, 5)
print(result)
# Output: (15, 5)

# Example 3: return (no value)
def show():
    print("Hello")
x = show()
print(x)
# Output:
# Hello
# None

# Direct Comparison 
    # `return x` → returns single value
    # `return x, y` → returns tuple of values
    # `return` → returns None

# Common Mistakes
    # ❌ Thinking `return x, y` returns two separate values (it returns a tuple).
    # ❌ Forgetting that a function without `return` gives `None`.
    # Interview line: “Python functions always return exactly one object.”

# Extra Recommended Methods
# Tuple unpacking – receive multiple returned values
a, b = calc(10, 5)
# Returning complex objects – list, dict, class objects
# Early return – exiting function based on condition