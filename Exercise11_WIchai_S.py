round = int(input("stories of the pyramid: "))
for x in range(round):
    space = " "*(round-(x+1))
    print(space+(("*"*x)+("*"*(x+1))))

#round = int(input("stories of the pyramid: "))
#for x in range(round):
#    space = " "*(round-(x+1))
#    print(space+("*"*(x+(x+1))))

'''
round = int(input("stories of the pyramid: "))
for x in range(round):
    space = " "*(round-(x+1))
    print(space+("*"*(2*x+1)))
'''

'''
round = int(input("stories of the pyramid: "))
for x in range(round):
       print((" "*(round-(x+1)))+("*"*x)+("*"*(x+1)))
'''

#case study from a classmate
'''
number = int(input("Enter your number :"))
for x in range(number):
    tab = " " * (number - x)
    star = "*" * ((2*x) + 1)
    result = tab + star
    print(result)
'''