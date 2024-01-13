# libraries
import random
import os

# variables
wanna_continue = 'y'
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']


# methods
def choose_data():
    # read data from file
    try:
        with open("words.txt", "r") as file:
            words = file.read().split()
    except FileNotFoundError:
        print("Error: File 'words.txt' not found.")
        exit()

    # select random word and make hidden_word list
    random_word = list(random.choice(words))
    hidden_word = list('_' * len(random_word))

    return random_word, hidden_word


def ask_and_check(searched_word, hidden_word, stage_pictures):
    # variable for calculate mistakes
    mistakes = 0
    max_mistakes = 6

    os.system('cls' if os.name == 'nt' else 'clear')
    print(''.join(hidden_word))

    # loop to add the next letters
    while mistakes < max_mistakes and '_' in hidden_word:
        if mistakes > 0:
            try:
                print(stage_pictures[mistakes])
            except:
                print('a higher limit than amount of stage pictures has been set')
        user_answer = input('Guess a letter or word: ').lower()

        # breaking loop if user answer is same with word (end game)
        if user_answer == ''.join(searched_word):
            break

        os.system('cls' if os.name == 'nt' else 'clear')
        # checking a letter appears in a word
        if user_answer in searched_word:
            # message if letter was already showed
            if user_answer in hidden_word:
                print('letter is already showed')

            hidden_word = show_letter(hidden_word, user_answer, searched_word)
        else:
            mistakes += 1
        print(''.join(hidden_word))
        print(f'mistake meter: {mistakes}')

    end_of_game(searched_word, mistakes, max_mistakes, stage_pictures)


def show_letter(hidden_word, letter, word):
    for i in range(len(word)):
        if word[i] == letter:
            hidden_word[i] = letter
    return hidden_word


def end_of_game(searched_word, mistakes, mistake_limit, stage_pictures):
    word = ''.join(searched_word)
    os.system('cls' if os.name == 'nt' else 'clear')
    if mistakes < mistake_limit:
        print(f'word: {word}')
        print('CONGRATULATIONS! YOU WIN!')
        print(f'number of mistakes: {mistakes}')
    else:
        print(f'word: {word}')
        print(stage_pictures[-1])
        print('You lose')


# process
while wanna_continue.lower() == 'y':
    selected_word, hidden_word = choose_data()
    ask_and_check(selected_word, hidden_word, stages)
    wanna_continue = input('Do you want to try again? (Type "y" and enter if yes or press Enter if no): ')
