#שאלה מספר 1
str = input("Enter your String")
num = int(input("Enter your Number"))
if (len(str) > num and num>0):
    print(str[num-1])
else:
    print("String isn't long enough")
