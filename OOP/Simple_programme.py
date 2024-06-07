# class Student:
#     def __init__(self,name,id):
#         for i in range(0,len(name)):
#             print(f"Name={name[i]}")
#             print(f"ID={id[i]}")  
            
# name=["Anas","rion","Jamee","Abid","Mahin","Omaer"]
# id=[10,20,30,40,50,60]             
# s1=Student(name,id) 
  

# class Student:
#     #(pass) #if i want to empty the class i can use ( pass)
#     pass 

################################# 
# here we'll use the class and will create a object and manipulate data 
# variable=class_name()
# this is how we can create an object . After making a variable and giving the 
# the name of the class we can create the object 

# s1=Student()#non parametre
# print(s1) # object je create hoyeche ta dekhano holo.Ekhane memory er kothay object ta create hoyeche sheta dekhano hoyeche . 



# class Student:
#     def __init__(self): #This is constructor . Constructtor built in vabe self niye nibe . 
#         # Self ta ekta default.eta thakbei . 
#         print("a student object created ") 
# s1=Student()
# print(s1)
## What is self? 
#here you can question how this constructor has printed ! because of self 
# s1=student() ekhane ami kichu dicchinah . taw ei self er throuhg tei amr call hocche . 
## ** (Constructor ekta object er jonno ekbar i call hbe  .) 
# ejonnoi tader memory location same thakbe. 
 


# class Student:
#     def __init__(self,name,id): ## self use krtesi bar bar . because ei self ta dara bujhay je eta student jei class ta create krechi oi class er ekta property . 
#         self.name=name # Instance variable
#         self.id=id     #Instance variable          ## Self ta kind of ekta porichoy bohoon kre  
#         # print("a student object created ") 
# s1=Student("Nimmi",12,)
# s2=Student("raiyan",22) 
# print(s1)  
## DESIGN  class er kono property i amra object reference chara access krte parbonah . 
# print(s1.name)
# print(s2.name) 

#if you want to change something . like name or id , firstly you need to access the name of the class through the object variable .
#like ---
# print(s2.name) 
# s2.name="BoB" 
# print(s2.name)  ## This is how you can change anything 

## Instance (method) Variable

# class Student:
#     def __init__(self,name,id):
#         self.name=name 
#         self.id=id    
#     def details(self):
#         print(f"Name:{self.name},ID:{self.id}")
# s1=Student("Nimmi",12,)
# s2=Student("raiyan",22)
# s1.id=15
# s2.id=25
# s1.details() 
# s2.details()  



# class Student :
#     def __init__(self,id,dept,cgpa):
#         self.id=id 
#         self.dept=dept
#         self.cgpa=cgpa 


# class ContactName:
#     def __init__(self,Name,Phone_Num,Date_of_birth): 
#         self.Name=Name
#         self.Phone_Num=Phone_Num
#         self.Date_of_birth=Date_of_birth  
#     def show(self):
#         return f"{self.Name}'s Birthdate is {self.Date_of_birth}"
#     def __str__(self):
#          return f"{self.Name}'s Phone Number  is {self.Phone_Num}"
# Name1=ContactName("Anas","01616919119","20 March")
# Name2=ContactName("Abid","1234567890","25 March") 
# print(Name1.show()) 
# print(Name2.show())
# print(Name1) 
# print(Name2) 


#Multiple class : 
# class Point: 
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y 
#     def show(self):
#         print(f"({self.x},{self.y})")

# class Line:
#     def __init__(self,point1,point2):
#         self.Start= point1
#         self.End=point2 
#     def show(self):
#        print(f"Start :{self.Start.show()} " ,end="")  
#        print(f"End:{self.End.show()}",end="")  
# l = Line(Point(0,0),Point(4,5))
# l.show() 
 

## Shallow copy 



