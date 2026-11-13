print('--Program that finds N leading prime numbers---')
n = int(input('Enter N: '))

count = 0        
candidate = 2    

while count < n:
    is_prime = True

    for divisor in range(2, candidate):
        if candidate % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(candidate, end=' ')
        count += 1

    candidate += 1