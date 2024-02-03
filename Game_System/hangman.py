from random import randint

LINE = '-'*60

def play_hangman():
    
    words_list = []
    # open file storing hangman words and store in a list
    with open("game_lib/hangman_words.txt",'r') as file:
        for line in file:
            word = line.strip('\n')
            words_list.append(word)
    
    # choose a word from the list
    number_of_words = len(words_list)
    index = randint(0,number_of_words-1)
    
    game_word = words_list[index].upper()

    # display instructions to user
    print("Hangman!\n"\
        + LINE +\
        "\nYour goal is to find the word."\
        "\nTo do this you need to guess letters of the word."
        "\nYou are only allowed 10 incorrect guessed."\
        "\nYour score is based on the number of incorrect guesses.\n"\
        + LINE)

    # display an underscore for each letter in the word
    
    print("Guess the word: \n")
    
    display_word = []
    for char in game_word:
        if char == " ":
            display_word.append("/")
        else:
            display_word.append("_ ")
    
    displayed_string = "".join(display_word)
    
    
    print(displayed_string + "\n" + LINE)
    
    # stores used letters
    used_letters = []
    
    # User selects a letter
    remaining_guesses= 10
    
    while remaining_guesses > 0:
        print("Number of Guesses:", remaining_guesses)
        
        letter = (input("\nSelect a letter: ")).upper()
        
        # check input is only one character
        if len(letter) != 1:
            print("Error! Only type in one letter. Try again.\n"\
                + LINE)
        # check input is alphabetical
        elif letter.isalpha() == False:
            print("Error! You need to type in a letter. Try again.\n"\
                + LINE)
        # check letter hasn't already been used
        elif letter in used_letters:
            print("Error! You have already guessed that letter. Try again.\n")
        
        # check if the letter is in the word
        if letter in game_word:
            for i, char in enumerate(game_word):
                if char == letter:
                    display_word[i] = letter
                elif char == " ":
                    display_word[i] = "/"
                    
            displayed_string = " ".join(display_word)
            print(displayed_string)
            
            if "_" not in displayed_string:
                print(LINE + "\nYou Win!"\
                    "\nThe correct word was", game_word,"\n"\
                        + LINE)
                break
        else:
            print("Incorrect guess!")
            remaining_guesses -= 1
        
        used_letters.append(letter)
    
    if remaining_guesses == 0:
        print(LINE + "\nYou Lose!"\
                    "\nThe correct word was", game_word,"\n"\
                        + LINE)
        score = 0
    else:
        score = ((remaining_guesses)/10)*100
        print(f"{LINE}\nYour score: {score}\n{LINE}")
    
    return score