# class Picnic2024:
#     def __init__(self,name,number,id):
#         self.name=name
#         self.number=number
#         self.id=id 
#     def message(self):
#         # print(f"{self.name},{self.id} - How are you? Hope everything is going well. please Bring money for the DS-Picnic 2024 .")
#         a={"Name" : self.name,
#            "Id":self.id ,
#            "Number":self.number,
#            "Message":"Please bring money for the picnic"
#         } 
#         print(a)  
# Name=["Anas","Abid","rion","sayma"]
# num=["01616919119","01955064219","01727068620","01878694608"]
# Id=["0152330094","0152330095","0152330096","052330097"]
# for i in range(0,len(Name)):
#     for j in range(i,i+1):
#         for k in range(i,i+1):
#             Student=Picnic2024(Name[i],num[j],Id[k])
#             Student.message() 

        
# class Student:
#     def __init__(self):
#         self.firstname="Swakkhar" 
#         self.lastname="Shatabda"
#         self.age=20
#         self.address = "Dhaka" 
#         self.cgpa= 3.75 
#         self.weight= 71.2 
# Swakkhar=Student()
# print(f"{Swakkhar.firstname} {Swakkhar.lastname}")


## if .....!!!!!!!!!!! 
# class Student:
#     def __init__(self):
#         self.firstname="Swakkhar"
#         self.lastname="Shatabda" 
#         self.age=25 
#         self.address="Chittagong" 
#         self.weight= 82 
#         self.cgpa=4.00 
# Swakkhar=Student() 
# Farid=Student() 
# print(f"{Swakkhar.firstname} {Swakkhar.lastname}") 
# print(f"{Farid.firstname} {Farid.lastname}")  

### Here in both object 1st and last name is same . but its not correct . Thats why we need parametre . 
### If we use pararmetre we can easily solve this problem . 

# class Student:
#     def __init__(self,firstname,lastname,age,address,weight,cgpa):
#         self.firstname=firstname
#         self.lastname=lastname 
#         self.age=age 
#         self.address=address 
#         self.weight=weight 
#         self.cgpa=cgpa 
# Swakkhar=Student("Swakkhar","Satabda",25,"Dhaka",72,3.75) 
# Farid=Student("Dewan","Farid",52,"Chittagong",96,3.90) 
# print(f"{Swakkhar.firstname} {Swakkhar.lastname},{Swakkhar.age} {Swakkhar.address} {Swakkhar.cgpa} {Swakkhar.weight}")
# print(f"{Farid.firstname} {Farid.lastname} {Farid.age} {Farid.address} {Farid.weight} {Farid.cgpa}")


# Consider a game where we have multiple players. A player could be
# modeled by a Player class with instance variables for name, points,
# health, location, and so on. Each player would have the same
# capabilities, but the methods could work differently based on the
# different values in the instance variables.


# class Player:
#     def __init__(self,name,points,health,location):
#         self.name=name
#         self.points=points
#         self.health=health
#         self.location=location 
#     def capabilities(self):
#         print(f"{self.name} , {self.points} , {self.health} , {self.location}") 
# Player1=Player("Mushfiq",50,"Strong","Motijheel") 
# Player2=Player("Jamme",45,"Medium","Mohammadpur") 
# Player1.capabilities()
# Player2.capabilities() 


# Imagine an address book. We could create a Person class with
# instance variables for name, address, phoneNumber, and birthday. We
# could create as many objects from the Person class as we want, one
# for each person we know. The instance variables in each Person
# object would contain different values. We could then write code to
# search through all the Person objects and retrieve information about
# the one or ones we are looking for.

# from typing import Any


# class Person:
#     def __init__(self,name,address,phoneNumber,birthday):
#         self.name=name
#         self.address=address
#         self.phoneNumber=phoneNumber
#         self.birthday=birthday 
# Person1=Person("Anas","Dhaka","01616919119","20 March") 
# Person2=Person("Mahin","GAzipur","01955064219","25 April" )
# print(Person2.name) 
# print(Person2.address)
# print(Person1.phoneNumber)
# print(Person1.birthday) 


##  Python Crash course ,page158,chap9 

# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def sit(self):
#         print(f"{self.name} 
#               is sitting") ## Stimulate a dog sitting response to a command 
#     def roll_over(self):
#         print(f"{self.name} Rolled over ! ") 
         
# Dog1=Dog("tommy",5) 
# Dog2=Dog("jimmy",4) 
# print(Dog1.sit())
# print(Dog2.roll_over())


## Setting a default value for Attribute 

