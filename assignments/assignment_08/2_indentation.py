# 1. Why is indentation mandatory in Python while it is optional in languages like C, C++ or Java?
# Python's Design Philosophy:
    # Python was designed with readability as a core principle. 
    # Guido van Rossum (Python's creator) wanted to enforce good coding practices at the language level rather than leaving them optional.

# C/C++/Java Use Braces: These languages use curly braces `{}` to define code blocks:
# C/Java/C++
if (condition) {
    statement1;
    statement2;
}
# The braces explicitly mark where blocks start and end, so indentation is just cosmetic (though strongly recommended for readability).

# Python Uses Indentation as Syntax:
# Python
# if condition:
#     statement1
#     statement2
# Python eliminates the braces and makes indentation the actual delimiter for code blocks. This means:
    # Less visual clutter (no braces needed)
    # Enforced readability (code that looks wrong IS wrong)
    # Fewer inconsistencies (can't have mismatched braces and indentation)
# The Philosophy: "There should be one—and preferably only one—obvious way to do it." By making indentation mandatory, Python ensures code structure is always visually clear and consistent.


# 2. What is an IndentationError? When does Python raise this error?
# Definition: An `IndentationError` is a syntax error raised when Python encounters incorrect or inconsistent indentation in your code.
# When Python Raises This Error:
# Case 1: Missing Indentation
if True:
print("Hello")  # IndentationError: expected an indented block
# Case 2: Unexpected Indentation
x = 5
    y = 10  # IndentationError: unexpected indent
# Case 3: Inconsistent Indentation (Mixing Tabs and Spaces)
def function():
    print("Line 1")  # 4 spaces
	print("Line 2")  # 1 tab - IndentationError: inconsistent use of tabs and spaces
# Case 4: Unindent Not Matching Any Outer Level
def function():
    if True:
        print("Hello")
      print("World")  # IndentationError: unindent does not match any outer indentation level
# Common Causes:
    # Forgetting to indent after `:` (colons)
    # Mixing tabs and spaces
    # Incorrect dedentation
    # Copy-pasting code with different indentation styles
# Best Practice: Use 4 spaces per indentation level (PEP 8 standard) and configure your editor to insert spaces when you press Tab.


# 3. How does Python internally identify the start and end of a code block using indentation?
# The Tokenization Process:When Python reads your code, it converts it into tokens. The indentation system uses two special tokens:
# 1. INDENT token: Marks the start of a new indented block
# 2. DEDENT token: Marks the end of an indented block
# Step-by-Step Process:
def greet():          # Line 1
    print("Hello")    # Line 2
    if True:          # Line 3
        print("Yes")  # Line 4
    print("Done")     # Line 5
print("End")          # Line 6

# What Python sees:
    # 1. Line 1: Colon `:` signals a block is coming
    # 2. Line 2: Indentation increases → INDENT token inserted → block starts
    # 3. Line 3: Same indentation level, still in first block
    # 4. Line 4: Indentation increases → INDENT token → nested block starts
    # 5. Line 5: Indentation decreases back to Line 2's level → DEDENT token → nested block ends
    # 6. Line 6: Indentation decreases to zero → DEDENT token → function block ends

# Indentation Stack: Python maintains a stack of indentation levels:
    # - Start: `[0]` (column 0)
    # - After Line 2: `[0, 4]` (0 and 4 spaces)
    # - After Line 4: `[0, 4, 8]` (0, 4, and 8 spaces)
    # - After Line 5: `[0, 4]` (pops 8)
    # - After Line 6: `[0]` (pops 4)

# Key Rules:
    # - Each increase in indentation = new block begins
    # - Each decrease in indentation = block(s) end
    # - Indentation must decrease to a level that exists in the stack (otherwise: IndentationError)
    # - Multiple DEDENT tokens can be inserted when indentation decreases multiple levels at once

# Why This Works: This system allows Python to understand code structure without needing explicit block terminators (like `}` or `end`), making the code cleaner while maintaining precise control flow definition.