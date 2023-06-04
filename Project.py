from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image,ImageTk
from tkinter import ttk
conn=sqlite3.connect("Bank.db")
conn1=sqlite3.connect("BankM.db")
cur1=conn1.cursor()
cur=conn.cursor()
#cur.execute("CREATE TABLE Login(UserName TEXT PRIMARY KEY,PassWord TEXT)")
#cur1.execute("CREATE TABLE Account(FirstName TEXT,LastName TEXT,AccountNumber Text PRIMARY KEY,UPIID TEXT,DOB TEXT,BALANCE INTEGER)")
def delet():
    def dele():
        def reset1():
            e31.delete(0,'end')
            e32.delete(0,'end')
        try:
            Acc=e31.get()
            up=e32.get()
            bdet=cur1.execute("SELECT * from Account where AccountNumber=?",(Acc,))
            a=cur1.fetchall()
            if Acc=="" or up=="":
                messagebox.showinfo("Status","All Fields are Require!!",parent=root8)
            elif not a:
                messagebox.showinfo("Status","Account not created",parent=root8)
            else:
                for i in a:
                    if Acc==i[2]and up==i[3]:
                        cur1.execute("DELETE from Account where AccountNumber=?",(Acc,))
                        conn1.commit()
                        messagebox.showinfo("Status","Account is deleted",parent=root8)
                        reset1()
                    else:
                         messagebox.showinfo("Status","Invalid AccountNumber or UPI ID!!!!",parent=root8)
        except sqlite3.Error as er:
            messagebox.showinfo("Status",er,parent=root8)
    
    root8=Tk()
    root8.geometry("700x400")
    root8.title("ToDelete Account")
    ph=Image.open("bank1.jpg")
    re=ph.resize((800,600))
    im=ImageTk.PhotoImage(re,master=root8)
    lab=Label(root8,image=im)
    lab.place(x=0,y=0)
    lab.image=im
    img=ImageTk.PhotoImage(Image.open("bank3.jpg").resize((200,200)),master=root8)
    Label(root8,image=img).place(x=20,y=90)
    Label.image=img
    Label(root8,text="Account Number",font=("Times",16)).place(x=300,y=70)
    e31=Entry(root8)
    e31.place(x=500,y=70,height=18,width=180)
    Label(root8,text="UPI ID",font=("Times",16)).place(x=300,y=140)
    e32=Entry(root8)
    e32.place(x=500,y=140,height=18,width=180)
    b10=Button(root8,text="Delete",command=dele,font=("Times",16)).place(x=440,y=230)
    
    
def details():
    def show():        
            root6=Tk()
            root6.title("Account Details")
            root6.configure(bg="skyblue")
            root6.geometry("800x600")
            accn=e29.get()
            cur1.execute("SELECT * from Account where AccountNumber=?",(accn,))
            det=cur1.fetchall()
            e17=Label(root6,text="FullName",font=("Times",30),bg="skyblue")
            e17.place(x=40,y=50)
            e18=Label(root6,text="LastName",font=("Times",30),bg="skyblue")
            e18.place(x=40,y=120)
            e19=Label(root6,text="AccountNumber",font=("Times",30),bg="skyblue")
            e19.place(x=40,y=190)
            e20=Label(root6,text="UPIID",font=("Times",30),bg="skyblue")
            e20.place(x=40,y=260)
            e21=Label(root6,text="DOB",font=("Times",30),bg="skyblue")
            e21.place(x=40,y=330)
            e22=Label(root6,text="Balance",font=("Times",30),bg="skyblue")
            e22.place(x=40,y=400)
            for i in det:
                e23=Label(root6,text=i[0],font=("Times",30),bg="skyblue")
                e23.place(x=400,y=50)
                e24=Label(root6,text=i[1],font=("Times",30),bg="skyblue")
                e24.place(x=400,y=120)
                e25=Label(root6,text=i[2],font=("Times",30),bg="skyblue")
                e25.place(x=400,y=190)
                e26=Label(root6,text=i[3],font=("Times",30),bg="skyblue")
                e26.place(x=400,y=260)
                e27=Label(root6,text=i[4],font=("Times",30),bg="skyblue")
                e27.place(x=400,y=330)
                e28=Label(root6,text=i[5],font=("Times",30),bg="skyblue")
                e28.place(x=400,y=400)
    def detail2():
        try:
            Acc=e29.get()
            up=e30.get()
            bdet=cur1.execute("SELECT * from Account where AccountNumber=?",(Acc,))
            a=cur1.fetchall()
            if Acc=="" or up=="":
                messagebox.showinfo("Status","All Fields are Require!!",parent=root7)
            elif not a:
                messagebox.showinfo("Status","Account not created",parent=root7)
            else:
                for i in a:
                    if Acc==i[2]and up==i[3]:
                        show()
                    else:
                         messagebox.showinfo("Status","Invalid AccountNumber or UPI ID!!!!",parent=root7)

        except sqlite3.Error as er:
             messagebox.showinfo("Status",er,parent=root7)
                    
        
    root7=Tk()
    root7.geometry("700x400")
    root7.title("Account details")
    ph=Image.open("bank1.jpg")
    re=ph.resize((800,600))
    im=ImageTk.PhotoImage(re,master=root7)
    lab=Label(root7,image=im)
    lab.place(x=0,y=0)
    lab.image=im
    img=ImageTk.PhotoImage(Image.open("bank3.jpg").resize((200,200)),master=root7)
    Label(root7,image=img).place(x=20,y=90)
    Label.image=img
    Label(root7,text="Account Number",font=("Times",16)).place(x=300,y=70)
    e29=Entry(root7)
    e29.place(x=500,y=70,height=18,width=180)
    Label(root7,text="UPI ID",font=("Times",16)).place(x=300,y=140)
    e30=Entry(root7)
    e30.place(x=500,y=140,height=18,width=180)
    b11=Button(root7,text="Submit",command=detail2,font=("Times",16)).place(x=440,y=230)
   
