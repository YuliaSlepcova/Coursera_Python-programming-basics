import  random
number = random.randint(0, 101)

while True:

    answer = input('Enter number ')
    
    if not answer or answer == 'exit':
        break
    
    if not answer.isdigit():
        print('Enter the correct number ')
        continue
    
    user_anser = int(answer)

    if user_anser > number:
        print('Our number is less')
    elif user_anser < number:
        print('Our number is bigger')
    else:
        print('Congratulations! You guessed the number', + number)
        break
