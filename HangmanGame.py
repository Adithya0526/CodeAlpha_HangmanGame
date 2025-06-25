import random 
guess_elements=['omen','python','visual','game','computer']
lives=6
guess_word=random.choice(guess_elements)
print('You have', lives, 'lives.')
print('The word to guess is:', '_' * len(guess_word))
while lives>0:
    print('You have', lives, 'lives.')
    # print('The word to guess is:', '_' * len(guess_word))
    guess_letter=input('Guess a letter: ')
    if guess_letter in guess_word:                            # first solution is to create a list of '_' then replace it with correct guess 
        print('Good guess!')                                   #then check using if '_' not in the new list is so then display the correct answer and break it 
        # Display the current state of the word 
        for letter in guess_word:
            if letter == guess_letter:
                print(letter, end=' ')
            else:
                print('_', end=' ')
            print()

         # New line after displaying the word
            
    else:
        print('Wrong guess try again!')
        lives-=1
if lives==0:
    print('You lost! The word was:',guess_word)
        