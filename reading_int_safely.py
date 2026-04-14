def read_int(prompt, min, max):
    try:
        user_input = int(input(prompt))
        if user_input < max and user_input > min:
            return print("The number is:", user_input)
        else:
            return print('Error: The value is not within the permitted range ({0}..{1})'.format(min,max))
    except:
        return print('Error: wrong input')
    


read_int("Enter a number from -10 to 10: ", -10, 10)