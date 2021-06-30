from tkinter import *
from PIL import Image,ImageTk
import os
import tkinter.messagebox as tm
import fileinput

def maine():
    f1=Frame(background="black")
    l= Label(f1,bg="black")
    l.pack(pady=5)
    b1= Button(f1,text="Create Account",bg="black",fg="white",font="AdobeFanHeitiStdB 14 bold",borderwidth=0.1,command=writeAccount).pack(padx=50)
    l= Label(f1,bg="black")
    l.pack(pady=5)
    b1= Button(f1,text="Deposit Money",bg="black",fg="white",font="AdobeFanHeitiStdB 14 bold",borderwidth=0.1,command=lambda:forwhat(3)).pack(padx=80)
    l= Label(f1,bg="black")
    l.pack(pady=5)
    b1= Button(f1,text="Withdraw Money",bg="black",fg="white",font="AdobeFanHeitiStdB 14 bold",borderwidth=0.1,command=lambda:forwhat(2)).pack(padx=80)
    l= Label(f1,bg="black")
    l.pack(pady=5)
    b1= Button(f1,text="Balance Enquiry",bg="black",fg="white",font="AdobeFanHeitiStdB 14 bold",borderwidth=0.1,command=lambda:forwhat(1)).pack(padx=80)
    l= Label(f1,bg="black")
    l.pack(pady=5)
    b1= Button(f1,text="All Account Holder List",bg="black",fg="white",font="AdobeFanHeitiStdB 14 bold",borderwidth=0.1,command=allholder).pack(padx=80)
    l= Label(f1,bg="black")
    l.pack(pady=5)
    b1= Button(f1,text="Close An Account",bg="black",fg="white",font="AdobeFanHeitiStdB 14 bold",borderwidth=0.1).pack(padx=80)
    l= Label(f1,bg="black")
    l.pack(pady=5)
    b1= Button(f1,text="Modify An Account",bg="black",fg="white",font="AdobeFanHeitiStdB 14 bold",borderwidth=0.1).pack(padx=80)
    l= Label(f1,bg="black")
    l.pack(pady=5)
    b1= Button(f1,text="Exit",bg="black",fg="white",font="AdobeFanHeitiStdB 14 bold",borderwidth=0.1,command=quit).pack(padx=80)
    l= Label(f1,bg="black")
    l.pack(pady=1)
    f1.place(x=450,y=230,width=480,height=555)
    b1= Label(text="Back",bg="black",fg="black",font="AdobeFanHeitiStdB 14 bold").place(x=10,y=10,width=200,height=200)

    
def writeAccount():
    account = GUI()
    account.createAccount()

def writeAccountsFile(**kwarg) : 
    
    fi = open("accounts.txt","a")
    fi.write(str(kwarg["number"])+"-" + kwarg["name"] +"-" + str(kwarg["deposit"])+"-" + kwarg["type"]+"\n")
    fi.close()
    maine()

def details(n):
    f=open("accounts.txt","r")
    f1=Frame()
    f1.config(background="black")
    f2=Frame(f1,background="black")
    while True:
        x=0
        st=f.readline()
        p=st.split("-")
        if not st:
            break
        elif int(p[0])==n:
            x=1
            print("heelo")
            break
    # if x==0:
    #     k=Label(f1,text="          "+p[2],fg="white",bg="black",font="AdobeFanHeitiStdB 14 bold").pack(side = TOP,padx=5,pady=5)
    #     # k=Label(f2,text="           no record found",fg="red",bg="black",font="AdobeFanHeitiStdB 14 bold").pack(side = TOP,padx=5)
    #     l=Label(f2,bg="black").pack(side=TOP)
    
    # else:

    f2.pack(side=BOTTOM)
    k1=Button(f2,text="   main menu   ",fg="white",bg="black",font="AdobeFanHeitiStdB 14 bold",command=maine).pack(side = TOP,padx=5)
    f1.place(x=550,y=600)

def increase(n):
    fi=open("accounts.txt","r")
    f1=Frame(background="black")
    while True:
         s=fi.readline()
         p=s.split("-")
         if not s:
             break
         if p[0]==str(n):
              x=Label(f1,text=p[1],fg="white",bg="black",font="AdobeFanHeitiStdB 14 bold").pack(padx=80)
              l= Label(f1,bg="black")
              l.pack(pady=1)

    f1.place(x=450,y=230,width=480,height=555)

def decrease(n):
    pass


def allholder():
    fi=open("accounts.txt","r")
    f1=Frame(background="black")
    while True:
        s=fi.readline()
        if not s:
            break
        p=s.split("-")
        x=Label(f1,text=p[1],fg="white",bg="black",font="AdobeFanHeitiStdB 14 bold").pack(padx=80)
        l= Label(f1,bg="black")
        l.pack(pady=1)

    f1.place(x=450,y=230,width=480,height=555)
    b1= Button(text="Back",bg="ivory3",fg="black",font="AdobeFanHeitiStdB 14 bold",borderwidth=0.1,command=maine).place(x=10,y=10)

