import tkinter
rgn=tkinter.Tk()
a1=tkinter.Label(rgn,text="REGISTRATION FORM")
a1.pack()
c1=tkinter.Label(rgn,text="First Name:")
c1.pack()
b1=tkinter.Entry(rgn)
b1.pack()
c1=tkinter.Label(rgn,text="Last Name:")
c1.pack()
b1=tkinter.Entry(rgn)
b1.pack()
c1=tkinter.Label(rgn,text="father`s Name:")
c1.pack()
b1=tkinter.Entry(rgn)
b1.pack()
c1=tkinter.Label(rgn,text="DOB:")
c1.pack()
b1=tkinter.Entry(rgn)
b1.pack()
c1=tkinter.Label(rgn,text="Address:")
c1.pack()
b1=tkinter.Entry(rgn)
b1.pack()
c1=tkinter.Label(rgn,text="course:")
c1.pack()
b1=tkinter.Listbox(rgn)
b1.insert(1, "Python")
b1.insert(2, "Perl")
b1.insert(3, "C")
b1.insert(4, "PHP")
b1.insert(5, "JSP")
b1.insert(6, "Ruby")
b1.insert(7, "Java")
b1.insert(8, "Advance Excel")
b1.insert(9, "Tally")
b1.insert(10, "Graphics")
b1.pack()
c1=tkinter.Label(rgn,text="Phone no:")
c1.pack()
b1=tkinter.Entry(rgn)
b1.pack()
c1=tkinter.Label(rgn,text="Fees:")
c1.pack()
b1=tkinter.Entry(rgn)
b1.pack()
c1=tkinter.Label(rgn,text="Email ID:")
c1.pack()
b1=tkinter.Entry(rgn)
b1.pack()
d1=tkinter.Button(rgn,text="submit",activebackground="red", activeforeground="blue",bd=20,bg="pink") 
d1.pack()
e1=tkinter.Button(rgn,text="Clear",activebackground="red", activeforeground="blue",bd=20,bg="pink") 
e1.pack()
rgn.mainloop()
