func = input("Do you want to check for suffix or prefix? ")
str1 = input("Enter word- ")
str2 = input("Enter suffix/prefix- ")
if (func=='suffix'):
    print(str1.endswith(str2))
if (func=='prefix'):
    print(str1.startswith(str2))    