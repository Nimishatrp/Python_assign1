def CtoF():
    c = float(input("Enter temprature in celsius- "))
    f=c*(9/5)+32
    print("temprature in fahrenheit is- ",f)
def FtoC():
    f = float(input("Enter temprature in Fahrenheit- "))
    c=  (f-32)*5/9
    print("Temprature in celsius is- ",c)
op = input("Enter a function (C to F or F to C (case sensitive))- ")
if (op=='C to F'):
     CtoF()    
if (op=='F to C'):
    FtoC() 