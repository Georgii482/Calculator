from tkinter import*
tk=Tk()
def d():
    global a,b
    a=float(l.get())
    b="+"
    l.delete(0,END)
def da():
    global a,b
    a=float(l.get())
    b="*"
    l.delete(0,END)
def das():
    global a,b
    a=float(l.get())
    b="-"
    l.delete(0,END)
def dasd():
    global a,b
    a=float(l.get())
    b="/"
    l.delete(0,END)
def Equal_click():
    global a,b
    c=float(l.get())
    l.delete(0,END)
    if b=="+":
        l.insert(END,a+c)
    if b=="/":
        l.insert(END,a/c)
    if b=="-":
        l.insert(END,a-c)
    if b=="*":
        l.insert(END,a*c)
def click():
     l.delete(0,END)
def bc():
     l.insert(END,".")
def abc():
     l.insert(END,"0")
def a2():
     l.insert(END,"2")
def a3():
     l.insert(END,"3")
def a4():
     l.insert(END,"4")
def a5():
     l.insert(END,"5")
def a6():
     l.insert(END,"6")
def a7():
     l.insert(END,"7")
def a8():
     l.insert(END,"8")
def a9():
     l.insert(END,"9")
def a10():
     l.insert(END,"1")
tk.geometry("300x400")
tk.title("Калькулятор")
l=Entry(justify="right",font="Arial 16")
b=Button(text="C",font="16",command=click)
b2=Button(text="=",font="16",command=Equal_click)
b3=Button(text="0",font="16",command=abc)
b4=Button(text=".",font="16",command=bc)
b5=Button(text="+",font="16",command=d)
b6=Button(text="7",font="16",command=a7)
b7=Button(text="8",font="16",command=a8)
b8=Button(text="9",font="16",command=a9)
b9=Button(text="/",font="16",command=dasd)
b10=Button(text="4",font="16",command=a4)
b11=Button(text="5",font="16",command=a5)
b12=Button(text="6",font="16",command=a6)
b13=Button(text="*",font="16",command=da)
b14=Button(text="1",font="16",command=a10)
b15=Button(text="2",font="16",command=a2)
b16=Button(text="3",font="16",command=a3)
b17=Button(text="-",font="16",command=das)
b17.pack()
b16.pack()
b15.pack()
b14.pack()
b13.pack()
b12.pack()
b11.pack()
b10.pack()
b9.pack()
b8.pack()
b7.pack()
b6.pack()
b5.pack()
b4.pack()
b3.pack()
b2.pack()
b.pack()
l.pack()
b17.place(x=240,y=250,height=40,width=40)
b16.place(x=166,y=250,height=40,width=40)
b15.place(x=93,y=250,height=40,width=40)
b14.place(x=20,y=250,height=40,width=40)
b13.place(x=240,y=190,height=40,width=40)
b12.place(x=166,y=190,height=40,width=40)
b11.place(x=93,y=190,height=40,width=40)
b10.place(x=20,y=190,height=40,width=40)
b9.place(x=240,y=130,height=40,width=40)
b8.place(x=166,y=130,height=40,width=40)
b7.place(x=93,y=130,height=40,width=40)
b6.place(x=20,y=130,height=40,width=40)
b5.place(x=240,y=320,height=40,width=40)
b4.place(x=166,y=320,width=40,height=40)
b3.place(x=20,y=320,width=100,height=40)
b2.place(x=180,y=70,width=100,height=40)
b.place(x=20,y=70,width=100,height=40)
l.place(x=20,y=20,width=260,height=30)
tk.mainloop()
