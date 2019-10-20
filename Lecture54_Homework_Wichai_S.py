def login():
    username = input("enter username: ")
    password = input("enter password: ")
    if username == "admin" and password == "1234":
        print("permission granted")
        return showMenu()
    else:
        print("access denied: incorrect username or password")
        return login()                                          #user/pass ผิด ล็อกอินใหม่
def showMenu():
    print("-----MY SHOP-----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return selectMenu()
def selectMenu():                                               #แสดงผลลัพธ์การคำนวณในฟังก์ชันนี้
    choice = int(input("select services: "))
    if choice == 1:
        print (vatCalculate(float (input("Price: "))))          #print ค่าจากฟังก์ชัน vatCalculate
    elif choice == 2:
        print (priceCalculate())                                #print ค่าจากฟังก์ชัน priceCalculate
    else:
        print ("Error: incorrect input")
        return selectMenu()
def vatCalculate(totalprice):
    vat = 7
    result = '%.2f' % (totalprice + (totalprice*vat/100))
    return result
def priceCalculate():
    price1 = int(input("First product price: "))
    price2 = int(input("Second product price: "))
    return vatCalculate(price1 + price2)

login()                                                         #เรียกใช้โปรแกรมคำนวณภาษีมูลค่าเพิ่ม


#Login
#Show Menu
#Select Menu
#Vat
#Price