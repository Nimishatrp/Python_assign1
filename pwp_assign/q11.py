n = int(input("enter number of terms in fibonacci series- "))
p = 0
q=1
cntr = 0
while(cntr<n):
    print(p)
    nth = p +q
    p=q
    q=nth
    cntr+=1