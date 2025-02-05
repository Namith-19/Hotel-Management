# home page
# importing all the required modules
from tkinter import *
import tkinter.font as c
import time
import random
import datetime
from PIL import ImageTk, Image
from tkinter import Tk, StringVar, ttk
import mysql.connector as c1
# declaring all the variables required
msu = int()
ssu = int()
bsu = int()
bdsu = int()
# connecting to sql
t = c1.connect(
    host="localhost", user="root", password="namit", database="food", autocommit=True
)
c2 = t.cursor()
# making the tkinter window
r = Tk()
r.geometry("400x400")
r.configure(bg="black")
"""imag=Image.open("C:/Users/Namith/Documents/namiths/ip project/home.png").resize((400,400))
img=ImageTk.PhotoImage(imag)
Label(r,image=img).pack()"""
r.title("HOME PAGE")
# function to run on starting the page
def ini():
    con1 = t.cursor()
    # displaying the name of user
    sqi = "use specific_user"
    sqi1 = "select name from log;"
    con1.execute(sqi)
    con1.execute(sqi1)
    ri = con1.fetchone()
    ri1 = str(ri[0]).title()
    l6v.set(ri1)


# logout button function
def logout():
    r.destroy()
    import LOGIN


# meals page function
def meals():
    # window for meals page
    n = Toplevel(r)
    n.geometry("970x800")
    n.title("Meals")
    n.configure(bg="black")
    # function for the starting of the page
    def ini():
        # connecting to sql to retrieve all tthe previous selected values
        sq = t.cursor()
        cmd1 = "use food"
        sq.execute(cmd1)
        qunt = []
        x = [
            "naan",
            "rumaliroti",
            "puri",
            "friedrice",
            "biryani",
            "pannerbuttermasala",
            "rajmadaal",
            "cholebhature",
            "lacha paneer",
        ]
        for i in range(0, len(x)):
            m = "select quant from meals where name='%s'" % (x[i])
            sq.execute(m)
            y = sq.fetchall()
            qunt.append(y[0][0])
        las.set(qunt[0])
        lbs.set(qunt[1])
        lcs.set(qunt[2])
        lds.set(qunt[3])
        les.set(qunt[4])
        lfs.set(qunt[5])
        lgs.set(qunt[6])
        lhs.set(qunt[7])
        lis.set(qunt[8])
        u1 = int(e1.get()) * 30
        u2 = int(e2.get()) * 30
        u3 = int(e3.get()) * 30
        u4 = int(e4.get()) * 50
        u5 = int(e5.get()) * 50
        u6 = int(e6.get()) * 50
        u7 = int(e7.get()) * 20
        u8 = int(e8.get()) * 20
        u9 = int(e9.get()) * 30
        sum1 = u1 + u2 + u3 + u4 + u5 + u6 + u7 + u8 + u9
        su = sum1
        lks.set(su)

    # function for the add button
    def addb():
        # making the total amount and displaying
        u1 = int(e1.get()) * 30
        u2 = int(e2.get()) * 30
        u3 = int(e3.get()) * 30
        u4 = int(e4.get()) * 50
        u5 = int(e5.get()) * 50
        u6 = int(e6.get()) * 50
        u7 = int(e7.get()) * 20
        u8 = int(e8.get()) * 20
        u9 = int(e9.get()) * 30
        sum1 = u1 + u2 + u3 + u4 + u5 + u6 + u7 + u8 + u9
        su = sum1
        lks.set(su)
        # making of a global variable fot displaying total amount in the home page
        global msu
        msu = sum1

    # next button function
    def nextb():
        # adding the selected products and their number to table in sql
        u1 = int(las.get())
        u2 = int(lbs.get())
        u3 = int(lcs.get())
        u4 = int(lds.get())
        u5 = int(les.get())
        u6 = int(lfs.get())
        u7 = int(lgs.get())
        u8 = int(lhs.get())
        u9 = int(lis.get())
        up = [
            (u1, "naan"),
            (u2, "rumaliroti"),
            (u3, "puri"),
            (u4, "friedrice"),
            (u5, "biryani"),
            (u6, "pannerbuttermasala"),
            (u7, "rajmadaal"),
            (u8, "cholebhature"),
            (u9, "lacha paneer"),
        ]
        sql1 = "use food"
        sql2 = "update meals set quant=%s where name=%s"
        c2.execute(sql1)
        c2.executemany(sql2, up)
        t.commit()
        n.destroy()
        import home

    # meals page widgets
    Tops = Frame(n, width=1350, height=100, bd=12, relief="raise", bg="black")
    Tops.pack(side=TOP)
    lblTitle = Label(
        Tops, font="times 36 bold underline", text="Meals", bg="black", fg="orange"
    )
    lblTitle.grid(row=0, column=0)
    BottomMainFrame = Frame(
        n, width=1350, height=650, bd=12, relief="raise", bg="black"
    )
    BottomMainFrame.pack(side=TOP)
    f1 = Frame(
        BottomMainFrame, width=450, height=650, bd=12, relief="raise", bg="black"
    )
    f1.pack(side=LEFT)
    f2 = Frame(
        BottomMainFrame, width=450, height=650, bd=12, relief="raise", bg="black"
    )
    f2.pack(side=LEFT)
    l1 = Label(f2, text="Amount", font="times 28 bold underline", bg="black", fg="blue")
    l1.place(x=0, y=0)
    l2 = Label(
        f2,
        text="1. Naan                                       RS.30",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l2.place(x=0, y=100)
    l3 = Label(
        f2,
        text="2. Rumali Roti                           RS.30",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l3.place(x=0, y=150)
    l4 = Label(
        f2,
        text="3. Puri                                        RS.30",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l4.place(x=0, y=200)
    l5 = Label(
        f2,
        text="4. FriedRice                               RS.50",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l5.place(x=0, y=250)
    l6 = Label(
        f2,
        text="5. Biryani                                   RS.50",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l6.place(x=0, y=300)
    l7 = Label(
        f2,
        text="6. Paneer Butter Masala          RS.50",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l7.place(x=0, y=350)
    l8 = Label(
        f2,
        text="7. RajmaDaal                             RS.20",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l8.place(x=0, y=400)
    l9 = Label(
        f2,
        text="8. CholeBhature                        RS.20",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l9.place(x=0, y=450)
    l0 = Label(
        f2,
        text="9. Lacha Paneer                        RS.30",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l0.place(x=0, y=500)
    lz = Label(
        f1, text="No. Of Dishes", font="times 28 bold underline", bg="black", fg="blue"
    )
    lz.place(x=0, y=0)
    las = IntVar()
    las.set(0)
    la = Label(f1, text="1. Naan", font="times 18 bold", bg="black", fg="orange")
    la.place(x=0, y=100)
    e1 = Entry(f1, textvariable=las)
    e1.place(x=300, y=107)
    lbs = IntVar()
    lbs.set(0)
    lb = Label(f1, text="2. Rumali Roti", font="times 18 bold", bg="black", fg="orange")
    lb.place(x=0, y=150)
    e2 = Entry(f1, textvariable=lbs)
    e2.place(x=300, y=157)
    lcs = IntVar()
    lcs.set(0)
    lc = Label(f1, text="3. Puri", font="times 18 bold", bg="black", fg="orange")
    lc.place(x=0, y=200)
    e3 = Entry(f1, textvariable=lcs)
    e3.place(x=300, y=207)
    lds = IntVar()
    lds.set(0)
    ld = Label(f1, text="4. FriedRice", font="times 18 bold", bg="black", fg="orange")
    ld.place(x=0, y=250)
    e4 = Entry(f1, textvariable=lds)
    e4.place(x=300, y=257)
    les = IntVar()
    les.set(0)
    le = Label(f1, text="5. Biryani", font="times 18 bold", bg="black", fg="orange")
    le.place(x=0, y=300)
    e5 = Entry(f1, textvariable=les)
    e5.place(x=300, y=307)
    lfs = IntVar()
    lfs.set(0)
    lf = Label(
        f1,
        text="6. Paneer Butter Masala",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    lf.place(x=0, y=350)
    e6 = Entry(f1, textvariable=lfs)
    e6.place(x=300, y=357)
    lgs = IntVar()
    lgs.set(0)
    lg = Label(f1, text="7. RajmaDaal", font="times 18 bold", bg="black", fg="orange")
    lg.place(x=0, y=400)
    e7 = Entry(f1, textvariable=lgs)
    e7.place(x=300, y=407)
    lhs = IntVar()
    lhs.set(0)
    lh = Label(
        f1, text="8. CholeBhature", font="times 18 bold", bg="black", fg="orange"
    )
    lh.place(x=0, y=450)
    e8 = Entry(f1, textvariable=lhs)
    e8.place(x=300, y=457)
    lis = IntVar()
    lis.set(0)
    li = Label(
        f1, text="9. Lacha Paneer", font="times 18 bold", bg="black", fg="orange"
    )
    li.place(x=0, y=500)
    e9 = Entry(f1, textvariable=lis)
    e9.place(x=300, y=507)
    b1 = Button(
        f1, text="add", bg="grey", width=15, height=1, font=13, command=addb, fg="gold"
    )
    b1.place(relx=0.03, rely=0.85)
    lj = Label(f1, text="TOTAL COST:", font=10, bg="black", fg="gold")
    lj.place(relx=0.46, rely=0.853)
    lks = IntVar()
    lk = Label(f1, textvariable=lks, font=7, bg="black", fg="gold")
    lk.place(relx=0.8, rely=0.853)
    b2 = Button(
        f1, text="next", bg="light blue", command=nextb, height=1, width=13, font=13
    )
    b2.place(relx=0.048, rely=0.92)
    ini()


# starters page function
def starters():
    # preparing window for starters page
    n = Toplevel(r)
    n.geometry("970x800")
    n.title("starters")
    n.configure(bg="black")
    # function for the starting of page
    def ini():
        # connecting sql to retreve all the previous selected items
        sq = t.cursor()
        cmd1 = "use food"
        sq.execute(cmd1)
        qunt = []
        x = [
            "paneertikka",
            "papdichat",
            "panipuri",
            "friedcorn",
            "babycorn",
            "springroll",
            "paner65",
            "tomatosoup",
            "mixedvegsoup",
        ]
        for i in range(0, len(x)):
            m = "select quant from starters where name='%s'" % (x[i])
            sq.execute(m)
            y = sq.fetchall()
            qunt.append(y[0][0])
        las.set(qunt[0])
        lbs.set(qunt[1])
        lcs.set(qunt[2])
        lds.set(qunt[3])
        les.set(qunt[4])
        lfs.set(qunt[5])
        lgs.set(qunt[6])
        lhs.set(qunt[7])
        lis.set(qunt[8])
        u1 = int(e1.get()) * 30
        u2 = int(e2.get()) * 20
        u3 = int(e3.get()) * 10
        u4 = int(e4.get()) * 20
        u5 = int(e5.get()) * 25
        u6 = int(e6.get()) * 20
        u7 = int(e7.get()) * 30
        u8 = int(e8.get()) * 20
        u9 = int(e9.get()) * 30
        sum1 = u1 + u2 + u3 + u4 + u5 + u6 + u7 + u8 + u9
        su = sum1
        lks.set(su)

    # function for add button
    def addb():
        # making the total amount
        u1 = int(e1.get()) * 30
        u2 = int(e2.get()) * 20
        u3 = int(e3.get()) * 10
        u4 = int(e4.get()) * 20
        u5 = int(e5.get()) * 25
        u6 = int(e6.get()) * 20
        u7 = int(e7.get()) * 30
        u8 = int(e8.get()) * 20
        u9 = int(e9.get()) * 30
        sum1 = u1 + u2 + u3 + u4 + u5 + u6 + u7 + u8 + u9
        su = sum1
        lks.set(su)
        # making global variable for displaying the total amount in the home page
        global ssu
        ssu = sum1

    # function for next button
    def nextb():
        # adding thw values in the databse
        u1 = int(las.get())
        u2 = int(lbs.get())
        u3 = int(lcs.get())
        u4 = int(lds.get())
        u5 = int(les.get())
        u6 = int(lfs.get())
        u7 = int(lgs.get())
        u8 = int(lhs.get())
        u9 = int(lis.get())
        up = [
            (u1, "paneertikka"),
            (u2, "papdichat"),
            (u3, "panipuri"),
            (u4, "friedcorn"),
            (u5, "babycorn"),
            (u6, "springrolls"),
            (u7, "paner65"),
            (u8, "tomatospup"),
            (u9, "mixedvegsoup"),
        ]
        sql1 = "use food"
        sql2 = "update starters set quant=%s where name=%s"
        c2.execute(sql1)
        c2.executemany(sql2, up)
        t.commit()
        n.destroy()
        import home

    # widgets of starters page
    Tops = Frame(n, width=1350, height=100, bd=12, relief="raise", bg="black")
    Tops.pack(side=TOP)
    lblTitle = Label(
        Tops, font="times 36 bold underline", text="Starters", bg="black", fg="green"
    )
    lblTitle.grid(row=0, column=0)
    BottomMainFrame = Frame(
        n, width=1350, height=650, bd=12, relief="raise", bg="black"
    )
    BottomMainFrame.pack(side=TOP)
    f1 = Frame(
        BottomMainFrame, width=450, height=650, bd=12, relief="raise", bg="black"
    )
    f1.pack(side=LEFT)
    f2 = Frame(
        BottomMainFrame, width=450, height=650, bd=12, relief="raise", bg="black"
    )
    f2.pack(side=LEFT)
    l1 = Label(f2, text="Amount", font="times 28 bold underline", bg="black", fg="blue")
    l1.place(x=0, y=0)
    l2 = Label(
        f2,
        text="1. PaneerTikka                        RS.30",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l2.place(x=0, y=100)
    l3 = Label(
        f2,
        text="2. PapdiChaat                          RS.20",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l3.place(x=0, y=150)
    l4 = Label(
        f2,
        text="3. PaniPuri                               RS.10",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l4.place(x=0, y=200)
    l5 = Label(
        f2,
        text="4. FriedCorn                            RS.20",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l5.place(x=0, y=250)
    l6 = Label(
        f2,
        text="5. BabyCorn                             RS.25",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l6.place(x=0, y=300)
    l7 = Label(
        f2,
        text="6. SpringRolls                          RS.20",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l7.place(x=0, y=350)
    l8 = Label(
        f2,
        text="7. Paneer65                              RS.30",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l8.place(x=0, y=400)
    l9 = Label(
        f2,
        text="8. TomatoSoup                         RS.20",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l9.place(x=0, y=450)
    l0 = Label(
        f2,
        text="9. MixedVegSoup                     RS.30",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l0.place(x=0, y=500)
    lz = Label(
        f1, text="No. Of Dishes", font="times 28 bold underline", bg="black", fg="blue"
    )
    lz.place(x=0, y=0)
    las = IntVar()
    las.set(0)
    la = Label(f1, text="1. PaneerTikka", font="times 18 bold", bg="black", fg="orange")
    la.place(x=0, y=100)
    e1 = Entry(f1, textvariable=las)
    e1.place(x=300, y=107)
    lbs = IntVar()
    lbs.set(0)
    lb = Label(f1, text="2. PapdiChaat", font="times 18 bold", bg="black", fg="orange")
    lb.place(x=0, y=150)
    e2 = Entry(f1, textvariable=lbs)
    e2.place(x=300, y=157)
    lcs = IntVar()
    lcs.set(0)
    lc = Label(f1, text="3. PaniPuri", font="times 18 bold", bg="black", fg="orange")
    lc.place(x=0, y=200)
    e3 = Entry(f1, textvariable=lcs)
    e3.place(x=300, y=207)
    lds = IntVar()
    lds.set(0)
    ld = Label(f1, text="4. FriedCorn", font="times 18 bold", bg="black", fg="orange")
    ld.place(x=0, y=250)
    e4 = Entry(f1, textvariable=lds)
    e4.place(x=300, y=257)
    les = IntVar()
    les.set(0)
    le = Label(f1, text="5. BabyCorn", font="times 18 bold", bg="black", fg="orange")
    le.place(x=0, y=300)
    e5 = Entry(f1, textvariable=les)
    e5.place(x=300, y=307)
    lfs = IntVar()
    lfs.set(0)
    lf = Label(f1, text="6. SpringRolls", font="times 18 bold", bg="black", fg="orange")
    lf.place(x=0, y=350)
    e6 = Entry(f1, textvariable=lfs)
    e6.place(x=300, y=357)
    lgs = IntVar()
    lgs.set(0)
    lg = Label(f1, text="7. Paneer65", font="times 18 bold", bg="black", fg="orange")
    lg.place(x=0, y=400)
    e7 = Entry(f1, textvariable=lgs)
    e7.place(x=300, y=407)
    lhs = IntVar()
    lhs.set(0)
    lh = Label(f1, text="8. TomatoSoup", font="times 18 bold", bg="black", fg="orange")
    lh.place(x=0, y=450)
    e8 = Entry(f1, textvariable=lhs)
    e8.place(x=300, y=457)
    lis = IntVar()
    lis.set(0)
    li = Label(
        f1, text="9. MixedVegSoup", font="times 18 bold", bg="black", fg="orange"
    )
    li.place(x=0, y=500)
    e9 = Entry(f1, textvariable=lis)
    e9.place(x=300, y=507)
    b1 = Button(
        f1, text="add", bg="grey", width=15, height=1, font=13, command=addb, fg="gold"
    )
    b1.place(relx=0.03, rely=0.85)
    lj = Label(f1, text="TOTAL COST:", font=10, bg="black", fg="gold")
    lj.place(relx=0.46, rely=0.853)
    lks = IntVar()
    lk = Label(f1, textvariable=lks, font=7, bg="black", fg="gold")
    lk.place(relx=0.8, rely=0.853)
    b2 = Button(
        f1, text="next", bg="light blue", command=nextb, height=1, width=13, font=13
    )
    b2.place(relx=0.048, rely=0.92)
    ini()


# beverages page function
def beverages():
    # making a window for beverages page
    n = Toplevel(r)
    n.geometry("970x800")
    n.title("Meals")
    n.configure(bg="black")
    # function for the strting of page
    def ini():
        # connecting to sql to retrieve all tthe previous selected values
        sq = t.cursor()
        cmd1 = "use food"
        sq.execute(cmd1)
        qunt = []
        x = [
            "coca-cola",
            "thumbsup",
            "frooti",
            "buttermilk",
            "badammilk",
            "hotchocolate",
            "tea",
            "coffee",
            "cappuccino",
        ]
        for i in range(0, len(x)):
            m = "select quant from beverages where name='%s'" % (x[i])
            sq.execute(m)
            y = sq.fetchall()
            qunt.append(y[0][0])
        las.set(qunt[0])
        lbs.set(qunt[1])
        lcs.set(qunt[2])
        lds.set(qunt[3])
        les.set(qunt[4])
        lfs.set(qunt[5])
        lgs.set(qunt[6])
        lhs.set(qunt[7])
        lis.set(qunt[8])
        u1 = int(e1.get()) * 20
        u2 = int(e2.get()) * 20
        u3 = int(e3.get()) * 10
        u4 = int(e4.get()) * 20
        u5 = int(e5.get()) * 20
        u6 = int(e6.get()) * 20
        u7 = int(e7.get()) * 10
        u8 = int(e8.get()) * 15
        u9 = int(e9.get()) * 30
        sum1 = u1 + u2 + u3 + u4 + u5 + u6 + u7 + u8 + u9
        su = sum1
        lks.set(su)

    # function of add button
    def addb():
        # making the total amount and displaying
        u1 = int(e1.get()) * 20
        u2 = int(e2.get()) * 20
        u3 = int(e3.get()) * 10
        u4 = int(e4.get()) * 20
        u5 = int(e5.get()) * 20
        u6 = int(e6.get()) * 20
        u7 = int(e7.get()) * 10
        u8 = int(e8.get()) * 15
        u9 = int(e9.get()) * 30
        sum1 = u1 + u2 + u3 + u4 + u5 + u6 + u7 + u8 + u9
        su = sum1
        lks.set(su)
        # declaring a global variable for displaying total amount  on the home page
        global bsu
        bsu = sum1

    # function for next button
    def nextb():
        # adding the values entered to the sql database
        u1 = int(las.get())
        u2 = int(lbs.get())
        u3 = int(lcs.get())
        u4 = int(lds.get())
        u5 = int(les.get())
        u6 = int(lfs.get())
        u7 = int(lgs.get())
        u8 = int(lhs.get())
        u9 = int(lis.get())
        up = [
            (u1, "coca-cola"),
            (u2, "thumbsup"),
            (u3, "frooti"),
            (u4, "buttermilk"),
            (u5, "bbadammilk"),
            (u6, "hotchocolate"),
            (u7, "tea"),
            (u8, "coffee"),
            (u9, "cappuccino"),
        ]
        sql1 = "use food"
        sql2 = "update beverages set quant=%s where name=%s"
        c2.execute(sql1)
        c2.executemany(sql2, up)
        t.commit()
        n.destroy()
        import home

    # widgets for beverages page
    Tops = Frame(n, width=1350, height=100, bd=12, relief="raise", bg="black")
    Tops.pack(side=TOP)
    lblTitle = Label(
        Tops,
        font="times 36 bold underline",
        text="Beverages",
        bg="black",
        fg="light blue",
    )
    lblTitle.grid(row=0, column=0)
    BottomMainFrame = Frame(
        n, width=1350, height=650, bd=12, relief="raise", bg="black"
    )
    BottomMainFrame.pack(side=TOP)
    f1 = Frame(
        BottomMainFrame, width=450, height=650, bd=12, relief="raise", bg="black"
    )
    f1.pack(side=LEFT)
    f2 = Frame(
        BottomMainFrame, width=450, height=650, bd=12, relief="raise", bg="black"
    )
    f2.pack(side=LEFT)
    l1 = Label(f2, text="Amount", font="times 28 bold underline", bg="black", fg="blue")
    l1.place(x=0, y=0)
    l2 = Label(
        f2,
        text="1. Coca-Cola                            RS.20",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l2.place(x=0, y=100)
    l3 = Label(
        f2,
        text="2. ThumsUp                             RS.20",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l3.place(x=0, y=150)
    l4 = Label(
        f2,
        text="3. Frooti                                   RS.10",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l4.place(x=0, y=200)
    l5 = Label(
        f2,
        text="4. ButterMilk                          RS.20",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l5.place(x=0, y=250)
    l6 = Label(
        f2,
        text="5. BadamMilk                         RS.20",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l6.place(x=0, y=300)
    l7 = Label(
        f2,
        text="6. HotChocolate                      RS.20",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l7.place(x=0, y=350)
    l8 = Label(
        f2,
        text="7. Tea                                       RS.10",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l8.place(x=0, y=400)
    l9 = Label(
        f2,
        text="8. Coffee                                   RS.15",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l9.place(x=0, y=450)
    l0 = Label(
        f2,
        text="9. Cappuccino                          RS.30",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l0.place(x=0, y=500)
    lz = Label(
        f1, text="No. Of Dishes", font="times 28 bold underline", bg="black", fg="blue"
    )
    lz.place(x=0, y=0)
    las = IntVar()
    las.set(0)
    la = Label(f1, text="1. Coca-Cola", font="times 18 bold", bg="black", fg="orange")
    la.place(x=0, y=100)
    e1 = Entry(f1, textvariable=las)
    e1.place(x=300, y=107)
    lbs = IntVar()
    lbs.set(0)
    lb = Label(f1, text="2. ThumsUp", font="times 18 bold", bg="black", fg="orange")
    lb.place(x=0, y=150)
    e2 = Entry(f1, textvariable=lbs)
    e2.place(x=300, y=157)
    lcs = IntVar()
    lcs.set(0)
    lc = Label(f1, text="3. Frooti", font="times 18 bold", bg="black", fg="orange")
    lc.place(x=0, y=200)
    e3 = Entry(f1, textvariable=lcs)
    e3.place(x=300, y=207)
    lds = IntVar()
    lds.set(0)
    ld = Label(f1, text="4. ButterMilk", font="times 18 bold", bg="black", fg="orange")
    ld.place(x=0, y=250)
    e4 = Entry(f1, textvariable=lds)
    e4.place(x=300, y=257)
    les = IntVar()
    les.set(0)
    le = Label(f1, text="5. BadamMilk", font="times 18 bold", bg="black", fg="orange")
    le.place(x=0, y=300)
    e5 = Entry(f1, textvariable=les)
    e5.place(x=300, y=307)
    lfs = IntVar()
    lfs.set(0)
    lf = Label(
        f1, text="6. HotChocolate", font="times 18 bold", bg="black", fg="orange"
    )
    lf.place(x=0, y=350)
    e6 = Entry(f1, textvariable=lfs)
    e6.place(x=300, y=357)
    lgs = IntVar()
    lgs.set(0)
    lg = Label(f1, text="7. Tea", font="times 18 bold", bg="black", fg="orange")
    lg.place(x=0, y=400)
    e7 = Entry(f1, textvariable=lgs)
    e7.place(x=300, y=407)
    lhs = IntVar()
    lhs.set(0)
    lh = Label(f1, text="8. Coffee", font="times 18 bold", bg="black", fg="orange")
    lh.place(x=0, y=450)
    e8 = Entry(f1, textvariable=lhs)
    e8.place(x=300, y=457)
    lis = IntVar()
    lis.set(0)
    li = Label(f1, text="9. Cappuccino", font="times 18 bold", bg="black", fg="orange")
    li.place(x=0, y=500)
    e9 = Entry(f1, textvariable=lis)
    e9.place(x=300, y=507)
    b1 = Button(
        f1, text="add", bg="grey", width=15, height=1, font=13, command=addb, fg="gold"
    )
    b1.place(relx=0.03, rely=0.85)
    lj = Label(f1, text="TOTAL COST:", font=10, bg="black", fg="gold")
    lj.place(relx=0.46, rely=0.853)
    lks = IntVar()
    lk = Label(f1, textvariable=lks, font=7, bg="black", fg="gold")
    lk.place(relx=0.8, rely=0.853)
    b2 = Button(
        f1, text="next", bg="light blue", command=nextb, height=1, width=13, font=13
    )
    b2.place(relx=0.048, rely=0.92)
    ini()


# baked and dessertts page function
def dandb():
    # making a window for baked and desserts page
    n = Toplevel(r)
    n.geometry("970x800")
    n.title("beverages and desserts")
    n.configure(bg="black")
    # function for strting the page
    def ini():
        # connecting to sql to retrieve all tthe previous selected values
        sq = t.cursor()
        cmd1 = "use food"
        sq.execute(cmd1)
        qunt = []
        x = [
            "chocolatechipcookies",
            "doughnuts",
            "plumcake",
            "icecreamrolls",
            "germanblackforestcake",
            "frozenicecreamcookies",
            "nutbrownies",
            "icecream",
        ]
        for i in range(0, len(x)):
            m = "select quant from bandd where name='%s'" % (x[i])
            sq.execute(m)
            y = sq.fetchall()
            qunt.append(y[0][0])
        las.set(qunt[0])
        lbs.set(qunt[1])
        lcs.set(qunt[2])
        lds.set(qunt[3])
        les.set(qunt[4])
        lfs.set(qunt[5])
        lgs.set(qunt[6])
        lhs.set(qunt[7])
        u1 = int(e1.get()) * 50
        u2 = int(e2.get()) * 35
        u3 = int(e3.get()) * 20
        u4 = int(e4.get()) * 25
        u5 = int(e5.get()) * 60
        u6 = int(e6.get()) * 45
        u7 = int(e7.get()) * 40
        u8 = int(e8.get()) * 95
        sum1 = u1 + u2 + u3 + u4 + u5 + u6 + u7 + u8
        su = sum1
        lks.set(su)

    # function for add button
    def addb():
        # calculating the total amount
        u1 = int(e1.get()) * 50
        u2 = int(e2.get()) * 35
        u3 = int(e3.get()) * 20
        u4 = int(e4.get()) * 25
        u5 = int(e5.get()) * 60
        u6 = int(e6.get()) * 45
        u7 = int(e7.get()) * 40
        u8 = int(e8.get()) * 95
        sum1 = u1 + u2 + u3 + u4 + u5 + u6 + u7 + u8
        su = sum1
        lks.set(su)
        # createing a global variable for displaying total amount on home page
        global bdsu
        bdsu = su

    # next page function
    def nextb():
        u1 = int(las.get())
        u2 = int(lbs.get())
        u3 = int(lcs.get())
        u4 = int(lds.get())
        u5 = int(les.get())
        u6 = int(lfs.get())
        u7 = int(lgs.get())
        u8 = int(lhs.get())
        up = [
            (u1, "chocolatechipcookies"),
            (u2, "doughnuts"),
            (u3, "plumcake"),
            (u4, "icecreamrolls"),
            (u5, "germanblackforestcake"),
            (u6, "frozenicecreamcookies"),
            (u7, "nutbrownies"),
            (u8, "icecream"),
        ]
        sql1 = "use food"
        sql2 = "update bandd set quant=%s where name=%s"
        c2.execute(sql1)
        c2.executemany(sql2, up)
        t.commit()
        n.destroy()
        import home

    # widgets for baked and desserts page
    Tops = Frame(n, width=1350, height=100, bd=12, relief="raise", bg="black")
    Tops.pack(side=TOP)
    lblTitle = Label(
        Tops,
        font="times 36 bold underline",
        text="Bakes and Desserts",
        bg="black",
        fg="yellow",
    )
    lblTitle.grid(row=0, column=0)
    BottomMainFrame = Frame(
        n, width=1350, height=650, bd=12, relief="raise", bg="black"
    )
    BottomMainFrame.pack(side=TOP)
    f1 = Frame(
        BottomMainFrame, width=450, height=650, bd=12, relief="raise", bg="black"
    )
    f1.pack(side=LEFT)
    f2 = Frame(
        BottomMainFrame, width=450, height=650, bd=12, relief="raise", bg="black"
    )
    f2.pack(side=LEFT)
    l1 = Label(f2, text="Amount", font="times 28 bold underline", bg="black", fg="blue")
    l1.place(x=0, y=0)
    l2 = Label(
        f2,
        text="1. Chocolate chip cookies                RS.50",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l2.place(x=0, y=100)
    l3 = Label(
        f2,
        text="2. Doughnuts                                     RS.35",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l3.place(x=0, y=150)
    l4 = Label(
        f2,
        text="3. Plum cakes                                    RS.20",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l4.place(x=0, y=200)
    l5 = Label(
        f2,
        text="4. Icecream rolls                               RS.25",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l5.place(x=0, y=250)
    l6 = Label(
        f2,
        text="5. German black forest cake            RS.60",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l6.place(x=0, y=300)
    l7 = Label(
        f2,
        text="6. Frozen icecream cookies              RS.45",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l7.place(x=0, y=350)
    l8 = Label(
        f2,
        text="7. Nut brownies                                 RS.40",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l8.place(x=0, y=400)
    l9 = Label(
        f2,
        text="8. Ice cream                                       RS.95",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    l9.place(x=0, y=450)
    lz = Label(
        f1, text="No. Of Dishes", font="times 28 bold underline", bg="black", fg="blue"
    )
    lz.place(x=0, y=0)
    las = IntVar()
    las.set(0)
    la = Label(
        f1,
        text="1. chocolate chip cookies",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    la.place(x=0, y=100)
    e1 = Entry(f1, textvariable=las)
    e1.place(x=300, y=107)
    lbs = IntVar()
    lbs.set(0)
    lb = Label(f1, text="2. doughnuts", font="times 18 bold", bg="black", fg="orange")
    lb.place(x=0, y=150)
    e2 = Entry(f1, textvariable=lbs)
    e2.place(x=300, y=157)
    lcs = IntVar()
    lcs.set(0)
    lc = Label(f1, text="3.plum cakes", font="times 18 bold", bg="black", fg="orange")
    lc.place(x=0, y=200)
    e3 = Entry(f1, textvariable=lcs)
    e3.place(x=300, y=207)
    lds = IntVar()
    lds.set(0)
    ld = Label(
        f1, text="4. ice cream rolls", font="times 18 bold", bg="black", fg="orange"
    )
    ld.place(x=0, y=250)
    e4 = Entry(f1, textvariable=lds)
    e4.place(x=300, y=257)
    les = IntVar()
    les.set(0)
    le = Label(
        f1,
        text="5. german black forest cake",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    le.place(x=0, y=300)
    e5 = Entry(f1, textvariable=les)
    e5.place(x=300, y=307)
    lfs = IntVar()
    lfs.set(0)
    lf = Label(
        f1,
        text="6. frozen icecream cookies",
        font="times 18 bold",
        bg="black",
        fg="orange",
    )
    lf.place(x=0, y=350)
    e6 = Entry(f1, textvariable=lfs)
    e6.place(x=300, y=357)
    lgs = IntVar()
    lgs.set(0)
    lg = Label(
        f1, text="7. nut brownies", font="times 18 bold", bg="black", fg="orange"
    )
    lg.place(x=0, y=400)
    e7 = Entry(f1, textvariable=lgs)
    e7.place(x=300, y=407)
    lhs = IntVar()
    lhs.set(0)
    lh = Label(f1, text="8. ice cream", font="times 18 bold", bg="black", fg="orange")
    lh.place(x=0, y=450)
    e8 = Entry(f1, textvariable=lhs)
    e8.place(x=300, y=457)
    b1 = Button(
        f1, text="add", bg="grey", width=15, height=1, font=13, command=addb, fg="gold"
    )
    b1.place(relx=0.03, rely=0.85)
    lj = Label(f1, text="TOTAL COST:", font=10, bg="black", fg="gold")
    lj.place(relx=0.46, rely=0.853)
    lks = IntVar()
    lk = Label(f1, textvariable=lks, font=7, bg="black", fg="gold")
    lk.place(relx=0.8, rely=0.853)
    b2 = Button(
        f1, text="next", bg="light blue", command=nextb, height=1, width=13, font=13
    )
    b2.place(relx=0.048, rely=0.92)
    ini()


def nextb():
    # making a window for the
    t = Toplevel(r)
    t.geometry("500x500")
    t.title("confirmation page")
    t.configure(background="black")
    # back button function
    def back():
        t.destroy()
        import home

    # next button function
    def next():
        t.destroy()
        r.destroy()
        import address

    # widgets for the confirmation page
    Tops = Frame(t, width=1350, height=100, bd=12, bg="black")
    Tops.pack(side=TOP)
    lblTitle = Label(
        Tops, text="Please confirm your order", font=13, bg="black", fg="gold"
    )
    lblTitle.grid(row=0, column=0)
    bot = Frame(
        t, width=1350, height=650, bd=12, relief="raise", bg="black", borderwidth=3
    )
    bot.pack(side=TOP)
    f1 = Frame(
        bot, width=450, height=650, bd=12, bg="black", borderwidth=2, relief="raise"
    )
    f1.pack(side=LEFT, anchor=W)
    f2 = Frame(
        bot, width=450, height=650, bd=12, bg="black", borderwidth=2, relief="raise"
    )
    f2.pack(side=RIGHT)
    t1 = c1.connect(host="localhost", user="root", password="namit", database="food")
    c2 = t1.cursor()
    la = Label(f1, text="ITEMS", font=20, bg="black", fg="gold")
    la.pack(side="top")
    lq = Label(f2, text="QUANTITY", font=20, bg="black", fg="gold")
    lq.pack(side="top")
    # retreving the values of selected items
    # preparing required lists
    mas = []
    mai = []
    resnme = []
    resqunt = []
    x = ["meals", "starters", "beverages", "bandd"]
    y = ["name", "quant"]
    for i in range(0, len(x)):
        m = "select name from %s where quant>0;" % (x[i])
        c2.execute(m)
        resnme.append(c2.fetchall())
        m1 = "select quant from %s where quant>0" % (x[i])
        c2.execute(m1)
        resqunt.append(c2.fetchall())
    for i in range(0, len(resnme)):
        for j in range(0, len(resnme[i])):
            mas.append(resnme[i][j][0])
            mai.append(resqunt[i][j][0])
    # placing required widgets
    b1 = Button(
        t,
        text="back",
        command=back,
        bg="grey",
        activeforeground="grey",
        foreground="gold",
        font="underline",
        activebackground="darkgrey",
    )
    b1.place(relx=0, rely=0.92)
    lv3 = StringVar()
    lv3.set("hi")
    l3 = Label(Tops, textvariable=lv3, bg="black", fg="light grey", font=12)
    l3.grid(row=0, column=1)
    b2 = Button(
        t,
        text="NEXT",
        command=next,
        bg="grey",
        font=16,
        fg="gold",
        activebackground="black",
        activeforeground="gold",
    )
    b2.place(relx=0.86, rely=0.9153)
    for v in mas:
        b = v
        Label(f1, text=b, bg="black", fg="gold", width=20).pack()
    for v1 in mai:
        b1 = v1
        Label(f2, text=b1, bg="black", fg="gold", width=20).pack()
    # function for displaying values in the starting of page
    def ini1():
        # preparing variable for the total amount
        vari = msu + ssu + bsu + bdsu
        lv1.set(vari)
        con1 = t1.cursor()
        sqi = "use specific_user"
        sqi1 = "select name from log;"
        con1.execute(sqi)
        con1.execute(sqi1)
        ri = con1.fetchone()
        ri1 = str(ri[0]).title()
        lv3.set(ri1)

    # rest of the widgets
    lv1 = IntVar()
    lv1.set(0)
    l1 = Label(t, textvariable=lv1, font=20, bg="black", fg="red")
    l1.place(relx=0.6, rely=0.915)
    lt = Label(t, text="Total amount=", font=20, bg="black", fg="red")
    lt.place(relx=0.3, rely=0.915)
    ini1()


# widgets of home page
font1 = c.Font(size=15, weight="bold")
font2 = c.Font(size=20, weight="bold", slant="italic")
font3 = c.Font(size=1, weight="bold")
un = Label(r, text="MENU", font="arial 20 underline italic bold", bg="black", fg="red")
un.place(relx=0.5, rely=0)
B1 = Button(r, text="", bg="gold", fg="red", command=meals, font=30)
B1.place(relx=0, rely=0.13)
L1 = Label(r, text="MEALS", foreground="red", background="black", font=font1)
L1.place(relx=0.05, rely=0.13)
B2 = Button(r, bg="gold", fg="red", text="", command=starters, font=15)
B2.place(relx=0.96, rely=0.23)
l2 = Label(r, text="STARTERS", foreground="red", background="black", font=font1)
l2.place(relx=0.64, rely=0.23)
B3 = Button(r, text="", bg="gold", fg="red", command=beverages, font=15)
B3.place(relx=0, rely=0.33)
l3 = Label(r, text="BEVERAGES", foreground="red", background="black", font=font1)
l3.place(relx=0.05, rely=0.33)
B4 = Button(r, bg="gold", fg="red", text="", command=dandb, font=15)
B4.place(relx=0.96, rely=0.44)
L4 = Label(
    r, text="DESERTS AND BAKED", foreground="red", background="black", font=font1
)
L4.place(relx=0.38, rely=0.44)
B5 = Button(
    r,
    bg="black",
    fg="red",
    text="PROCEED",
    command=nextb,
    font=15,
    activebackground="dark blue",
    activeforeground="gold",
)
B5.place(relx=0.7, rely=0.87)
B6 = Button(
    r,
    bg="black",
    fg="red",
    text="LOG OUT",
    command=logout,
    activebackground="black",
    activeforeground="gold",
    font=15,
)
B6.place(relx=0.03, rely=0.871)
l6v = StringVar()
l6v.set("hi")
l6 = Label(r, textvariable=l6v, background="black", fg="gold", font=1)
l6.place(relx=0.25, rely=0)
l7 = Label(r, text="Welcome", background="black", fg="gold", font=1)
l7.place(relx=0, rely=0)
ini()
r.mainloop()
