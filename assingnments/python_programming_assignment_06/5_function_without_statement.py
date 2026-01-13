**Question:**
Can a Python function exist without any statements inside its body? If yes, how?

---

### **Topic Name:**

Empty Function Body in Python

---

### **Key Idea (2–4 lines):**

Yes, a Python function can exist without any executable statements.
In such cases, the `pass` keyword is used as a placeholder.
`pass` tells Python that the function body is intentionally empty.

---

### **Important Points (bullets):**

* Python does not allow an empty function body.
* `pass` is a **null statement** (does nothing).
* Used when function logic is not decided yet.
* Helps avoid `IndentationError`.
* Common in function stubs and future planning.

---

### **How Can a Function Exist Without Statements?**

* By using the `pass` keyword inside the function body.
* `pass` satisfies Python’s syntax rules.
* Function can be defined now and implemented later.

---

### **Code Examples:**

```python
# Example 1: Empty function using pass
def test():
    pass

print("Function defined successfully")

# Output:
# Function defined successfully
```

```python
# Example 2: pass used as placeholder
def calculate():
    pass   # logic will be added later

calculate()
```

---

### **What Happens Without `pass`?**

```python
def fun():
# No statement here

# Output:
# IndentationError: expected an indented block
```

---

### **Common Mistakes / Interview Points:**

* Forgetting `pass` causes `IndentationError`.
* Interview Q: “Why is pass needed?” → To define empty blocks.
* `pass` does nothing, but is syntactically required.

---

### **Micro Practice Questions:**

1. What error occurs if a function body is empty?
2. Write a function with no logic using `pass`.
3. Can `pass` be used inside loops or conditions?

---

### **Extra Recommended Methods / Topics (not in your original passage):**

* `pass` in `if`, `for`, `while`, `class`
* Difference between `pass` and `return`
* Using `...` (ellipsis) as placeholder (advanced)

---

If you want to continue, next good topic is:
👉 **Local vs Global variables (scope in functions)**
