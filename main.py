user_message = input("Enter your message: ")
user_shift = int(input("Enter your encyption number: "))
encripted = []
cap_state = "upper"

for char in user_message:
    if char.isalpha():
        if not char.isupper(): cap_state = "lower"
        char = char.lower()
        sum_shift = ord(char) + user_shift 
        if sum_shift > 122:
            shift_number = 96 + (sum_shift - 122)
        else:
            shift_number = ord(char) + user_shift
        if cap_state == "upper": shift_number = shift_number - 32
        encripted.append(chr(shift_number))
        cap_state = "upper"
    else:
        encripted.append(char)
        continue
print(''.join(encripted))
