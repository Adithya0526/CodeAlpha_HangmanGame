import random 
guess_elements=['omen','python','visual','game','computer']
guess_count=0
guess_word=random.choice(guess_elements)
while guess_count<6:
    guess_letter=input('Guess a letter: ')
    if guess_letter in guess_word:
        print('Correct guess you won the game!')
    else:
        print('Wrong guess try again!')
        guess_count+=1
    if guess_count==6:
        print('You lost! The word was:',guess_word)
        break
