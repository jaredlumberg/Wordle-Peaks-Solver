import json
import string
import statistics
import math

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

        # print(letters_difference) # DEBUG
        # print(min(letters_difference, key=letters_difference.get)) # DEBUG
        optimal_word += min(letters_difference, key=letters_difference.get)

    return optimal_word

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

def main():
    # Add words into list
    word_list = None

    with open("dictionary-filtered.json", "r") as read_file:
        word_list = json.load(read_file)

    while True:
        # Find the optimal word for this list
        if len(word_list) == 1:
            print("Solved!!! Solution is " + word_list[0] + ".")
            quit()

        ideal = ideal_word(word_list)
        # print(ideal) # DEBUG

        # Find the closest word in this list to the optimal word
        closest = closest_word(ideal, word_list)
        # print(closest) # DEBUG
        print("Guess the word: " + closest)

        if closest == ideal:
            print("Solved!!! Solution was " + closest + ".")
            quit()

        # Filter out word list based on guess results
        print("Enter results of guess:")
        print("B = before, A = After, $ = correct")
        result = input()
        print("\n")

        if result == "$$$$$":
            print("Solved!!! Solution was " + closest + ".")
            quit()
        
        word_list = filter(closest, result, word_list)

        # Repeat until answer is found

if __name__ == "__main__":
    main()
