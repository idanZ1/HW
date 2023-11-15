#שאלה מספר 1
str = input("Enter your String")
num = int(input("Enter your Number"))
if len(str) > num:
    print(str[num])
else:
    print("String isn't long enough")