def forwhat(i):
    de=IntVar()
    f1=Frame(a)
    f1.config(background="black")
    f=Frame(f1)
    f.config(background="black")
    k=Label(f,text="Account number",fg="white",bg="black",font="AdobeFanHeitiStdB 14 bold").pack(side=LEFT,padx=5,pady=5)
    E5=Entry(f,textvariable=de).pack(side=LEFT,pady=10)
    l= Label(f,bg="black")
    l.pack(pady=5)
    # f.place(x=600,y=500)
    f.pack(side=TOP,pady=15)

    if i==1:
        f=Frame(f1)
        t=de.get()
        f.config(background="black")
        b1= Button(f1,text="Submit",bg="black",fg="white",font="AdobeFanHeitiStdB 14 bold",borderwidth=2,relief=SUNKEN,command=lambda:details(t))
        # b1.place(x=200,y=370)
        b1.pack(pady=20)
        f.pack(side=BOTTOM,pady=5)

    elif i==2:
        f=Frame(f1)
        t=de.get()
        f.config(background="black")
        b1= Button(f1,text="Submit",bg="black",fg="white",font="AdobeFanHeitiStdB 14 bold",borderwidth=2,relief=SUNKEN,command=lambda:decrease(t))
        # b1.place(x=200,y=370)
        b1.pack(pady=20)
        f.pack(side=BOTTOM,pady=5)
        
    else:
        f=Frame(f1)
        t=de.get()
        f.config(background="black")
        b1= Button(f1,text="Submit",bg="black",fg="white",font="AdobeFanHeitiStdB 14 bold",borderwidth=2,relief=SUNKEN,command=lambda:increase(t))
        # b1.place(x=200,y=370)
        b1.pack(pady=20)
        f.pack(side=BOTTOM,pady=5)

    f1.place(x=450,y=230,width=480,height=555)
    b1= Button(text="Back",bg="ivory3",fg="black",font="AdobeFanHeitiStdB 14 bold",borderwidth=0.1,command=maine).place(x=10,y=10)


a=Tk()
a.geometry("1400x900")
p=Image.open("Logo_MyBank_positive.png")
p=p.resize((350,190),Image.ANTIALIAS)
t=ImageTk.PhotoImage(p)
l=Label(a,image=t,borderwidth=0)
l.pack()
l=Label(a,bg="black")
l.pack(pady=10)
a.config(bg="black")
maine()

class GUI():
    def __init__(self):
        self.detail={}
        self.nam=StringVar()
        self.typ=StringVar()
        self.num=IntVar()
        self.dep=IntVar()
        self.f=StringVar()
        self.t=""
    
    def createAccount(self):
        f1=Frame(a)
        
        k=Label(f1,bg="black").pack(side=TOP,padx=5,pady=5)
        f1.config(background="black")
        f=Frame(f1)
        f.config(background="black")
        k=Label(f,text="Enter Name",fg="white",bg="black",font="AdobeFanHeitiStdB 14 bold").pack(side=LEFT,padx=5,pady=5)
        E1=Entry(f,textvariable=self.nam).pack(side=LEFT)
        l= Label(f,bg="black")
        l.pack(pady=5)
        # f.place(x=600,y=400)
        f.pack(side=TOP,pady=15)

        f=Frame(f1)
        f.config(background="black")
        k=Label(f,text="Type of Acount [Saving / Current]",fg="white",bg="black",font="AdobeFanHeitiStdB 14 bold").pack(side=LEFT,padx=5,pady=5)
        E2=Entry(f,textvariable=self.typ).pack(side=LEFT)
        l= Label(f,bg="black")
        l.pack(pady=5)
        # f.place(x=600,y=450)
        f.pack(side=TOP,pady=15)

        f=Frame(f1)
        f.config(background="black")
        k=Label(f,text="Account number",fg="white",bg="black",font="AdobeFanHeitiStdB 14 bold").pack(side=LEFT,padx=5,pady=5)
        E3=Entry(f,textvariable=self.num).pack(side=LEFT,pady=10)
        l= Label(f,bg="black")
        l.pack(pady=5)
        # f.place(x=600,y=500)
        f.pack(side=TOP,pady=15)

        f=Frame(f1)
        f.config(background="black")
        k=Label(f,text="Deposit",fg="white",bg="black",font="AdobeFanHeitiStdB 14 bold").pack(side=LEFT,padx=5,pady=5)
        E4=Entry(f,textvariable=self.dep).pack(side=LEFT)
        l= Label(f,bg="black")
        l.pack(pady=5)
        # f.place(x=600,y=550)
        f.pack(side=TOP,pady=15)

        f=Frame(f1)
        f.config(background="black")
        b1= Button(f1,text="Submit",bg="black",fg="white",font="AdobeFanHeitiStdB 14 bold",borderwidth=2,relief=SUNKEN,command=self.printf)
        # b1.place(x=200,y=370)
        b1.pack(pady=20)
        f.pack(side=BOTTOM,pady=5)

        f=Frame(f1)
        f.config(background="black")
        k=Label(f,text="please fill details carefully!!",fg="red",bg="ivory3",font="AdobeFanHeitiStdB 14 bold").pack(side=LEFT,padx=5,pady=5)
        l= Label(f,bg="black")
        l.pack(pady=5)
        f.pack(side=TOP,pady=15)

        f1.place(x=450,y=230,width=480,height=555)
        b1= Button(text="Back",bg="ivory3",fg="black",font="AdobeFanHeitiStdB 14 bold",borderwidth=0.1,command=maine).place(x=10,y=10)

    def printf(self):
        self.detail={"type":self.typ.get(),"name":self.nam.get(),"deposit":self.dep.get(),"number":self.num.get()}
        tm.showinfo("Account Created",message=("Account successfully created and credited by %s "%self.detail["deposit"]))
        writeAccountsFile(**self.detail)

    

a.mainloop()
