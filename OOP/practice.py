# print("Hello World")
# a=int(input("what is the value of a ? "))
# b=int(input("what is the value of b ?" )) 
# c=a+b 
# print(f"The summation is = {c}") 


# class Vector:
#     def __init__(self, i, j, k):
#         self.i = i
#         self.j = j
#         self.k = k

#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"

#     def __add__(self,other):
#         return Vector(self.i + other.i, self.j + other.j, self.k + other.k)



# v1 = Vector(2,5,7) 
# print(f"{v1.i}i + {v1.j}j + {v1.k}k")
# v2 = Vector(3,4,5)
# print(f"{v2.i}i + {v2.j}j + {v2.k}k")
# print("Sub:", end = " ")
# print(v1 + v2) 


# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     def __str__(self):
#         return f"{self.day}/{self.month}/{self.year}"

# class Period:
#     def __init__(self, start, end):
#         self.start = Date(start.day, start.month, start.year)  # Create a copy of start date
#         self.end = Date(end.day, end.month, end.year)          # Create a copy of end date

#     def __str__(self):
#         return f"{self.start}-{self.end}"

# d1 = Date(31, 1, 2024)
# d2 = Date(31, 5, 2024)
# p = Period(d1, d2)
# d1.year = 2025
# print(p)


# # Function to take multiple arguments
# def add(datatype, *args):
 
#     # if datatype is int
#     # initialize answer as 0
#     if datatype == 'int':
#         answer = 0
 
#     # if datatype is str
#     # initialize answer as ''
#     if datatype == 'str':
#         answer = ''
 
#     # Traverse through the arguments
#     for x in args:
 
#         # This will do addition if the
#         # arguments are int. Or concatenation
#         # if the arguments are str
#         answer = answer + x
 
#     print(answer)
 
 
# # Integer
# add('int', 5, 6)
 
# # String
# add('str', 'Hi ', 'Geeks')


# class Rectangle:
#     def __init__(self,w=0,h=0):
#         self.width=w
#         self.height=h
#     def asString(self):
#         return f"width: {self.width}, height: {self.height}"
# class ColoredRectangle(Rectangle):
#     def __init__(self,w=0,h=0,c=""):
#         super().__init__(w,h)
#         self.color=c
#     def asString(self):
#         return f"""width: {self.width}, height: {self.height},
# color: {self.color}"""
# c = ColoredRectangle(8,4,"blue")
# print(c.asString()) 

# class A:
#     def __init__(self,x=0):
#         self.__x=x
# class B(A):
#     def __init__(self,x):
#         super().__init__(x)
#     def change(self,n):
#             self._A__x=n
# b = B(15)
# b.change(25)
# print(b._A__x)

# class A:
#     counter = 0
#     def __init__(self,x=0):
#         self.x=x
#         A.counter = A.counter + 1
# class B(A):
#     def __init__(self,x=0,y=0):
#         self.y=y
#         super().__init__(x)
# b1=B()
# b2=B()
# b3=B()
# print(B.counter)
# print(A.counter)
# print(b1.counter)
# print(b2.counter)

# from abc import ABC,abstractclassmethod
# class Shape:
#     @abstractclassmethod
#     def area(self):
#         pass

# class rectangle(Shape):
#     def __init__(self,w,h):
#         self.h=h
#         self.w=w 

#     def area(self):
#         return self.w*self.h 
    
# r=rectangle(10,4) 
# print(r.area())


# from abc import ABC,abstractclassmethod
# class Shape:
#     @abstractclassmethod
#     def area(self):
#         pass 

# class Rectangular(Shape):
#     def __init__(self,h,w):
#         self.h=h
#         self.w=w 
    
#     def area(self):
#         return self.w* self.h 
    
# r= Rectangular(20,4)
# print(r.area())

# class Age:
#     def __init__(self,y=0,m=0):
#         self.year=y
#         self.month=m
#     def __repr__(self):
#         return f"{self.year} years {self.month}"
# a1 = Age(12,3)
# a2 = Age(5,3)
# a3 = Age(40,3)
# dictAges = {a1:"Eligible",a2:"Not Eligible",a3:"Eligible"}
# print(dictAges)
# print(dictAges[Age(12,3)])

        


# class A:
#     def __init__(self):
#         self.x=0
# class B:
#     def __init__(self):
#         self.y=0
# class C(A,B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         self.z=0
#     def __str__(self):
#         return f"{self.x} {self.y} {self.z}"
# c = C()
# print(c)


# class A:
#     def __init__(self, x=0):
#         self.x = x

# class B:
#     def __init__(self, y=0):
#         self.y = y

# class C(A, B):
#     def __init__(self, x=0, y=0, z=0):
#         A.__init__(self, x)  # Initialize x using A's initializer
#         B.__init__(self, y)  # Initialize y using B's initializer
#         self.z = z

#     def __str__(self):
#         return f"{self.x} {self.y} {self.z}"

# # Example usage
# c = C(10, 20, 30)
# print(c)  # Output: 10 20 30

# class A:
#     def greet(self):
#         print("Hello from class A")
# class B(A):
#     def greet(self):
#         print("Hello from class B")
# class C(A):
#     def greet(self):
#         print("Hello from class C")
# class D(C, B):
#     pass
# # Using the classes
# obj = D()
# obj.greet()


