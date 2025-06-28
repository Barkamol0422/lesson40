from tkinter import *
import datetime
root=Tk()
root.title("Sample screen")
root.geometry("400x400")
l1=Label(root, text="Hey there",bg="blue",fg="white",width=150)
l1.pack()
l2=Label(root, text="Full name:",bg="dodgerblue",fg="white")
l2.pack()
e1=Entry(root,width=50)
e1.pack()
def on_click():
    n=e1.get()
    t1.insert(END,n)
b1=Button(root, text="Submit", bg="orange",fg="white",width=10,command=on_click)
b1.pack()
t1=Text(root, width=50,height=30)
t1.pack()