def reset2():
    e1.delete(0,'end')
    e2.delete(0,'end')
def insertReg():
    try:
        name=e1.get()
        passw=e2.get()
        cur.execute("INSERT INTO Login VALUES(?,?)",(name,passw))
        conn.commit()
        messagebox.showinfo("Status","Register successfully!!!!")
    except sqlite3.Error as er:
        messagebox.showinfo("Status",er)

def Login():
    try:
        name=e1.get ()
        passw=e2.get()
        res=cur.execute("SELECT * from Login where UserName=?",(name,))
        a=cur.fetchall()
        if name=="" or passw=="":
             messagebox.showinfo("Status","All Fields are required")
        elif not a:
            messagebox.showinfo("Status","Not register yet!!!!")
        else:
            for i in a:
                if name==i[0]and passw==i[1]:
                    messagebox.showinfo("Status","Login successfully!!!!")
                    reset2()
                    Bank()
                else:
                     messagebox.showinfo("Status","Invalid user name or password!!!!")
                    
                    
    except sqlite3.Error as er:
        messagebox.showinfo("Status",er)
def check():
    def chk():
        try:
            Acc=e15.get()
            up=e16.get()
            checkbal=cur1.execute("SELECT * from Account where AccountNumber=?",(Acc,))
            a=cur1.fetchall()
            if Acc=="" or up=="":
                messagebox.showinfo("Status","All Fields are Require!!",parent=root5)
            elif not a:
                messagebox.showinfo("Status","Account not created",parent=root5)
            else:
                for i in a:
                    if Acc==i[2] and up==i[3]:
                        messagebox.showinfo("Status","Balance= "+str(i[5]),parent=root5)
                    else:
                        messagebox.showinfo("Status","Invalid AccountNumber or UPI ID!!",parent=root5)
        except sqlite3.Error as er:
             messagebox.showinfo("Status",er,parent=root5)
                
                
    root5=Tk()
    root5.geometry("700x400")
    root5.title("Check Balance")
    ph=Image.open("bank1.jpg")
    re=ph.resize((800,600))
    im=ImageTk.PhotoImage(re,master=root5)
    lab=Label(root5,image=im)
    lab.place(x=0,y=0)
    lab.image=im
    img=ImageTk.PhotoImage(Image.open("bank3.jpg").resize((200,200)),master=root5)
    Label(root5,image=img).place(x=20,y=90)
    Label.image=img
    Label(root5,text="Account Number",font=("Times",16)).place(x=300,y=70)
    e15=Entry(root5)
    e15.place(x=500,y=70,height=18,width=180)
    Label(root5,text="UPI ID",font=("Times",16)).place(x=300,y=140)
    e16=Entry(root5)
    e16.place(x=500,y=140,height=18,width=180)
    b10=Button(root5,text="Check",command=chk,font=("Times",16)).place(x=440,y=230)
    
