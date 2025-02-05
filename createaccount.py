#create account page
# importing required modules
from tkinter import *
import tkinter.font as c
from PIL import ImageTk,Image
import mysql.connector as n
import time
#creating tkinter window
t=Tk()
t.geometry("400x400")
t.title("create account")
t.configure(bg="dark blue")
#back button function
def backb():
    t.destroy()
    import LOGIN
#create account button function
def createab():
    #retreving values of feilds
    if len(t1.get()) and len(t2.get()) and len(t3.get())>0:
        if t2.get()==t3.get():
            #connecting to sql
            C=n.connect(host="localhost",user="root",password="namit",database="login_info")
            T=C.cursor()
            #inserting the values
            try:
                e=("INSERT INTO login(username,password) VALUES(%s,%s)")
                v=(t1.get(),t2.get())
                T.execute(e,v)
                C.commit()
                #if error printing error
            except n.Error as err:
                p.set("THIS ACCOUNT ALREADY EXISTS")
                C.close()
            u=t1.get()
            T.execute("select * from login where username='%s'"),(u)
            r=T.rowcount
            #checking if the account is created
            if r== 0:
                p.set("NOT DONE")
            else:
                p.set("SUCCESSFULLY CREATED YOUR ACCOUNT PLEASE LOGIN")
                time.sleep(2)
        else:
            p.set("PASSWORDS DONT MATCH")
    else:
        p.set("PLEASE ENTER ALL THE FEILDS")   
font1=c.Font(size=19,weight="bold",slant="italic")
font2=c.Font(size=13,weight="bold",slant="italic")
l1=Label(t,text="Create Account",font=font1,background="dark blue",foreground="yellow")
l1.place(relx=0.25,rely=0)
l2=Label(t,text="Username:",font=font2,background="dark blue",foreground="gold")
l2.place(relx=0.21,rely=0.4)
l3=Label(t,text="Password:",font=font2,background="dark blue",foreground="gold")
l3.place(relx=0.21,rely=0.45)
l4=Label(t,text="Re Enter:",font=font2,background="dark blue",foreground="gold")
l4.place(relx=0.21,rely=0.5)
uvar=StringVar()
pvar=StringVar()
revar=StringVar()
t1=Entry(t,textvariable=uvar)
t1.place(relx=0.45,rely=0.4)
t2=Entry(t,textvariable=pvar)
t2.place(relx=0.45,rely=0.45)
t3=Entry(t,textvariable=revar)
t3.place(relx=0.45,rely=0.5)
b1=Button(t,text="Create Account",background="light blue",activebackground="grey",command=createab,height=1,width=17)
b1.place(relx=0.35,rely=0.59)
b2=Button(t,text="<back",background="dark blue",activeforeground="red",foreground="orange",command=backb)
b2.place(relx=0,rely=0)
p=StringVar()
l=Label(t,textvariable=p,background="dark blue",foreground="yellow",font=13)
l.place(relx=0.25,rely=0.7)
t.mainloop()