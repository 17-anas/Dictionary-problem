# from tkinter import *
# myroot = Tk()
# myroot.mainloop()

##################

# from tkinter import *
# myroot = Tk()
# myroot.geometry("600x400")
# myroot.title("First GUI Application")
# myroot.resizable(width=False,height=True)
# myroot.mainloop()

##############################################

## Add A label 
# from tkinter import *
# root=Tk()

# root.geometry("600x400")
# root.title("This is ANAS zone") 

# label=Label(text="My First GUI Application",borderwidth=6,relief=SUNKEN)
# label.pack(padx=50,pady=50)  

# root.mainloop()

################################################

## Add two Buttons 
# from tkinter import*
# root=Tk()

# root.geometry("600x400")
# root.title("My first GUI application")

# label=Label(root,text="0")
# label.pack()

# b1= Button(root,text="Increase") 
# b1.pack()
# b2=Button(root,text="Decrease")
# b2.pack()

# root.mainloop()

## Here It will create e simle event handling 

## Object Oriented GUI 

# from tkinter import* 

# class MyApplication(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Event Handling") 

#         self.label1=Label(self,text="This is a label")
#         self.label1.pack()

#         self.B1=Button(self,text="Increase") 
#         self.B1.pack()

#         self.B2=Button(self,text="Decrease") 
#         self.B2.pack()
# my_app=MyApplication()
# my_app.geometry("600x400") 

# my_app.mainloop()



# from tkinter import *
# class MyApplication(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Event Handling")

#         self.label1 = Label(self,text="0")
#         self.label1.pack()

#         self.btn1 = Button(self,text="Increase")
#         self.btn1.pack()
#         self.btn2 = Button(self,text="Decrease")
#         self.btn2.pack()

#         def clicked1(event):
#             self.label1.config(text = int(self.label1['text'])+1)
#         def clicked2(event):
#             self.label1.config(text = int(self.label1['text'])-1)
            
#         self.btn1.bind('<Button-1>',clicked1)
#         self.btn2.bind('<Button-1>',clicked2)




# from tkinter import*
# class MyApplication(Tk):
#     def __init__(self):
#         super().__init__()

#         self.label1=Label(self,text="0") 
#         self.label1.pack() 

#         self.B1=Button(self,text="Subhanallah") 
#         self.B1.pack() 

#         self.B2=Button(self,text="Alhamdulillah")  
#         self.B2.pack()

#         self.B3=Button(self,text="Allahu Akbar")  
#         self.B3.pack()

#         self.B4=Button(self,text="Start Over")  
#         self.B4.pack()

#         def clicked1(event):
#             self.label1.config(text=int(self.label1["text"])+1)

#         def clicked2(event):
#             self.label1.config(text=int(self.label1["text"])+1)

#         def clicked3(event):
#             self.label1.config(text=int(self.label1["text"])+1)

#         def clicked4(event):
#             self.label1.config (text="0")

#         self.B1.bind("<Button-1>",clicked1)
#         self.B2.bind("<Button-1>",clicked2)
#         self.B3.bind("<Button-1>",clicked3)
#         self.B4.bind("<Button-1>",clicked4) 

# myApp = MyApplication()
# myApp.geometry('350x150')
# myApp.mainloop()


# from tkinter import *
# class MyApplication(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Event Handling")
#         self.label1 = Label(self,text="0")
#         self.label1.pack()
#         def clicked1():
#             self.label1.config(text = int(self.label1['text'])+1)
#         def clicked2():
#             self.label1.config(text = int(self.label1['text'])-1)

#         self.btn1 = Button(self,text="Increase",command=clicked1)
#         self.btn1.pack()
#         self.btn2 = Button(self,text="Decrease",command=clicked2)
#         self.btn2.pack()

# myApp = MyApplication()
# myApp.geometry('350x150')
# myApp.mainloop()


# from tkinter import *
# class MyApplication(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Event Handling")

#         self.label1 = Label(self,text="I am a Label 1",fg="red",bg = "teal")
#         self.label1.pack(fill=X,padx=10)

#         self.label2 = Label(self,text="I am a Label 2",font=("Times 12 italic",24,"bold"),fg="pink",bg = "cyan")
#         self.label2.pack(fill=X,pady=10)

#         self.label3 = Label(self,text="I am a Label 3",bg = "yellow")
#         self.label3.pack(fill=X)

# myApp = MyApplication()
# myApp.geometry("200x100")
# myApp.mainloop()


# from tkinter import *
# class MyApplication(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Event Handling")

#         self.label1 = Label(self,text="I am a Label 1",fg="red",bg = "teal")
#         self.label1.pack(side=TOP)

#         self.label2 = Label(self,text="I am a Label 2",
# font="Times 12 italic",bg = "cyan")
#         self.label2.pack(side=LEFT)

#         self.label3 = Label(self,text="I am a Label 3",bg = "yellow")
#         self.label3.pack(side=RIGHT)

# myApp = MyApplication()
# myApp.geometry("200x100")
# myApp.mainloop()4

# from tkinter import *
# class MyApplication(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Event Handling")

#         self.label1 = Label(self,text="I am a Label 1",fg="red",bg = "teal")
#         self.label1.place(x=1000,y=500,width=120,height=25)

#         self.label2 = Label(self,text="I am a Label 2",font="Times 12 italic",bg = "cyan")
#         self.label2.place(x=30,y=40,width=120,height=25)

#         self.label3 = Label(self,text="I am a Label 3",bg = "yellow")
#         self.label3.place(x=30,y=70,width=120,height=25)

# myApp = MyApplication()
# myApp.geometry("200x100")
# myApp.mainloop()


