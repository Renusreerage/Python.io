import tkinter
from tkinter import *
import database
root=Tk()


root.geometry("600x500")
root.title("Registration")
lblHeading=Label(root,text="Registration",font=('impact',40),fg='white',bg='blue')
lblHeading.place(x=550,y=200)

sUserName=StringVar()
sCourse=StringVar()
sPaymentStatus=StringVar()
#1
lblValue1=Label(root,text="UserName ")
lblValue1.place(x=550,y=300)
txtValue1=Entry(root,textvariable=sUserName)
txtValue1.place(x=650,y=300)
#2
lblValue2=Label(root,text="course ")
lblValue2.place(x=550,y=350)
dropdown=OptionMenu(root,sCourse,'Bsc','B.tech','B.com')
dropdown.place(x=650,y=350)
#3
lblValue3=Label(root,text="PaymentStatus ")
lblValue3.place(x=550,y=400)
dropdown=OptionMenu(root,sPaymentStatus,'yes','no')
dropdown.place(x=650,y=400)

def Login():
    username=sUserName.get()
    course=sCourse.get()
    paymentstatus=sPaymentStatus.get()
    if database.login(username,course,paymentstatus):
        print("Registration successfully")
    else:
        print("Invalid username and course and paymentstatus")
        
#button
btnadd=Button(root,text="submit",command=Login,bg="pink")
btnadd.place(x=650,y=450)

