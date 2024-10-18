# Step1: Import Tkinter File
from tkinter import *


# Step2: GUI Interaction
window=Tk()
window.geometry('500x500')

# Step3: adding inputs

#Entry
e=Entry(window,width=50,borderwidth=5)
e.place(x=0,y=0)
#Buttons
def click(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(num)+str(result))
b=Button(window,text='1',width=10,command=lambda:click(1))
b.place(x=10,y=60)
b=Button(window,text='2',width=10,command=lambda:click(2))
b.place(x=80,y=60)
b=Button(window,text='3',width=10,command=lambda:click(3))
b.place(x=150,y=60)
b=Button(window,text='4',width=10,command=lambda:click(4))
b.place(x=10,y=120)
b=Button(window,text='5',width=10,command=lambda:click(5))
b.place(x=80,y=120)
b=Button(window,text='6',width=10,command=lambda:click(6))
b.place(x=150,y=120)
b=Button(window,text='7',width=10,command=lambda:click(7))
b.place(x=10,y=180)
b=Button(window,text='8',width=10,command=lambda:click(8))
b.place(x=80,y=180)
b=Button(window,text='9',width=10,command=lambda:click(9))
b.place(x=150,y=180)
b=Button(window,text='0',width=10)
b.place(x=10,y=240)
def add():
    n1=e.get()
    global math
    math="addition"
    global i
    i=int(n1)
    e.delete(0,END) # this is to remove the values in entry box and give the result
b=Button(window,text='+',width=10,command=add)
b.place(x=80,y=240)
def sub():
    n1=e.get()
    global math
    math = "subtraction"
    global i
    i=int(n1)
    e.delete(0,END) # this is to remove the values in entry box and give the result
b=Button(window,text='-',width=10, command=sub)
b.place(x=150,y=240)
def mult():
    n1=e.get()
    global math
    math = "multiplication"
    global i
    i=int(n1)
    e.delete(0,END) # this is to remove the values in entry box and give the result
b=Button(window,text='*',width=10, command=mult)
b.place(x=10,y=300)
def div():
    n1=e.get()
    global math
    math = "division"
    global i
    i=int(n1)
    e.delete(0,END) # this is to remove the values in entry box and give the result
b=Button(window,text='/',width=10,command=div)
b.place(x=80,y=300)
def equal():
    n2=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,i+int(n2))
    elif math=="subtraction":
        e.insert(0,i-int(n2))
    elif math=="multiplication":
        e.insert(0,i*int(n2))
    elif math=="division":
        e.insert(0,i//int(n2))

b=Button(window,text='=',width=10,command=equal)
b.place(x=150,y=300)
def clear():
    e.delete(0,END)
b=Button(window,text='clear',width=10, command=clear)
b.place(x=80,y=360)


# Step4: main loop
mainloop()