# class Car:
#     def __init__(self,make,model ,year):
#         self.make=make
#         self.model=model
#         self.year=year 
#         self.odometer_reading= 0 ## its a default value for this attribute 
#     def read_odometre(self):
#         print(f"This car has {self.odometer_reading} miles on it ") 
# my_new_car=Car("audi","a4",2024)
# my_new_car.read_odometre()  

## modifying an attributes value through a method 

# class Car:
#     def __init__(self,make,model ,year):
#         self.make=make
#         self.model=model
#         self.year=year 
#         self.odometer_reading= 0 ## its a default value for this attribute 
#     def read_odometre(self):
#         print(f"This car has {self.odometer_reading} miles on it at {self.year}") 
#     def update_odometre(self,mileage,num):
#         self.odometer_reading=mileage 
#         self.year=num 

# my_new_car=Car("audi","a4",2024)
# my_new_car.update_odometre(25,100)
# my_new_car.read_odometre()


# class Car:
#     def __init__(self,make,model ,year):
#         self.make=make
#         self.model=model
#         self.year=year 
#         self.odometer_reading= 20 ## its a default value for this attribute 
#     def read_odometre(self):
#         print(f"This car has {self.odometer_reading} miles on it at {self.year}") 
#     def update_odometre(self,mileage,num):
#         if mileage>=self.odometer_reading:
#             self.odometer_reading=mileage
#         else:
#             print("You cant roll back an odometre!")   

# my_new_car=Car("audi","a4",2024)
# my_new_car.update_odometre(12,100)
# my_new_car.read_odometre()


## Incrementing an Attributes Value Through a Methode 



# 1. Create a class named “Box” which has 3 attributes: length, width, height and a method
# named get_volume(). The get_volume() method will calculate the volume of the Box and return
# the value. Create 2 Box objects with different length, width, height, then call the get_volume()
# method and print the volumes.

# class Box:
#     def __init__(self,length,width,height):
#         self.length=length
#         self.width=width
#         self.height=height 
#     def get_volume(self): 
#         volume=(self.height*self.width*self.length) 
#         return volume 
# Box1=Box(20,30,40) 
# Box2=Box(40,50,60) 
# print(f"The volume is {Box1.get_volume()}") 
# print(f"The volume is {Box2.get_volume()}")

# 2. Create an Address Book application, where a user can create a new record, update record,
# delete record.

# class AddressBook:
#     def __init__(self):
#         self.Book={} 
#     def create_record(self,name,address):
#         self.Book[name]=address 
#     def update_record(self,name,new_address):
#         self.Book[name]=new_address 
#     def del_record(self,name):
#         del self.Book[name] 
# p1=AddressBook() 
# p1.create_record("Abu Anas","Dhaka") 
# p1.create_record("Mahi","Dhanmondi") 
# print(p1.Book)
# p1.update_record("Abu Anas","Khilgaon") 
# print(p1.Book) 
# p1.del_record("Mahi")  
# print(p1.Book) 

# 3. Create a Banking Application, where a user can create a new account, deposit money,
# withdraw money and check the balance. 
# class BankAccount:
#     def __init__(self):
#         self.__balance=0 
#     def new_account(self,name,id):
#         self.name=name 
#         self.id=id 
#     def deposit_money(self,deposit):
#         self.deposit=deposit 
#         self.__balance+=self.deposit 
#     def withdraw_money(self,withdraw):
#         self.withdraw=withdraw 
#         if (self.withdraw < self.deposit):
#             self.__balance-=self.withdraw 
#     def check_balance(self):
#         print(self.__balance)  
# account1=BankAccount() 
# account1.new_account("Anas",2004) 
# account1.deposit_money(5000) 
# account1.withdraw_money(2000) 
# account1.check_balance() 
 
## Tawsif sir CT  
# class Message :
#     def __init__(self,sender,recipient,content,timestamp):
#         self.sender=sender 
#         self.recipient=recipient 
#         self.content=content 
#         self.timestamp=timestamp
#         self.format={}
#     def display_message(self):
#         self.format["From"]=self.sender
#         self.format["To"]=self.recipient 
#         self.format["Content"]=self.content 
#         self.format["Sent at "]=self.timestamp 
#         return self.format 
#     def update(self,content,timestamp): 
#         self.format["Content"]=content
#         self.format["Sent at"]=timestamp 
#         return self.format
# Message1=Message("Alice","Bob","Hello how are you","8:46 pm, Friday")
# print(Message1.display_message()) 
# print(Message1.update("Hello Alice,how are you ?","Tuesday,15 february")) 



