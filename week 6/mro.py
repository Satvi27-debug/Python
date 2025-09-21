class A:
    def show(self):
        print("Class A method")

class B(A):
    def show(self):
        print("Class B method")
        super().show()  # Calls the next class's show method in the MRO

class C(A):
    def show(self):
        print("Class C method")
        super().show()  # Calls the next class's show method in the MRO

class D(B, C):
    def show(self):
        print("Class D method")
        super().show()  # Calls the next class's show method in the MRO

# Creating an object of class D
d = D()
d.show()

# Printing Method Resolution Order
print("\nMethod Resolution Order:")
print(D.mro())