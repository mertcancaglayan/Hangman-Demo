import random

print('Hello, Welcome to Hangman by Jidely')
print('-----------------------------------')


# List of Possible Words
wordDictionary = ["light", "trousers", "screen", "date", "house", "pillow", "grape", "coffee", "python", "lemon",
 "television", "computer", "brown", "movie", "pear", "pineapple", "hello", "strawberry", "motorcycle", "watermelon"]


# Generate a random word

random_word = random.choice(wordDictionary)

for letter in random_word:
    print('-', end=' ')

def print_hangman(wrong):
    if(wrong == 0):
        print('\n+---+')
        print('    |')
        print('    |')
        print('    |')
        print('   ===')
    elif(wrong == 1):
        print('\n+---+')
        print(' O  |')
        print('    |')
        print('    |')
        print('   ===')
    elif(wrong == 2):
        print('\n+---+')
        print(' O  |')
        print(' |  |')
        print('    |')
        print('   ===')
    elif(wrong == 3):
        print('\n+---+')
        print(' O  |')
        print('/|  |')
        print('    |')
        print('   ===')
    elif(wrong == 4):
        print('\n+---+')
        print(' O  |')
        print('/|\ |')
        print('    |')
        print('   ===')
    elif(wrong == 5):
        print('\n+---+')
        print(' O  |')
        print('/|\ |')
        print('/   |')
        print('   ===')
    elif(wrong == 6):
        print('\n+---+')
        print(' O  |')
        print('/|\ |')
        print('/ \ |')
        print('   ===')

    
def print_Word(guessedLetters):
    counter = 0
    rightLetters = 0
    for char in random_word:
        if(char in guessedLetters):
            print(random[counter], end=' ')
            rightLetters+=1
        else:
            print(' ',end=' ')
        counter+=1
    return rightLetters

def printLines():
    print('\r')
    for char in random_word:
        print("\u203E", end=' ')

length_of_word_to_guess = len(random_word)
amounth_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while amounth_of_times_wrong !=6 and current_letters_right != length_of_word_to_guess:
    print('\nLetters guessed so far: ')
    for letter in current_letters_guessed:
        print(letter, end=' ')
    # Prompt user for input
    letterGuessed = input('\nGuess a letter: ')
    if random_word[current_guess_index] == letterGuessed:
        print_hangman(amounth_of_times_wrong)
        # Print word
        current_guess_index +=1
        current_letters_guessed.append(letterGuessed)
        current_letters_right = print_Word(current_letters_guessed)
        printLines()
        #user was wrong
    else:
        amounth_of_times_wrong+=1
        current_letters_guessed.append(letterGuessed)
        #update drawing
        print_hangman(amounth_of_times_wrong)
        #print word
        current_letters_right = print_Word(current_letters_guessed)
        printLines()

print('game over!')