lines =[]
while True:
    line = input("Enter some text- ")
    if line:
        lines.append(line)
    else:
        break 
ip='\n'.join(lines)       
print("Your text is-",ip)