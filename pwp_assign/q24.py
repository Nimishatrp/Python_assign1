n1 = int(input("Enter a number- "))
n2 = int(input("enter second number- "))
op = input("Enter an operator (+,-,/,*)- ")
if (op=='+'):
    sum = n1+n2
    print("The sum is- ",sum)
elif (op=='-'):
    dif= n2-n1
    print("The diffrence is- ",dif) 
elif (op =='*'):
    pro =  n1*n2
    print("The product is- ",pro)     
elif (op=='/'):
    div = n1/n2
    print("THe division is- ",div)
else:
    print("Please enter a valid function.")    