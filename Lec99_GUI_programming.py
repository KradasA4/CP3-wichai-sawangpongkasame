from tkinter import *
from tkinter.font import Font

def leftClickButton(event):
    kgWeight = float(textBoxWeight.get())                       #ดึงค่าใน textBowWeight มาใช้ พร้อมแปลงเป็น float
    mHeight = float(textBoxHeight.get()) / 100
    BMI = float("%.2f" % (kgWeight / (mHeight**2)))
    if BMI > 30.0:
        BMIresult = "คุณอ้วนมาก"
    elif BMI >= 25.0 < 30.0:
        BMIresult = "คุณอ้วน"
    elif BMI >= 23.0 < 25.0:
        BMIresult = "คุณน้ำหนักเกิน"
    elif BMI >= 18.6 < 23.0:
        BMIresult = "คุณน้ำหนักปกติ"
    else:
        BMIresult = "คุณผอมเกินไป"
    labelResult.configure(text = f"BMI = {BMI} {BMIresult}")


MainWindow = Tk()
myFont = Font(family='cordia new', size=14, weight='bold')

labelHeight = Label(MainWindow,text = "ส่วนสูง (cm.)",font = myFont)
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
labelWeight = Label(MainWindow,text = "น้ำหนัก (Kg.)",font = myFont)
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
#textBoxHeight = Entry(MainWindow).grid(row=0,column=1)             #NoneType   เป็นการเซ็ตค่าในตัวแปรเลย
#textBoxWeight = Entry(MainWindow)                                  #Type tkinter.Entry
#print(type(textBoxWeight.get()))                                   #Type str
textBoxHeight.grid(row=0,column=1)                          #เรียก method มาตั้งค่าทีหลัง
textBoxWeight.grid(row=1,column=1)
calculationButton = Button(MainWindow, text = "คำนวณ BMI", font = myFont)
calculationButton.bind('<Button-1>', leftClickButton)
calculationButton.grid(row=2, column=0)
labelResult = Label(MainWindow, text = "ผลลัพธ์", font = myFont)
labelResult.grid(row=2, column=1)

MainWindow.mainloop()
