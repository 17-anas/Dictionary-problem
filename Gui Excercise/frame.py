from tkinter import * 
root=Tk() 
root.geometry("500x500")
f1= Frame(root,bg="Grey",borderwidth=6,relief=SUNKEN) 
f1.pack(side=LEFT,fill="y")
l=Label(f1,text="This is My project")
l.pack(pady=140) 
f2=Frame(root,bg="Blue",borderwidth=6,relief=SUNKEN) 
f2.pack(side=TOP,fill="x") 
l2=Label(f2,text="Welcome to my Gui ",font=("Fraktur Bold", 20 )) 
l2.pack()    
root.mainloop()