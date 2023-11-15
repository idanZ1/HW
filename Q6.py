#שאלה מספר 6
my_string = input("Enter new String")
ans = True
str = "" #הכרזת משתנה חדש שיכיל את הסטרינג ללא הרווחים

for i in my_string:
    if (i != " "): # לופ שפועל רק שהאות היא לא רווח ומכניס אותה למשתנה החדש
        str = str + i
str =str.lower() #הופך את הסטרינג לאותיות קטנות

for x in range(int(len(str) / 2)):#לופ העובד על חצי מהסטרינג משום שמשווים את הראשון לאחרון...
    if (str[x] != str[0-(x+1)]):#משווה את הראשון (x) למקום של המספר השלילי של x פחות אחד
        ans = False
print(ans)