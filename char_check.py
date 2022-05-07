user_phrase = input()
counter = 0

check_char = str(user_phrase[0])
check_phrase = str(user_phrase[2:])

for char in range(len(check_phrase)):
    if check_char == check_phrase[char]:
        counter += 1

if counter == 1:
    print(counter, check_char)
else:
    print(counter, check_char + "'s")
