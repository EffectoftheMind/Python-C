input_month = input()
input_day = int(input())

if input_month == 'March':
    if (input_day > 0) and (input_day <= 20):
        print("Winter")
    elif (input_day >= 21) and (input_day <= 31):
        print("Spring")
    else:
        print("Invalid")
elif input_month == 'April':
    if (input_day > 0) and (input_day <= 30):
        print("Spring")
    else:
        print("Invalid")
elif input_month == 'May':
    if (input_day > 0) and (input_day <= 31):
        print("Spring")
    else:
        print("Invalid")
elif input_month == 'June':
    if (input_day > 0) and (input_day <= 20):
        print('Spring')
    elif (input_day >= 21) and (input_day <= 30):
        print('Summer')
    else:
        print("Invalid")
elif input_month == 'July':
    if (input_day > 0) and (input_day <= 31):
        print('Summer')
elif input_month == 'August':
    if (input_day > 0) and (input_day <= 31):
        print('Summer')
    else:
        print("Invalid")
elif input_month == 'September':
    if (input_day > 0) and (input_day <= 21):
        print('Summer')
    elif (input_day >= 22) and (input_day <= 30):
        print('Autumn')
    else:
        print("Invalid")
elif input_month == 'October':
    if (input_day > 0) and (input_day <= 31):
        print('Autumn')
    else:
        print("Invalid")
elif input_month == 'November':
    if (input_day > 0) and (input_day <= 30):
        print('Autumn')
    else:
        print("Invalid")
elif input_month == 'December':
    if (input_day > 0) and (input_day <= 20):
        print('Autumn')
    elif (input_day >= 21) and (input_day <= 31):
        print('Winter')
    else:
        print("Invalid")
elif input_month == 'January':
    if (input_day > 0) and (input_day <= 31):
        print('Winter')
    else:
        print("Invalid")
elif input_month == 'February':
    if (input_day > 0) and (input_day <=29):
        print('Winter')
    else:
        print("Invalid")
else:
    print('Invalid')
