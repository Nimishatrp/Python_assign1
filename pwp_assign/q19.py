str1 = input("Enter a string with punctuation- ")
punc = '''!@#$%^&*(),./';[]-=_+{}:"<>?`~'''
for ele in str1:
    if ele in punc:
        str1 = str1.replace(ele,"")
print(str1)        