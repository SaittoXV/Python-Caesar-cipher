user_message = input("Enter your message: ")
user_shift = int(input("Enter your encyption number: "))
encripted = []

for char in user_message:
    if char.isalpha():
        is_upper = char.isupper() 
        char = char.lower()
        sum_shift = ord(char) + user_shift 
        if sum_shift > 122:
            shift_number = 96 + (sum_shift - 122)
        else:
            shift_number = ord(char) + user_shift
        if is_upper: shift_number = shift_number - 32
        encripted.append(chr(shift_number))
    else:
        encripted.append(char)
        continue
print("Caesar Cipher: ",''.join(encripted))