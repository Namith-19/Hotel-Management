#address page
#importing the required modules
from tkinter import *
import time
import random
from PIL import ImageTk,Image
#making of tkinter window
root = Tk()
root.geometry('400x500')
root.config(bg='black')
root.title('address page')
#checking if the feilds exist and proceed button function
def prob():
    r1=e1.get()
    r2=e2.get()
    r3=address.get("1.0",END)
    if len(r1)<1:
        e3v.set("please enter valid information")
        r1o=0
    else:
        r1o=len(r1)
    if len(r2)==10:
        r2o=len(r2)
    else:
        e3v.set("please enter valid information")
        r2o=0
    if len(r3)==1:
        e3v.set("please enter valid information")
        r30=0
    else:
        r3o=len(r3)
    if r1o and r2o and r3o>0:
        root.destroy()
        import lastpage
#widgets of address page
Name = StringVar()
Number = StringVar()
frame = Frame(background="black")
frame.pack(pady=10)
frame1 = Frame(background="black")
frame1.pack()
frame2 = Frame(background="black")
frame2.pack(pady=5)
Label(frame, text = 'Name', font='arial 12 bold',fg="gold",bg="black").pack(side=LEFT)
e1s=StringVar()
e1s.set("")
e1=Entry(frame, textvariable =e1s,width=50,background="light blue")
e1.pack()
Label(frame1, text = 'Phone No.', font='arial 12 bold',fg="gold",bg="black").pack(side=LEFT)
e2s=StringVar()
e2s.set("")
e2=Entry(frame1, textvariable =e2s ,width=50,background="light blue")
e2.pack()  
Label(frame2, text = 'Address', font='arial 12 bold',fg="gold",bg="black").pack(side=LEFT)
address =Text(frame2,width=37,height=10,background="light blue")
address.pack()
Button(root,text="Proceed",font="arial 12 bold underline",command=prob,bg="black",fg="light green",activebackground="light grey",width=12).place(x=145, y=270)
e3v=StringVar()
Label(frame2,textvariable=e3v,bg="black",fg="red").pack()
# Execute Tkinter
root.mainloop()