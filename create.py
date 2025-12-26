#This program is inspired by the New York Times game "Spelling Bee," go to https://www.nytimes.com/puzzles/spelling-bee to see the real thing.
fin = open('words_all_lengths.txt').readlines()
import random

#This function is what hangles the word creation aspect of the game
def swap(mode: str):
    words_to_guess = []
    #max is the difficulty setting of how many words the user has to get it isn't exactly these values but a range of them
    if mode == "EASY":
        max = 10
    elif mode == "MEDIUM":
        max = 20
    else:
        max = 40
    while len(words_to_guess) < max-5 or len(words_to_guess) > max+10:
        words_to_guess = []
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        t = []
        letters_to_use = []
        #randomly picks 7 letters and removes them to make sure there are no duplicate letters selected
        for i in range(7):
            x = random.choice(letters)
            letters_to_use.append(x)
            letters.remove(x)
            #uses thes 7 letters to curse the words_all_lengths.txt file and store all the possible words made with these random letters
            #if the number of words do not fall within 5 less than max or 10 more of max then 7 new letters are selected untill the condition passes
        for line in fin:
            word = line.strip()
            for i in range(len(word)):
                if word[i] in letters:
                    break
                elif i == (len(word)-1):
                    t.append(word)
        score = 0
        #The NYT game has a center letter that has to be in the word. This is chosen to be the 4th letter generated but it doesn't really matter as it is random
        must_use = letters_to_use[3]
        #curses through the list t to append all words where the center letter is in the word to a new list that is the one the user will be guessing from
        for i in t:
            if must_use in i:
                words_to_guess.append(i)
    print(letters_to_use, "you must use the letter", must_use)
    print("You have up to", len(words_to_guess), "words to guess")
    return words_to_guess

#This function handles the guessing aspect of the game this doesn't really need to be its own function but for the AP CSP create task it needed two functions... so
def guess(words_to_guess: list):
    score = 0
    guess = input("Enter a word to guess or \" I QUIT \" to quit: " )
    while guess.strip() != "I QUIT":
        if guess.strip() in words_to_guess:
            words_to_guess.remove(guess.strip())
            print("You have", len(words_to_guess), "words to guess")
            score += len(guess.strip())
            print("Score: ", score)
        if len(words_to_guess) == 0:
            print("You Win!")
            break
        guess = input("Enter a word to guess or \" I QUIT \" to quit: " )
    print("Your final score is ", score, "The words to guess were", words_to_guess)
   
guess(swap(input("Enter a mode, EASY, MEDIUM, or HARD: ")))