def withdraw():
    def reset1():
        e12.delete(0,'end')
        e13.delete(0,'end')
        e14.delete(0,'end')
    def withd():
        try:
            Acc=e12.get()
            up=e13.get()
            Amo=e14.get()
            withdr=cur1.execute("SELECT * from Account where AccountNumber=?",(Acc,))
            a=cur1.fetchall()
            if Acc=="" or up=="":
                messagebox.showinfo("Status","All Fields are Require!!",parent=root4)
            elif not a:
                messagebox.showinfo("Status","Account not created",parent=root4)
            else:
                for i in a:
                    if Acc==i[2] and up==i[3]:
                        if int(Amo)>i[5]:
                             messagebox.showinfo("Status","Insufficient Balance !!!!",parent=root4)
                        else:
                            bal=i[5]-int(Amo)
                            cur1.execute("UPDATE Account SET BALANCE=? where AccountNumber=?",(bal,Acc,))
                            conn1.commit()
                            messagebox.showinfo("Status","WithDraw Successfully !!!!",parent=root4)
                            reset1()
                    else:
                        messagebox.showinfo("Status","Invalid AccountNumber or UPI ID!!",parent=root4)
                        
        except sqlite3.Error as er:
            messagebox.showinfo("Status",er,parent=root4)
    root4=Tk()
    root4.geometry("700x400")
    root4.title("WithDraw Amount")
    ph=Image.open("bank1.jpg")
    re=ph.resize((800,600))
    im=ImageTk.PhotoImage(re,master=root4)
    lab=Label(root4,image=im)
    lab.place(x=0,y=0)
    lab.image=im
    img=ImageTk.PhotoImage(Image.open("bank3.jpg").resize((200,200)),master=root4)
    Label(root4,image=img).place(x=20,y=90)
    Label.image=img
    Label(root4,text="Account Number",font=("Times",16)).place(x=300,y=50)
    e12=Entry(root4)
    e12.place(x=500,y=50,height=18,width=180)
    Label(root4,text="UPI ID",font=("Times",16)).place(x=300,y=110)
    e13=Entry(root4)
    e13.place(x=500,y=110,height=18,width=180)
    Label(root4,text="Amount",font=("Times",16)).place(x=300,y=170)
    e14=Entry(root4)
    e14.place(x=500,y=170,height=18,width=180)
    b9=Button(root4,text="WithDraw",command=withd,font=("Times",16)).place(x=440,y=230)
    
def deposit():
    def reset1():
        e9.delete(0,'end')
        e10.delete(0,'end')
        e11.delete(0,'end')
    def dep():
        try:
            Acc=e9.get()
            up=e10.get()
            Amo=e11.get()
            depo=cur1.execute("SELECT * from Account where AccountNumber=?",(Acc,))
            a=cur1.fetchall()
            if Acc=="" or up=="":
                messagebox.showinfo("Status","All Fields are Require!!",parent=root3)
            elif not a:
                messagebox.showinfo("Status","Account not created",parent=root3)
            else:
                for i in a:
                    if Acc==i[2] and up==i[3]:
                        bal=int(Amo)+i[5]
                        cur1.execute("UPDATE Account SET BALANCE=? where AccountNumber=?",(bal,Acc,))
                        messagebox.showinfo("Status","Deposit Successfully !!!!",parent=root3)
                        reset1()
                        conn1.commit()
                    else:
                        messagebox.showinfo("Status","invalid AccountNumber or UPI ID!!",parent=root3)
        except sqlite3.Error as er:
            messagebox.showinfo("Status",er,parent=root3)
    root3=Tk()
    root3.geometry("700x400")
    root3.title("Deposit Amount")
    ph=Image.open("bank1.jpg")
    re=ph.resize((800,600))
    im=ImageTk.PhotoImage(re,master=root3)
    lab=Label(root3,image=im)
    lab.place(x=0,y=0)
    lab.image=im
    img=ImageTk.PhotoImage(Image.open("bank3.jpg").resize((200,200)),master=root3)
    Label(root3,image=img).place(x=20,y=90)
    Label.image=img
    Label(root3,text="Account Number",font=("Times",16)).place(x=300,y=50)
    e9=Entry(root3)
    e9.place(x=500,y=50,height=18,width=180)
    Label(root3,text="UPI ID",font=("Times",16)).place(x=300,y=110)
    e10=Entry(root3)
    e10.place(x=500,y=110,height=18,width=180)
    Label(root3,text="Amount",font=("Times",16)).place(x=300,y=170)
    e11=Entry(root3)
    e11.place(x=500,y=170,height=18,width=180)
    b8=Button(root3,text="Deposit",command=dep,font=("Times",16)).place(x=440,y=230)
