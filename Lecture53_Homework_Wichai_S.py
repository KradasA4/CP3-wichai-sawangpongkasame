def vatCalculate(totalprice):
    result = totalprice*1.07
    return result
totalprice = float(input ("Price: "))
print ('%.2f'%(vatCalculate(totalprice)))
