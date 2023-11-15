#שאלה מספר 3
Name = input("Enter your name")
print(Name.upper())

upper = ""
NAME=Name.upper()
for i in NAME:
    upper = upper + str(ord(i)) + "@"
print(upper[:-1])

print(Name.lower())

lower = ""
name = Name.lower()
for i in name:
    lower = lower + str(ord(i)) + "@"
print(lower[:-1])
