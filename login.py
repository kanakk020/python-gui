from tkinter import *
from button import *

def check1():
    name=e1.get()
    pas=e2.get()
    if name=="123" and pas=="123":
        log.destroy()
        butt()
    else:
        l5=tkinter.Label(log,text="invalid user id and password")
        l5.place(x=90,y=190)
log=tkinter.Tk()
log.resizable(False,False)
log.geometry("300x250")
log.title("Login Form")
l1=tkinter.Label(log,text="Login",font=("Arial 15"))
l1.place(x=120,y=10)
l2=tkinter.Label(log,text="User ID:")
l2.place(x=50,y=50)
e1=tkinter.Entry(log,width=25)
e1.place(x=120,y=50)
l3=tkinter.Label(log,text="Password")
l3.place(x=50,y=90)
e2=tkinter.Entry(log,width=25,show='*')
e2.place(x=120,y=90)
b1=tkinter.Button(log,text="Login",width=15,command=check1)
b1.place(x=50,y=130)
b2=tkinter.Button(log,text="Cancel",width=15, command=log.destroy)
b2.place(x=170,y=130)
l4=tkinter.Label(log,text="Forget Password?")
l4.place(x=120,y=170)
log.mainloop()
