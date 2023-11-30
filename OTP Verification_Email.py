from tkinter import *
from tkinter import ttk
import smtplib as sm
import math,random
digits = "0123456789"
OTP = ""
for i in range(4) :
    OTP += digits[math.floor(random.random() * 10)]
def generate():
        smtp_object=sm.SMTP('smtp.gmail.com',587)
        smtp_object.ehlo()
        smtp_object.starttls()
        email="bhavanach650@gmail.com"
        password="dpkgvbvkqpsdjjzf"
        smtp_object.login(email,password)
        from_address=email
        mail=e1.get()
        subject="your otp to login "
        msg="Subject: "+subject+'\n'+OTP
        smtp_object.sendmail(from_address,mail,msg)
        smtp_object.quit()
        
def verify():
    
        n=e2.get()    
        print("n",n)
        print("OTP",OTP)
        print(str(n)==OTP)
        if str(n)==OTP:
                top= Toplevel(w)
                top.configure(bg="green")
                top.geometry("250x250")
                top.title("Login")
                Label(top, text= "Login successful", font=('Mistral 18 bold'),bg="green",fg="white").place(x=80,y=80)
        else:
                top= Toplevel(w)
                top.configure(bg="red")
                top.geometry("300x250")
                top.title("Login")
                Label(top, text= "wrong details", font=('Mistral 18 bold'),bg="red",fg="white").place(x=90,y=80)
               

        
w=Tk()

w.geometry("1000x1000")
w.title("Login PAGE")
w.configure(bg="skyblue")
Label(w,bd=4,text="Email",font=("Times New Roman", 20),width=5,bg="skyblue",fg="black").grid(row=0,column=0)
Label(w,bd=4,text="OTP",font=("Times New Roman", 20),width=5,bg="skyblue",fg="black").grid(row=1,column=0)
e1=Entry(w,width=23,fg="black")
e2=Entry(w,width=23,fg="black")
e1.grid(row=0,column=2)
e2.grid(row=1,column=2)
b=Button(w,bd=4,text="GENERATE OTP",command=generate)
b.grid(row=4,column=0)
b2=Button(w,bd=4,text="VERIFY OTP",command=verify)
b2.grid(row=4,column=2)
w.mainloop()
