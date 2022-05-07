user_text = input()

char_count = 0

chars = list(user_text)

for entry in range(len(chars)):
    if chars[entry] == ".":
        char_count -= 1
    elif chars[entry] == "!":
        char_count -= 1
    elif chars[entry] == " ":
        char_count -= 1
    elif chars[entry] == ",":
        char_count -= 1
    char_count += 1
    
print(char_count)
