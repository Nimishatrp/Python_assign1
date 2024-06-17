lst = []
n = int(input("Enter number of elements in list- "))
for i in range(0,n):
    a = int(input("enter element- "))
    lst.append(a)
print("minimum value- ",min(lst))
print("maximum value- ",max(lst))