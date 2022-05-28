import json
import string
import statistics
import math

# Find the optimal guess for a list of words
def ideal_word(words):
    optimal_word = ""

    for i in range(5):
        letters_before = dict.fromkeys(string.ascii_lowercase, 0)
        letters_after = dict.fromkeys(string.ascii_lowercase, 0)
        
        for word in words:
            for c in string.ascii_lowercase:
                if word[i] < c:
                    letters_before[c] += 1
                if word[i] > c:
                    letters_after[c] += 1
                else:
                    pass

        letters_difference = {key: abs(letters_before[key] - letters_after.get(key, 0)) for key in letters_before.keys()}
        optimal_word += min(letters_difference, key=letters_difference.get)

    return optimal_word

# Find the closest word in the list to the optimal guess
def closest_word(optimal_word, words):
    best_word = ""
    best_score = math.inf

    for word in words:
        score = 0

        for i in range(5):
            score += abs(ord(word[i]) - ord(optimal_word[i]))
        
        if score < best_score:
            best_score = score
            best_word = word

    return best_word

# Remove all words from the list that can't be the solution
def filter(input, result, words):
    new_list = []

    for word in words:
        wrong_letters = 0
        for i in range(5):
            if result[i] == 'B':
                if ord(word[i]) >= ord(input[i]):
                    wrong_letters += 1
            elif result[i] == 'A':
                if ord(word[i]) <= ord(input[i]):
                    wrong_letters += 1
            elif result[i] == '$':
                if ord(word[i]) != ord(input[i]):
                    wrong_letters += 1
        
        if wrong_letters == 0:
            new_list.append(word)

    return new_list

# Solve Wordle Peaks puzzles
def main():
    # Add words into list from game dictionary
    word_list = None
    with open("dictionary-filtered.json", "r") as read_file:
        word_list = json.load(read_file)

    # Loop until an answer is found
    while True:
        # If there is only one possible word, the puzzle is solved
        if len(word_list) == 1:
            print("Solved!!! Solution is " + word_list[0] + ".")
            quit()

        # Find the ideal word
        ideal = ideal_word(word_list)

        # Find the closest word in the word list to the optimal word
        closest = closest_word(ideal, word_list)

        # Prints the word the player should guess
        print("\n" + "Guess the word: " + closest + "\n")

        # User inputs the result of the guess
        print("KEY: B = before, A = After, $ = correct")
        result = input("Enter results of guess: ")

        # If the player guessed correctly, solving the puzzle
        if result == "$$$$$":
            print("Solved!!! Solution was " + closest + ".")
            quit()
        
        # Filter out all words that can't be the solution   
        word_list = filter(closest, result, word_list)

if __name__ == "__main__":
    main()
