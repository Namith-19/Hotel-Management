#login page
#importing the required modules
from tkinter import *
import tkinter.font as c
from PIL import ImageTk,Image
import mysql.connector as n
import time
#connecting to sql
c2=n.connect(host="localhost",user="root",password="namit",database="login_info")
t2=c2.cursor()
#making a tkinter window
t=Tk()
t.geometry("600x600")
t.config(bg="black")
#imag=Image.open("C:/Users/Namith/Documents/namiths/ip project/ex.png").resize((600,600))
#img=ImageTk.PhotoImage(imag)
t.title("login")
#Label(t,image=img).pack()
#function of login button
def loginb():
    #retreving the entry of password and username
    unm=un.get()
    psd=pa.get()
    #checking the database and confirmation of login detials
    if len(psd) and len(unm)>0:
        sql3="use login_info"
        sql = "select * from login where username = %s and password = %s"
        t2.execute(sql3)
        t2.execute(sql,[(unm),(psd)])
        results = t2.fetchall()
        if results:
            #creating all the temp tables
           for i in results:
               sql2="use specific_user"
               sql6="drop table if exists log"
               sql4="create table log(name varchar(20),id varchar(100))"
               t2.execute(sql2)
               t2.execute(sql6)
               time.sleep(1)
               t2.execute(sql4)
               uf=(un.get(),1)
               sql5=("INSERT INTO log(name,id) VALUES(%s,%s);")
               t2.execute(sql5,uf)
               c2.commit()
               t.destroy()
               import home
               break
            
        else:
            p.set("Incorrect password/username")
    else:
        p.set("Please all the fields")
 #create button function   
def createab():
    t.destroy()
    import createaccount 
#login page widgets       
font1=c.Font(size=13,weight="bold",slant="italic")
font2=c.Font(family="Lucida Sans",size=19,weight="bold",slant="italic")
font3=c.Font(size=10,weight="bold",slant="italic")
l1=Label(t,text="welcome to diner to door!!!!",foreground="maroon",background="black",font=font2)
l1.place(relx =0.26, rely =0)
l2=Label(t,text="Username:",foreground="dark blue",background="black",font=font1)
l2.place(relx = 0.35, rely = 0.3)
l3=Label(t,text="Password:",foreground="dark blue",background="black",font=font1)
l3.place(relx=0.35,rely=0.4)
pa=Entry(t,textvariable=StringVar())
un=Entry(t,textvariable=StringVar())
pa.place(relx=0.51,rely=0.4)
un.place(relx=0.51,rely=0.3)
b1=Button(t,text="login",activebackground="blue",bg="dark grey",font=font3,command=loginb,width=10,height=2)
b1.place(relx=0.35,rely=0.5)
b2=Button(t,text="create account",font=font3,command=createab,width=15,height=2,bg="dark grey")
b2.place(relx=0.57,rely=0.5)
p=StringVar()
l=Label(t,textvariable=p,background="black",foreground="red",font=15)
l.place(relx=0.38,rely=0.7)
u=un.get()
t.mainloop()