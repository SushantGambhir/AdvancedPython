### 🔒 What is Encapsulation?
- **Encapsulation** means **bundling data (attributes) and behavior (methods) together inside a class**.  
- It also means **restricting direct access** to some parts of an object, so the internal details are hidden and protected.  
- The idea: you expose only what’s necessary, and keep the rest private.

---

### 🧩 Why Encapsulation?
1. **Data protection** → Prevents accidental modification of important variables.  
2. **Controlled access** → You decide how the outside world interacts with your object.  
3. **Cleaner code** → Users of your class don’t need to know its internal complexity.  
4. **Flexibility** → You can change internal implementation later without breaking external code.

---

### ⚙️ Example in Python
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private attribute (note the __)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
```

Usage:
```python
account = BankAccount("Sushant", 1000)
account.deposit(500)
print(account.get_balance())  # 1500
```

- `__balance` is **hidden** (private). You can’t directly do `account.__balance`.  
- Instead, you use methods like `deposit()`, `withdraw()`, and `get_balance()` to interact safely.

---

### 🗝️ Key Concepts
- **Public members** → Accessible from outside the class (e.g., `owner`).  
- **Private members** → Hidden from outside, usually marked with `__` in Python.  
- **Getters/Setters** → Special methods to safely read or update private attributes.  

---

### 🔑 Analogy
Think of a **capsule medicine**:
- The capsule hides the powder inside (data).  
- You only interact with it by swallowing the capsule (methods).  
- You don’t need to know the exact chemical mix inside — just trust the controlled interface.

---

👉 Encapsulation is basically about **control and safety**: you decide what’s visible and what’s hidden.  