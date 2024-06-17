a = input("Enter a word- ")
b = input("enter second word- ")
if(sorted(a) == sorted(b)):
    print("anagrams")
else:
    print("not anagrams")