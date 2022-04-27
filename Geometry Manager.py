from tkinter import *

window = Tk()
window.title("The Geometry Manager")
window.geometry("500x400+20+10")

#Simple calculator

lbl1 = Label(window,text="Standard Calculator")
lbl1.grid(row = 1,column = 1)

lbl2 = Label(window,text="Input the 1st Number:")
lbl2.grid(row=2,column=0)

lbl3 = Label(window,text="Input the 2nd Number:")
lbl3.grid(row=3,column=0)

entry3 = Entry(window)
entry3.grid(row=2,column=1,padx=4)

entry4 = Entry(window)
entry4.grid(row=3, column=1,padx=4)

lbl4 = Label(window, text='Choose among the operators',justify="left",bg="yellow")
lbl4.grid(row=4,column=0)

btn1=Button(window,text="Add",width=10)
btn1.grid(row=5,column=0)

def add(self):
    self.entry.delete(0, 'end')
    number1 = int(self.entry.get())
    number2 = int(self.entry.get())
    answer = number1 + number2
    self.entry.insert(END, str(answer))

btn2=Button(window,text="Subtract",width=10)
btn2.grid(row=5,column=1,sticky=W)

def subtract(self):
    self.entry.delete(0, 'end')
    number1 = int(self.entry.get())
    number2 = int(self.entry.get())
    answer = number1 - number2
    self.entry.insert(END, str(answer))

btn3=Button(window,text="Multiply",width=10)
btn3.grid(row=5,column=2,sticky=W)

def multiply(self):
    self.entry.delete(0, 'end')
    number1 = int(self.entry.get())
    number2 = int(self.entry.get())
    answer = number1 * number2
    self.entry.insert(END, str(answer))

btn4=Button(window,text="Divide",width=10)
btn4.grid(row=5,column=3,padx=5,sticky=E)

def div(self, event):
    self.entry.delete(0, 'end')
    number1 = int(self.entry.get())
    number2 = int(self.entry.get())
    answer = number1 / number2
    self.entry.insert(END, str(answer))

lbl5 = Label(window,text = "Answer")
lbl5.grid(row=6,column = 0)

entry5 = Entry(window)
entry5.grid(row=6, column = 1)

window.mainloop()
