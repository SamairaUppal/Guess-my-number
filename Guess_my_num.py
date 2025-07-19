correct_number = int(input())
num_guesses = 0
while True:
    print('Guess the number:')
    guess = int(input())
    if isinstance(guess, int) == True and 1<=guess<=100:
        num_guesses +=1
        if guess == correct_number:
            print('correct')
            print('Number of guesses:',num_guesses)
            break
        elif guess< correct_number:
            print('go up')
            continue
        else:
            print('go down')
            continue
    else:
        print('invalid guess')
        continue
        