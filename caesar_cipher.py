user_message = input("Enter your message: ")
user_shift = int(input("Enter your encyption number: "))
encripted = []
upper_shift = 32

for char in user_message:
    if char.isalpha():
        is_upper = char.isupper() 
        char = char.lower()
        sum_shift = ord(char) + user_shift 
        if sum_shift > ord('z'):
            shift_number = ord('`') + (sum_shift - ord('z'))
        else:
            shift_number = ord(char) + user_shift
        if is_upper: shift_number = shift_number - upper_shift
        encripted.append(chr(shift_number))
    else:
        encripted.append(char)
        continue
print("Caesar Cipher: ",''.join(encripted))


# list slicing -> array[start:end:step]