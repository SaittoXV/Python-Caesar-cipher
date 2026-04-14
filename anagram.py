first_message = input('Enter your first word: ')
second_message = input('Enter your second word: ')

sort_fist = sorted(first_message.lower()) 
sort_second = sorted(second_message.lower()) 

if ''.join(sort_fist) == ''.join(sort_second):
    print('Anagram')
else:
    print('Not anagram')