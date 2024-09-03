# game state: Grayed Letters (a.), Letters in Wrong Spot (a?), Correct Letters (a+)
#             Guesses are seperated by spaces

# Have access to 58,000 english words

import random

def load_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return words


def choose_word(words):
    return random.choice(words)


def provide_feedback(secret_word, guess):
    feedback = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            feedback.append('+')
        elif guess[i] in secret_word:
            feedback.append('?')
        else:
            feedback.append('.')
    return ''.join(feedback)


def filter_words(words, guess, feedback):
    filtered_words = []
    for word in words:
        match = True
        for i, char in enumerate(guess):
            if feedback[i] == '+':
                if word[i] != char:
                    match = False
                    break
            elif feedback[i] == '?':
                if char not in word or word[i] == char:
                    match = False
                    break
            elif feedback[i] == '.':
                if char in word:
                    match = False
                    break
        if match:
            filtered_words.append(word)
    return filtered_words


def main():

    # get list of all possible guesses
    words = load_words('words.txt')
    
    # instructions
    print("Please enter what you know about the game. Add a '.' after incorrect words, a '?' after letters in the wrong place, and a '+' after correct words.")
    
    # all words are possible at first
    possible_words = words[:] 

    userInput = input("Enter what you know (e to exit): ").strip().lower()
    while (userInput != "e"):
        
        # make sure user follows correct format
        if (len(userInput) != 10 and userInput != "e"):
            print("Make sure you follow the required format.")
        
        # seperate symbols and letters
        guess = []
        feedback = []
        for i in range(10):
            if (i % 2 != 0): feedback.append(userInput[i])
            else: guess.append(userInput[i])

        # update possible words
        possible_words = filter_words(possible_words, guess, feedback)
        if (possible_words != []): print(choose_word(possible_words))
        else: print("No possible guesses in word list!")

        # get user info for next
        userInput = input("Enter what you know (e to exit): ").strip().lower()


if __name__ == "__main__":
    main()
