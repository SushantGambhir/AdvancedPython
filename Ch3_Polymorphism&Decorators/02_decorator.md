Decorators in Python are a powerful feature that let you **modify or enhance the behavior of functions or classes without changing their actual code**. Think of them as wrappers that add extra functionality around existing functions.

---

## 🔑 What is a Decorator?
- A **decorator** is a function that takes another function (or class) as input, adds some behavior, and returns a new function.
- They are often used for **logging, authentication, timing, caching, or enforcing rules**.
- Syntax uses the `@` symbol placed above a function definition.

---

## 🧩 How They Work
1. Define a decorator function that accepts another function.
2. Inside, define a wrapper function that adds extra behavior.
3. Return the wrapper.
4. Apply the decorator using `@decorator_name`.

---

## ⚙️ Example 1: Basic Decorator
```python
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**
```
Before the function runs
Hello!
After the function runs
```

---

## ⚙️ Example 2: Decorator with Arguments
```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Sushant")
```

**Output:**
```
Hello, Sushant!
Hello, Sushant!
Hello, Sushant!
```

---

## ⚙️ Example 3: Built-in Decorators
Python has built-in decorators like:
- `@staticmethod`
- `@classmethod`
- `@property`

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area)  # 78.5
```

---

## 📌 Why Use Decorators?
- **Code reuse:** Apply the same logic to multiple functions.
- **Separation of concerns:** Keep core logic clean, move extra behavior outside.
- **Flexibility:** Add/remove functionality without touching the original function.

---

👉 In short, decorators are like **plug-ins for your functions**—you can attach extra behavior elegantly.  