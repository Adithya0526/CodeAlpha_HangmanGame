import random 
guess_elements=['omen','python','visual','game','computer']
lives=6
guess_word=random.choice(guess_elements)
guess_list=list('_'*len(guess_word))  
#print('You have', lives, 'lives.')
print('The word to guess is:', '_' * len(guess_word))
while lives>0:
    print('You have', lives, 'lives.')
    # print('The word to guess is:', '_' * len(guess_word))
    guess_letter=input('Guess a letter: ')
    if guess_letter in guess_word:  
        if guess_letter in guess_list:
            print("You have already enterred this letter now choose another letter ")
            continue                          
        else :
            print('Good guess!')                                  
        # Display the current state of the word               
        for i in range(len(guess_word)):
            if guess_word[i] == guess_letter :
                guess_list[i] = guess_letter
                print(guess_list)         
        print()
           
    else:
        print('Wrong guess try again!')
        lives-=1
    if '_' not in guess_list:
        print('Congratulations! You guessed the word:', guess_word)
        break
if lives==0:
    print('You lost! The word was:',guess_word)
        