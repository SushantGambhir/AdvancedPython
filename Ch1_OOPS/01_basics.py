class MyClass:

    # Attributes (Class Variables)

    var1 = "Sushant"
    var2 = "Gambhir"

    # Methods (Functions inside a class)

    def func1(self):
        print("Hello World")

    def func2(self):
        print("Hello Globe")

# Objects of the class

obj1 = MyClass()
obj2 = MyClass()

# Accessing attributes and methods using objects

print(obj1.var1)  # Output: Sushant
print(obj2.var2)  # Output: Gambhir
obj1.func1()      # Output: Hello World
obj2.func2()      # Output: Hello Globe