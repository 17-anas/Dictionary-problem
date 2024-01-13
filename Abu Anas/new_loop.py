# product = 3
# while product <= 50:
#     product = product * 3
# print(product) 


## Problem -- Average of grades of students  
# total_mark=0 
# total_students=0 
# marks=[87,90,92,93,99,85,86,88,82,87,86] 
# for i in marks:
#     total_mark+=i 
#     total_students+=1 
# average= total_mark//total_students 
# print(average) 

## Unique Marks 
# marks=[87,90,92,93,99,85,86,88,82,87,86,93,92]  
# unique_marks=[]
# duplicate_marks=[]
# for i in marks:
#     if i not in unique_marks:
#         unique_marks.append(i) 
#     else:
#         duplicate_marks.append(i) 
# print(duplicate_marks)
# print(unique_marks) 

# Write a program (WAP) that will print following series upto N th terms
# N=int(input()) 
# lst=[]
# for i in range (1,N+1):
#     lst.append(i) 
# print(*lst) 


# Write a program (WAP) that will print following series upto N th terms and the number would be odd . 
# N=int(input())
# num=N*2 
# lst=[]
# for i in range (1,num):
#     if i%2!=0:
#         lst.append(i)
# print(*lst) 

# Write a program (WAP) that will take two numbers X and Y as inputs. Then it will print the
# square of X and increment (if X<Y) or decrement (if X>Y) X by 1, until X reaches Y. If and
# when X is equal to Y, the program prints “Reached!”

# x=int(input()) 
# y=int(input()) 
# if x>y :
#     for i in range (x,y,-1):
#         print(i**2,end=",")
        
# elif x<y:
#     for j in range(x,y):
#         print(j**2,end=",")
#         if j not in range(x,y):
#             print("reached")
# elif x==y:
#     print("reached") 
# print("reached") 


x=int(input("Player 1 choice : ")) 
N=int(input("How many times you can guess ? ")) 
for i in range (N,0,-1):
    number=int(input("Player 2 choice : ")) 
    if x==number:
        print("Right! Player 2 wins")
        break
    elif x!=number:
        print(f"wrong!{i-1} choices left ")
        if i==1:
            print("Player 1 wins")
 



# Write a program (WAP) that will run and show keyboard inputs until the user types an ’A’
# at the keyboard.

# count=0
# while True:
#     given_input=input()
#     if given_input == "A":
#         break
#     else:
#         count+=1
#         print(f"input{count}  : {given_input}") 

# Write a program (WAP) that will reverse the digits of an input integer.

# number=list(input())
# for i in number:
#     print(*number[::-1],end="")
#     break   


