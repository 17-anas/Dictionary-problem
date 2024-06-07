from tkinter import * 
anas_root=Tk()
anas_root.geometry("200x200")
anas_main_label=Label(text="This is Anas Newspaper " ,font=("Helvetica" ,32 , "bold") )
anas_main_label.pack()

anas_photo1=PhotoImage(file="1.png")
anas_photo2=PhotoImage(file="2.png")
anas_photo3=PhotoImage(file="3.png")
anas_photo4=PhotoImage(file="4.png")

f1=open("1.txt","r") 
f2=open("2.txt","r") 
f3=open("3.txt","r") 
f4=open("4.txt","r")

a=f1.readline()
b=f2.readline()
c=f3.readline()
d=f4.readline()
  
anas_label1=Label(text=a ,font=("Helvetica" ,22 , "bold") )
anas_label1_1=Label(image=anas_photo1)
anas_label1_1.pack()
anas_label1.pack()

anas_label2=Label(text=b ,font=("Helvetica" ,22 , "bold") )
anas_label2_1=Label(image=anas_photo2)
anas_label2_1.pack()
anas_label2.pack()

anas_root.mainloop() 