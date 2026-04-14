user_input = (input('Enter a date (YYYYMMDD): '))

while len(user_input) > 1:
    sum_input = 0
    for number in user_input:
        sum_input += int(number)
    user_input = str(sum_input)

print('The output is ', user_input)