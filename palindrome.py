user_input = input('Enter you message: ')
list_input = user_input.split()
strip_input = "".join(list_input)
if strip_input.lower() == strip_input[::-1].lower():
    print('It\'s a palindrome')
else:
    print('It\'s not a palindrome')