inputRound = int(input("How many number to sum up?: "))
sum = 0
for x in range(inputRound):
    inputNumber = int(input("Number"+str(x+1)+":"))
    sum += inputNumber
print("result: ",sum)