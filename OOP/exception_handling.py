# try:
#     print("Helllo") 
# except:
#     print("world")  

## here it will only print hello because it'll first go on the try part . If try block does not work it'll go the except part . 


     
# def my_func(x):
#     if x==10:
#         return ("Kuch to rehem kar!! ")
#     else:
#         print("ye dukh kahe khatam nehi huta ?")  
# n=input() 
# a=my_func(n)
# print(a) 
    

# try:
#     print("World") 
#     print(5/0)
#     print("Anas")  
# except:
#     print("world")
# finally:
#     print("Never ending plan e anas in ") 


################ Multiple Exception ################# 
# file=open("anas.txt","r") 
# print(file.readlines()) 

# file=open("anas.txt","r") 
# print(file.readline()) 

# file=open("anas.txt","r") 
# print(file.read()) 

# Here is three types where you can open a file . 
# readlines = The elements of the file will turn into a list if you use readlines .
# read = It'll just read the lines 


## File not found Error ------

# try :
#     file=open("path.txt","r") 
#     print(file.readline()) 
# except FileNotFoundError:
#     file=open("anas.txt","r") 
#     print(file.readline())
       
# There can be three types of error... 
# 1. Zro Division Error 
# 2. File not Found Error 
# 3. Value Error 
 
# try:
#     x=int(input())
#     y=int(input()) 
#     print(x/y) 
#     file= open("anas.txt","w") 
#     file.writelines(str(x/y)) 
# # except:
# #     print("kajshush")  ## You cant use this here . 
# except ValueError :
#     print("Input type isn't integer ") 
# except ZeroDivisionError :
#     print("Cant devide by zero") 
# except FileNotFoundError:
#     print("file doesn't exists on the given path ") 
# except :
#     print("Hahhaha ")

## when you will give this error you cant take any normal except before this error


    
# Define a function named divide_numbers that takes two parameters: x and y.
# def divide_numbers(x, y):
#     try:
#         # Attempt to perform the division operation and store the result in the 'result' variable.
#         result = x / y
#         # Print the result of the division.
#         print("Result:", result)
#     except ZeroDivisionError:
#         # Handle the exception if a division by zero is attempted.
#         print("The division by zero operation is not allowed.")

# # Usage
# # Define the numerator and denominator values.
# numerator = int(input())
# denominator = int(input())
# # Call the divide_numbers function with the provided numerator and denominator.
# divide_numbers(numerator, denominator)





# def divide_numbers(a, b):
#     try:
#         result = a / b
#         return result
#     except ZeroDivisionError :
#         print("Error occurred")
    

# # Example usage
# try:
#     result = divide_numbers(10, 0)
#     print("Result of division:", result)
# except:
#     print("An error occurred during division.")




# try:
#     my_list = [1, 2, 3]
#     print(my_list[5])
# except IndexError :
#     print("Error")


# try:
#     my_dict = {"key1": 1, "key2": 2}
#     print(my_dict["nonexistent_key"])
# except KeyError:
#     print("Error")
   
###################### For out put trace ################
# import traceback

# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         raise ValueError("Cannot divide by zero")

# try:
#     result = divide(10, 0)
# except ValueError as e:
#     print("Error occurred:", e)
#     traceback.print_exc()


# import traceback

# try:
#     my_list = [1, 2, 3]
#     print(my_list[5])
# except (IndexError, KeyError) as e:
#     print("Error occurred:", e)
#     traceback.print_exc()


# import traceback

# class CustomError(Exception):
#     def __init__(self, message):
#         self.message = message

# try:
#     raise CustomError("This is a custom error")
# except CustomError as e:
#     print("Error:", e.message)
#     traceback.print_exc()


# import traceback

# try:
#     assert False, "Assertion failed"
# except AssertionError as e:
#     print("Error:", e)
#     traceback.print_exc()


def try_it(value):
    try:
        x = int(value)
    except ValueError:
        print(f'{value} could not be converted to an integer')
    else:
        print(f'int({value}) is {x} ')
    
try_it(1.5)
