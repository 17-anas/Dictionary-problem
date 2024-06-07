# Exercise 1:
# Complex Number Arithmetic Implement a class representing complex numbers.Overload the necessary operators (+, -, *, /) to perform arithmetic operations 
# with complex numbers.

# Exercise 2: Matrix Addition
# Create a Matrix class that supports addition of two matrices using the + operator.
# Implement the necessary methods to support this operation.

# Exercise 3: Fraction Arithmetic
# Write a Fraction class that represents fractions (e.g., 1/2, 3/4).
# Overload the operators (+, -, *, /) to perform arithmetic operations with fractions. 

# Exercise 4: Custom String Concatenation
# Design a class that represents strings with custom rules for concatenation.
# Overload the + operator to implement concatenation based on your custom rules.

# Exercise 5: Vector Subtraction
# Extend the Vector class from the previous exercise to support subtraction of two vectors using the - operator.

# Exercise 6: Custom Comparison
# Create a class representing a custom data type (e.g., a Date class or a Point class). Implement methods to compare instances of this class using operators like ==, <, <=, >, >=, etc.

# Exercise 7: Custom Container
# Design a custom container class (e.g., a Set or a Bag) and overload the necessary operators to support operations like union, intersection, difference, etc.

# Exercise 8: Polynomial Arithmetic
# Write a Polynomial class representing polynomials with coefficients. Overload the arithmetic operators to perform addition, subtraction, multiplication, and division of polynomials.

# Exercise 9: Custom Iterator
# Create a class that implements a custom iterator. Overload the necessary operators to iterate through the elements of the class using familiar constructs like for loops.

# Exercise 10: Custom Data Structure
# Design a custom data structure (e.g., a linked list, a tree, or a graph). Overload operators to perform operations specific to your data structure (e.g., traversal, insertion, deletion).


# [Operator overloading is a feature in many programming languages that allows the same operator to have different implementations depending on the types of its operands. 
# In other words, you can redefine how operators behave when they are used with custom data types. This can make your code more expressive and easier to read.
# For example, in Python, the + operator is normally used to add numbers together, but you can also use it to concatenate strings]

# # Adding numbers
# result = 3 + 5  # result is 8

# # Concatenating strings
# result = "Hello, " + "world!"  # result is "Hello, world!" 

# In this example, + is overloaded to perform addition with numbers and concatenation with strings.

# Here's a simple exercise to practice operator overloading in Python:

# Exercise: Vector Addition
# Implement a Vector class that supports addition of two vectors using the + operator.

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         """Overload the addition operator to add two vectors."""
#         return Vector(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         """Return a string representation of the vector."""
#         return f"({self.x}, {self.y})"

# # Test the Vector class
# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# print("Vector 1:", v1)
# print("Vector 2:", v2)

# # Add two vectors
# result = v1 + v2
# print("Result of addition:", result)

# In this exercise, we define a Vector class that represents a two-dimensional vector with x and y components. We overload the + operator using the __add__ method to perform vector addition.
# When we add two Vector objects together (v1 + v2), it returns a new Vector object with the sum of their respective components.
# Feel free to extend this exercise by implementing other arithmetic operations (subtraction, multiplication, etc.) or by working with different types of operands.


# Exercise 1:
# Complex Number Arithmetic Implement a class representing complex numbers.Overload the necessary operators (+, -, *, /) to perform arithmetic operations 
# with complex numbers.

# class ComplexNumbers:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y 
#         self.z=z 

#     def __add__(self,other):
#         return (self.x+other.x,self.y+other.y,self.z+other.z)

#     def __sub__(self,other):
#         return (self.x-other.x,self.y-other.y,self.z-other.z)

#     def __mul__(self,other):
#         return (self.x*other.x,self.y*other.y,self.z*other.z)

#     def __truediv__(self,other):
#         return (self.x/other.x,self.y/other.y,self.z/other.z) 
    
# cn1=ComplexNumbers(10,20,40) 
# cn2=ComplexNumbers(5,10,20)
# print(cn1+cn2)
# print(cn1-cn2)
# print(cn1*cn2)
# print(cn1/cn2) 


# Exercise 2: Matrix Addition
# Create a Matrix class that supports addition of two matrices using the + operator.
# Implement the necessary methods to support this operation.


# class Matrix:
#     def __init__(self, matrix):
#         self.matrix = matrix

#     def __add__(self, other):
#         if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
#             raise ValueError("Matrices must have the same dimensions for addition.")
        
#         result = []
#         for i in range(len(self.matrix)):
#             row = []
#             for j in range(len(self.matrix[0])):
#                 row.append(self.matrix[i][j] + other.matrix[i][j])
#             result.append(row)
#         return Matrix(result)

#     def __str__(self):
#         return '\n'.join([' '.join([str(item) for item in row]) for row in self.matrix])

# # Example usage:
# matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
# matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])

# result_matrix = matrix1 + matrix2
# print("Matrix 1:")
# print(matrix1)
# print("\nMatrix 2:")
# print(matrix2)
# print("\nResult of addition:")
# print(result_matrix)


class Vector:
    def init(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def str(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def add(self,other):
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)



v1 = Vector(1,2,3)
print(f"{v1.i}i + {v1.j}j + {v1.k}k")
v2 = Vector(3,4,5)
print(f"{v2.i}i + {v2.j}j + {v2.k}k")
print("Sub:", end = " ")
print(v1 + v2)