### BOOK P Crash course 
## 9.1 ,9.2 
# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_name):
#         self.restaurant_name=restaurant_name
#         self.cuisine_name=cuisine_name
#     def describe_restaurant(self): 
#         print("resturant is open now ") 
# Res=Restaurant("Chilox","Fast food") 
# Res.describe_restaurant() 
# print(Res.restaurant_name) 
# print(Res.cuisine_name)
# Res2=Restaurant("Yum Cha Ditrict","Thai") 
# Res3=Restaurant("Star Kabab ","Bangladeshi ") 
# Res2.describe_restaurant() 
# Res3.describe_restaurant() 


## 9.3 

# class User:
#     def __init__(self,first_name,last_name,id,number,age):
#         self.first_name=first_name
#         self.last_name=last_name 
#         self.id=id
#         self.number=number
#         self.age=age 
#     def describe_user (self):
#         print(f"{self.first_name} {self.last_name} is a great person who's {self.age} years old and his id number is  {self.id} . His number is  {self.number}") 
#     def greet_user(self):
#         print(f"{self.first_name} , Good Morning . Hope you're well. ") 
# user1=User("Abu","Anas","0152330094","01616919119",22) 
# user1.describe_user()
# user1.greet_user() 



# Create a bookstore application that will help a bookstore owner keep a record of its
# books, show all available books, sell books (should be able to sell multiple copies), and
# order new/existing books from publishers. You should implement two classes: one for
# each book and another for the bookshop. The Book class should contain all relevant
# information about the book like title, author, price, and quantity (you can add more
# attributes if you think it is relevant). The Bookshop class should contain a list of Book
# objects.

# (show all available books, sell books )**
# (order new/existing books from publishers)** 
# class BookInfo:
#     def __init__(self,title,author,price,quantity):
#         self.title =title
#         self.author = author
#         self.price = price
#         self.quantity =quantity 
#     def available_books(self):
#         print(f"{self.title} by {self.author}.") 
#     def 

# class Bookshop:
#     def __init__(self):
#         self.books=[] 
#     def add_books(self,books):
#         self.books.append(books) 
#     def sell_books(self,title,quantity):
#         for book in self.books:
#             if  




# class Song:
#     def __init__(self,title,artist,duration):
#         self.title=title
#         self.artist=artist
#         self.duration=duration 
#     def __str__(self):
#         return f"{self.title} , {self.artist}" 
# class Playlist:
#     def __init__(self,song_name):
#         self.song_list=[song_name] 
#     def add_song(self,song_name):
#         if song_name not in self.song_list:
#             self.song_list.append(song_name) 
#     def remove_song(self,song_name):
#         if song_name in self.song_list:
#             del song_name  
#     def display_songs(self):
#         for i in range(0, len(self.song_list)): 
#             print( self.song_list[i])   
#     def search_song(self,song_name):
#         if song_name in self.song_list:
#             print(f"yes,here is the {song_name}")
#         else:
#             print("The song isnt here .")
# song1=Song("Jadukor","pritom","5min")
# song2=Song("beni khule","habib","4min")
# song3=Song("oniket prantor","Artcell","15 min")    
# playlist1=Playlist("Jadukor")
# playlist2=Playlist("beni khule")  
# playlist3=Playlist("oniket prantor") 
# playlist1.add_song("chammak challo ")
# playlist1.display_songs()
# playlist1.search_song("oniket")  



class House:
    def __init__(self):
        self.window=4 ## If there's mention that ,intially window number is 4 
        self.door=2   ## If there's mention that ,intially Door number is 2 
    def view(self):
        if self.door>=2:
            print( f"{self.window} ,windows . {self.door}, Doors")  
        else:
            print("code kora lagbenah ,bashay jaw .") 
h1=House() 
h2=House() 
print(h1) # Here is the object location. you can consider this as a city name .Bascically ( self ) refers this location . self represents this
# memory location . this is the locationof 1st house. 
print(h2) # this is the locationof 2nd house . 
h1.view() 
h2.view() 
h1.window=4
h2.door=1 
h1.view()
h2.view() 
        
