def addNumber(x,y):             #plus
    print(x+y)
def subtractNumber(x,y):        #minus
    print(x-y)
def multiplyNumber(x,y):        #multiply
    print(x*y)
def divideNumber(x,y):          #divide
    print(int(x/y))

result = "wrong"
while result == "wrong":
    x = int(input("first number: "))
    y = int(input("second number: "))
    mark = input("math operation: ")
    if mark == "+":
        result=addNumber(x,y)
    elif mark == "-":
        result=subtractNumber(x,y)
    elif mark == "*":
        result=multiplyNumber(x,y)
    elif mark == "/":
        result=divideNumber(x,y)
    else:
        result="wrong"
        print("wrong mathematical operation mark, please try again")