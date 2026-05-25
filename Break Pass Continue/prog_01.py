#break 
#Loop ko turant rok deta hai.Socho loop chal raha hai 1–10 tak, lekin hum bol dein 5 pe ruk jao → break.
for i in range(1, 11):
    if i == 5:
        break

    print(i)

#continue
#Loop ke current iteration ko skip kar deta hai aur next iteration pe chala jata hai
for i in range(1, 6):

    if i == 3:
        continue

    print(i)

#pass
for i in range(5):

    if i == 3:
        pass

    print(i)    