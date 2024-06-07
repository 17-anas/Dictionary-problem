# from tkinter import * 
# anas_root=Tk() 

# ## for Width or height of the label 
# anas_root.geometry("500x500") #(width x height) 

# ## If you want to give a limit of the height or width and make a limitation of max and min size  
# # Here it takes the width and Height in a different way where we dont use small (X) instead of this we use comma(,).and quotetion deya jabenah 

# anas_root.minsize(100,200)
# anas_root.maxsize(1200,988) 

# ## LABEL- 
# Jamee=Label(text="Jamee is a good boy and this is his GUI") 
# Jamee.pack() # If you dont pack this it will not display. 

## GUI Logic 
# anas_root.mainloop()


# from tkinter import *
# myroot=Tk() 
# myroot.geometry('350x150')
# myroot.title("First GUI Applicatiion ") 
# myroot.mainloop()  

###################### How to add photo on GUI ################################ 
# from tkinter import * 
# anas_root=Tk()
# anas_root.geometry("500x500")
# anas_photo=PhotoImage(file="tiger.png")  
# anas_label=Label(image=anas_photo) 
# anas_label.pack()
# anas_root.mainloop()


###################### Label and Pack attributes ############################# 
# from tkinter import *
# root=Tk()
# root.geometry("400x400")
# root.title("My Gui") 
### Important label Options
# text = Adds the text 
# bd = Background 
# fg = Foreground 
# PadX = X Padding , 
# PadY = Y Padding 
# relief = Border Style -- The styles are ...
# 1. SUNKEN, 2. RAISED , 3. GROOVE , 4. RIDGE  
# Font Size --- 
# font=("Font name , font size, bold/italic") 

# anas_label=Label(text="Hello Let's Change The Label",bg="#ebd513",fg="#1337eb",padx=23,pady=44,font=("Helvetica" ,32 , "bold"),borderwidth=10, relief=GROOVE)   
# anas_label.pack(side=LEFT,anchor=NE,fill=Y,padx=50,pady=50)  
# pack attribute --- 
# side = top, bottom ,left, right 
# anchor = sw = south west  ,se = south east ,nw,ne
# fill = it'll fulfill the x axis or stretch on the direction of x or y 
# padx 
# pady  



# root.mainloop()