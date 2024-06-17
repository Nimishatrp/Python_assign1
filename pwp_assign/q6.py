f= input("enter the adress of the file with .txt extension- ")
file1=open(f,'r')
line=file1.readline()
while(line!=""):
    print(line)
    line=file1.readline()
file1.close()    