# from tkinter import *
# root = Tk()
# root.geometry("300x300")
# root.resizable(0,0)
# msg= Entry(bg="#ffffff")
# msg.pack()

# def login():
#     print("hello world !")
#     l=Label(text=msg.get())
#     l.pack()

# btn = Button(text="Login",command=login)
# btn.pack()

# mainloop()


# from tkinter import *
# root = Tk()
# root.geometry("300x300")

# username = Entry(bg="#ffffff")
# username.pack()
    
# password = Entry(bg="#ffffff")
# password.pack()

# def login(): 
#     if username.get()=="nosin" and password.get()=="123":
#         l.config(text="success")
#     else:
#         l.config(text="failed")

# l=Label(text="")
# l.pack()

# Button(text="Login", command=login).pack()
# mainloop()

# value input in tkinter--(entry-- gets multipleline input), (text-- index starts from 1.0-- 1 defines no of line, .0 defines cursor position)
# from tkinter import *
# root = Tk()
# root.geometry("300x300")

# def click():
#     text1="Address"+mytext.get('1.0',END)
#     lbl.config(text=str(text1))

# mytext = Text(root, font=20, width=20, height=10)
# mytext.place(x=0,y=50)

# btn= Button(root, text="Click me", font=30, command=click)
# btn.place(x=400, y=300)

# lbl=Label(root, text="", font=30)
# lbl.place(x=200, y=300)
# root.mainloop()

# config -- changes value on text

# radio button ------- single option can only be chosen
# check button ------- multiple options can be chosen
#  

# from tkinter import *
# root = Tk()
# root.geometry("300x300")


# # methods to access radiobutton value ---- IntVar(), DoubleVar(), BooleanVar(), StringVar().... set()---- set initial action
# def click():
#     if c.get()==1:
#         lbl.config(text="You are male")
#     elif c.get()==2:
#         lbl.config(text="female")
#     elif c.get()==3:
#         lbl.config(text="others")

# lbl=Label(text=" ")
# lbl.pack()

# c= IntVar()

# r1= Radiobutton(text="male",variable=c, value=1)
# r1.pack()
    
# r2= Radiobutton(text="female",variable=c, value=2)
# r2.pack()
    
# r3= Radiobutton(text="others",variable=c, value=3)
# r3.pack()
   

# btn= Button(root, text="Click me", font=30, command=click)
# btn.pack()

# root.mainloop()
# # auto call-- direct call of function in command
# # call after action--- call of function within lambda in command

# def click():
#     lbl.config(text=c.get())

# lbl=Label(text=" ")
# lbl.pack()

# c= StringVar()

# r1= Checkbutton(text="male",variable=c, onvalue="Male", offvalue="")
# r1.pack()
    
# r2= Checkbutton(text="female",variable=c, onvalue="Female", offvalue="")
# r2.pack()
    
# r3= Checkbutton(text="others",variable=c, onvalue="Others", offvalue="")
# r3.pack()
   

# btn= Button(root, text="Click me", font=30, command=click)
# btn.pack()

# def login():
#     pass

# lbl=Label(text=" ")
# lbl.pack()

# c=IntVar()
# r1= Checkbutton(root, variable=c, text="Show", command=login)
# r1.pack()
# root.mainloop()

from tkinter import *

root = Tk()
root.geometry("300x300")

def vehicle():
    vehicle_choice = c.get()
    print(vehicle_choice)

c = StringVar()
c.set(" ") 

r1 = Radiobutton(root, text="car", variable=c, value="car")
r1.pack()

r2 = Radiobutton(root, text="scooter", variable=c, value="scooter")
r2.pack()

r3 = Radiobutton(root, text="motorbike", variable=c, value="motorbike")
r3.pack()

btn = Button(root, text="Confirm", font=30, command=vehicle)
btn.pack()

root.mainloop()


mainloop()