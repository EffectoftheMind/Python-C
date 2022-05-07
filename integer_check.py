user_string = input()
user_string = list(user_string)

num_list = ['1', '2', '3', '4' ,'5', '6', '7', '8', '9', '0']
counter = 0

isInt = True

for char in user_string:
    if char not in num_list:
        isInt = False

if isInt == True:
    print('yes')
else:
    print('no')
