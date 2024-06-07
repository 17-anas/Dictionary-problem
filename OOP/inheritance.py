# Attribute - What an object has are attributes 
#method- What an object does are methode 
## The quick brown fox jumps over the lazy dog 
# The quick brown fox jumps over the lazy dog
#  the quick brown fox jumps over the lazy dog 

# class Human :
#     def eat(self):
#         print("i can eat ") 
#     def work(self):
#         print("I can work") 
# class Male(Human): ## Here it is inheritance . we are inheriting Human Class. which is the base class here . 
#     pass 
# male1=Male() 
# male1.work() 
# male1.eat()
 

## Derived class can also have his own method and we can also use it 

# class Human :
#     def eat(self):
#         print("i can eat ") 
#     def work(self):
#         print("I can work") 
# class Male(Human):
#     def flirt(self):
#         print("i can flirt ") 
# male1=Male() 
# male1. eat() 
# male1.work() 
# male1.flirt()  ## Jekono 1 ta object male1 diyei .. both human class and both male class er 
                ## Method gula use korte partese 


# ## I Can also use the same method in a diiferent way in inherited class ..like ..
# class Human :
#     def eat(self):
#         print("i can eat ") 
#     def work(self):
#         print("I can work") 
# class Male(Human):
#     def work(self):
#         print("i can code") ## here the methode is same but the work is different . 
# # we can aslo use this method through one object 

# male1=Male() 
# male1.work() 
# Human1=Human()  
# Human1.work() 
## This is called overriding . here weve overriden work method. 


## If you want to have the work def as well as you want to add someething extra.. 
# It means i want o print ... (I can work) as well as i can code 

# class Human :
#     def eat(self):
#         print("i can eat ") 
#     def work(self):
#         print("I can work",end=" ") 
# class Male(Human):
#     def flirt(self):
#         print("i can flirt ") 
#     def work(self):
#         super().work() 
#         print("i can code")  ## Super function is bascically to give you 
#         ## the accecss to all the methoods and the attributes of parent class 
#         ## 
# male1=Male() 
# male1.flirt()
# male1.work()   



# class Human :
#     def __init__(self):
#         self.num_eyes=2
#         self.num_nose=1
#     def eat(self):
#         print("i can eat ") 
#     def work(self):
#         print("I can work",end=" ") 
# class Male(Human):
#     def __init__(self,name):
#         self.name=name  ## If you also want to add extra attribute in inherited class , i mean in the male class.
#     def flirt(self):
#         print("i can flirt ") 
#     def work(self):
#         super().work() 
#         print("i can code")  ## Super function is bascically to give you 
#         ## the accecss to all the methoods and the attributes of parent class 
#         ## 
# male1=Male("Anas") 
# # male1.flirt()
# # male1.work()
# print(male1.num_eyes) ## Though we haven't declared any attribute in male class , we can access the attribute through the male class .

# After run this you'll show this problem . because you've printed male1.num_eyes.but male object has only one attribute which is (name) 
#### AttributeError: 'Male' object has no attribute 'num_eyes'
## The reason behind this problem is ,, you've now created your own (init) constructor in male class
## the solution is ..........


# class Human :
#     def __init__(self):
#         self.num_eyes=2
#         self.num_nose=1
#     def eat(self):
#         print("i can eat ") 
#     def work(self):
#         print("I can work",end=" ") 
# class Male(Human):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name  
 
#     def work(self):
#         super().work() 
#         print("i can code")  
# male1=Male("Anas") 
# print(male1.num_eyes)  ## Now it will run 
# print(male1.num_nose) 

## another thing ....

# class Human :
#     def __init__(self,num_heart):  ## If you set any arguement in parent class ..
#         self.num_eyes=2
#         self.num_nose=1
#         self.num_heart=num_heart
#     def eat(self):
#         print("i can eat ") 
#     def work(self):
#         print("I can work",end=" ") 
# class Male(Human):
#     def __init__(self,name,heart): ## here you need to use an arguemnt to get access of the num_heart
#         super().__init__(heart)   ## you've to set the parametre here also . otherwise it'll show you an error.
#         self.name=name  
#     def work(self):
#         super().work() 
#         print("i can code")  
# male1=Male("Anas",1) 
# print(male1.num_eyes)  
# print(male1.num_nose)
# print(male1.name)
# print(male1.num_heart) 

## You can also do this....

# class Human :
#     def __init__(self,num_heart):  ## If you set any arguement in parent class ..
#         self.num_eyes=2
#         self.num_nose=1
#         self.num_heart=num_heart
#     def eat(self):
#         print("i can eat ") 
#     def work(self):
#         print("I can work",end=" ") 
# class Male(Human):
#     def __init__(self,name,heart):
#         self.name=name 
#         super().__init__(heart)   
#     def work(self):
#         super().work() 
#         print("i can code") 
#     def display(self):
#         print(f" Hi I am {self.name} and I have {self.num_heart} heart.") 
# male1=Male("Anas",1) 
# print(male1.num_eyes)  
# print(male1.num_nose)
# print(male1.name)
# male1.display()  

## Types of inheritance 
# 1. Single inheritance    3.Multilevl inheritance 
# 2. Multiple inheritance  4. Hierarchical inheritance
# 5. hybrid inheritance


# 2. Multiple inheritance -- From more than 1 parent class .. inherti in 1 child class 
 ##  There will be parent class more than 1 and only 1 child class will inherit from those classes..this is called muultiple inheritance 


# Multiple Inheritance 

# class Human:
#     def eat(self):
#         print("I can eat ") 

# class Male:
#     def flirt(self):
#         print("I can flirt ") 

# class Boy(Human,Male):
#     pass 
# Boy1=Boy() 
# Boy1.eat() 
# Boy1.flirt() 


## If you want to use the overriden method here.. 
# class Human:
#     def eat(self):
#         print("I can eat ") 
#     def work(self):
#         print("I can work") 

# class Male:
#     def flirt(self):
#         print("I can flirt ") 
#     def work(self):
#         print("I can code")  

# class Boy(Human,Male): ## Here the order of the class matters. order onujayi jei class ta 1st e boshbe shei class tar element i access krbe . 
#     ## jemon ekhane human class ta first e likha hoyeche tai ekhane Human class er work method ta kaj korbe . 

#     pass 
# Boy1=Boy() 
# Boy1.work() ## This method can only access in the work method of human class . 
 ## If you wnat to print the method of male class.... like .. ( I Can code ) .. then solution is....

# class Human:
#     def eat(self):
#         print("I can eat ") 
#     def work(self):
#         print("I can work") 

# class Male:
#     def flirt(self):
#         print("I can flirt ") 
#     def work(self):
#         print("I can code")  

# class Boy(Human,Male): 

#     pass 
# Boy1=Boy() 
# Male.work(Boy1) ## Ekta object darai male class er work method use hoye gelo  


## if you want to add method in  Boy class also ..
# class Human:
#     def eat(self):
#         print("I can eat ") 
#     def work(self):
#         print("I can work") 

# class Male:
#     def flirt(self):
#         print("I can flirt ") 
#     def work(self):
#         print("I can code")  

# class Boy(Human,Male): 
#     def sleep(self):
#         print("I can sleep") 
#     def work(self):
#         print("I can test")  
# Boy1=Boy() 
# Boy1.work() ## If you simply write this this will print (I can test). The work method from boy we can easily access
## Obviously Boy1 object can access all the methods but here it is the same method . in this case you need to do thisss .....

## there is a method name mro ..here we can see the srquence of the class .. we can see that 
## first it will find the Boy class , then Human then Male and then object
