menuList = []                                           #สร้าง list ไว้เก็บข้อมูล
priceList = []
def showInvoice():
    print('My Food'.center(21, '-'))
    for number in range(len(menuList)):               #วนตามจำนวนรอบเท่ากับ ขนาดของ list
        print(menuList[number]+':',priceList[number],"baht")
def showPrice():
    totalPrice = 0
    for price in range(len(priceList)):
        totalPrice = totalPrice + priceList[price]
    print('Total Price:', totalPrice, "baht")

while True:
    menuName = input("Please enter menu: ")
    if menuName.casefold() == 'exit':                #ปรับให้input เป็นตัวพิมพ์เล็กก่อนตรวจสอบ เผื่อผู้ใช้พิมพ์ Exit
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showInvoice()
showPrice()

