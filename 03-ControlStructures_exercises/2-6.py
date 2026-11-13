number = int(input('Enter a number: '))

if number >= 1:
    print(f'Number {number} is positive')
elif number <= -1:
    print(f'Number {number} is negative')
elif number == 0:
    print('Number is 0')
else:
    print('You typed something wrong')
