#שאלה מספר 5
input_str = input("Enter new String")
output = ""
old = ""

for i in input_str:
    if i not in old:
        counter = input_str.count(i)
        output = output + "'" + i + "':" + str(counter) + ", "
        old += i

print(output[:-2])