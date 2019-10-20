from tkinter import *
from tkinter.font import Font

MainWindow = Tk()
myFont = Font(family='cordia new', size=14, weight='bold')

labelHeight = Label(MainWindow,text = "ส่วนสูง (cm.)",font = myFont).grid(row=0,column=0)
textBoxHeight = Entry(MainWindow).grid(row=0,column=1)
labelWeight = Label(MainWindow,text = "น้ำหนัก (Kg.)",font = myFont).grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
print(type(textBoxHeight))
print(type(textBoxWeight))
print(type(textBoxWeight.get()))
textBoxWeight.grid(row=1,column=1)
calculationButton = Button(MainWindow, text = "คำนวณ", font = myFont).grid(row=2)
MainWindow.mainloop()