def create():
    def reset1():
        e3.delete(0,'end')
        e4.delete(0,'end')
        e5.delete(0,'end')
        e6.delete(0,'end')
        e7.delete(0,'end')
        e8.delete(0,'end')
    def reset():
        try:
            fname=e3.get()
            lname=e4.get()
            Anumber=e5.get()
            Uid=e6.get()
            Dob=e7.get()
            Bal=e8.get()
            cur1.execute("UPDATE Account SET FirstName=?,LastName=?,AccountNumber=?,UPIID=?,DOB=?,Balance=? where AccountNumber=?",(fname,lname,Anumber,Uid,Dob,Bal,Anumber))
            conn1.commit()
            messagebox.showinfo("Status","Your Account has been Reset",parent=root2)
            reset1()
        except sqlite3.Error as er:
             messagebox.showinfo("Status",er,parent=root2)
        
        
    def insert():
        try:
            fname=e3.get()
            lname=e4.get()
            Anumber=e5.get()
            Uid=e6.get()
            Dob=e7.get()
            Bal=e8.get()
            if fname=="" or lname=="" or Anumber=="" or Uid=="" or Dob=="" or Bal=="":
                messagebox.showinfo("Status","All Fields are Require",parent=root2)
            elif int(Bal) < 3000:
                messagebox.showinfo("Status","Minimum 3000 require",parent=root2)
            else:                
                cur1.execute("INSERT INTO Account VALUES(?,?,?,?,?,?)",(fname,lname,Anumber,Uid,Dob,Bal))
                conn1.commit()
                messagebox.showinfo("Status","Account Created",parent=root2)
                reset1()
        except sqlite3.Error as er:
            messagebox.showinfo("Status",er,parent=root2)
    root2=Tk()
    root2.geometry("800x500")
    root2.title("Create Account")
    ph=Image.open("bank1.jpg")
    re=ph.resize((800,600))
    im=ImageTk.PhotoImage(re,master=root2)
    lab=Label(root2,image=im)
    lab.place(x=0,y=0)
    lab.image=im
    img=ImageTk.PhotoImage(Image.open("bank3.jpg").resize((200,200)),master=root2)
    Label(root2,image=img).place(x=20,y=130)
    Label.image=img
    Label(root2,text="First Name",font=("Times",16)).place(x=300,y=50)
    e3=Entry(root2)
    e3.place(x=500,y=50,height=18,width=180)
    Label(root2,text="Last Name",font=("Times",16)).place(x=300,y=110)
    e4=Entry(root2)
    e4.place(x=500,y=110,height=18,width=180)
    Label(root2,text="Account Number",font=("Times",16)).place(x=300,y=170)
    e5=Entry(root2)
    e5.place(x=500,y=170,height=18,width=180)
    Label(root2,text="UPI ID",font=("Times",16)).place(x=300,y=230)
    e6=Entry(root2)
    e6.place(x=500,y=230,height=18,width=180)
    Label(root2,text="D.O.B",font=("Times",16)).place(x=300,y=290)
    e7=Entry(root2)
    e7.place(x=500,y=290,height=18,width=180)
    Label(root2,text="Balance",font=("Times",16)).place(x=300,y=350)
    e8=Entry(root2)
    e8.place(x=500,y=350,height=18,width=180)
    b6=Button(root2,text="Submit",command=insert,font=("Times",16)).place(x=400,y=410)
    b7=Button(root2,text="Update",command=reset,font=("Times",16)).place(x=550,y=410)
def Bank():
    root1=Tk()
    root1.geometry("800x600")
    root1.title("Bank Management System")
    ph=Image.open("bank2.jpg")
    re=ph.resize((800,600))
    im=ImageTk.PhotoImage(re,master=root1)
    lab=Label(root1,image=im)
    lab.place(x=0,y=0)
    lab.image=im
    b2=Button(root1,text="Create Account",font=("Times",18),command=create).place(x=450,y=80)
    b3=Button(root1,text="Deposit",font=("Times",18),command=deposit).place(x=490,y=160)
    b4=Button(root1,text="WithDraw",font=("Times",18),command=withdraw).place(x=475,y=240)
    b5=Button(root1,text="Check Balance",font=("Times",18),command=check).place(x=450,y=320)
    b11=Button(root1,text="AccDetails",font=("Times",18),command=details).place(x=470,y=400)
    b12=Button(root1,text="DeleteAcc",font=("Times",18),command=delet).place(x=470,y=480)
    
    
root=Tk()
root.geometry("800x600")
root.title("Bank Management Login")
photo=Image.open("login3.png")
resimg=photo.resize((600,600))
img=ImageTk.PhotoImage(resimg)
label=Label(image=img).place(x=0,y=0)
Label(root,text="Login",font=("Times",40),fg="purple").place(x=450,y=80)
Label(root,bg="skyblue",width=200).place(x=0,y=0)
Label(root,text="Please Enter Details",font=("Times",18),bg="skyblue",width=20).pack()
Label(root,text="UserName",font=("Times",20),fg="mediumvioletred").place(x=350,y=200)
e1=Entry(root)
e1.place(x=500,y=210,height=20,width=200)
Label(root,text="PassWord",font=("Times",20),fg="mediumvioletred").place(x=350,y=260)
e2=Entry(root)
e2.place(x=500,y=270,height=20,width=200)
b1=Button(root,text="Login",font=("Times",18),command=Login).place(x=580,y=340)
b1=Button(root,text="Register",font=("Times",18),command=insertReg).place(x=420,y=340)

