#last page
#importing all the required feilds
from tkinter import *
import random
import mysql.connector as c
#connecting to sql to erase all the temporary tables and felids
t=c.connect(host="localhost",user="root",password="namit",database="specific_user")
cur=t.cursor()
#making a random number for order number
n=random.randint(10000,1000000)
#making a tkinter window
root=Tk()
root.geometry("600x400")
root.configure(bg='grey')
from PIL import ImageTk,Image
"""imag=Image.open("C:/Users/Namith/Documents/namiths/ip project/last.png").resize((600,400))
img=ImageTk.PhotoImage(imag)
Label(root,image=img).pack()"""
#exit button function
def exitb():
    #droppind all the temporary feilds and tables
    sql1="use specific_user"
    cur.execute(sql1)
    sql3="use food"
    sql4="update meals set quant=0"
    sql5="update beverages set quant=0"
    sql6="update starters set quant=0"
    sql7="update bandd set quant=0"
    cur.execute(sql3)
    cur.execute(sql4)
    cur.execute(sql5)
    cur.execute(sql6)
    cur.execute(sql7)
    t.commit()
    root.destroy()
#last page widgets
un=Label(root,bg="grey",text='YOUR ORDER HAS BEEN RECIEVED AND PROCESSED',font=('arial',14,'italic'),foreground="gold")
un.place(relx=0.1,rely=0.4)
un1=Label(root,bg="grey",text='YOUR ORDER NUMBER IS-',font=('arial',11,'italic'),foreground="gold")
un1.place(relx=0.25,rely=0.5)
un2=Label(root,bg="grey",text=n,fg="dark blue",font=('arial 11 underline'))
un2.place(relx=0.58,rely=0.5)
B=Button(root,text='EXIT',bg="grey",fg="gold",font=('arial 10 underline bold'),activebackground="black",command=exitb)
B.place(relx=0.5,rely=0.6)
un3=Label(root,text="THANK YOU COME AGAIN",bg="grey",fg="gold",font=('arial 15 italic bold'))
un3.place(relx=0.5,rely=0.9)
root.mainloop()