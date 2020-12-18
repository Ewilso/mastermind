from itertools import product
import sys
import threading

# TODO: Rework scoring function
def scorer(guess, response):
    out = []
    for i in range(len(s)):
        score = []
        for j in range(len(guess)):
            # Checks for right in right place
            if guess[j] == s[i][j]:
                score.append("B")

        for j in range(len(guess)):
            # Otherwise checks for right in the wrong place
            for k in range(j + 1,len(guess)):
                if guess[k] == s[i][j] and len(score) < 4:
                    score.append("W")
            for k in range(j - 1):
                if guess[k] == s[i][j] and len(score) < 4:
                    score.append("W")
        # Generates list
        if score != response:
            print(guess, score, s[i])
            out.append(s[i])
    return out

def minimax():
    min = []
    for i in range(len(s)):
        # Calculates minimum no. possiblities removed
        eliminate = 0
        for k in range(len(pegs)):
            score = len(scorer(s[i], pegs[k]))
            if score < eliminate:
                eliminate = score
        min.append([s[i], eliminate])

    guess = ""
    max = 0
    # Finds the max of the min
    for i in range(len(min)):
        current = len(s) - min[i][1]
        if current > max:
            guess = min[i][0]
            max = current
    return guess

def guess(response, new_guess):
    # Formatting input from string to list
    sliced = []
    for char in response:
        sliced.append(char.upper())
    sliced.sort()
    # Win clause
    if sliced == ["B","B","B","B"]:
        sys.exit()

    # Gets rid of bad choices
    remove = scorer(new_guess, sliced)
    for i in range(len(remove)):
        s.remove(remove[i])
    print(len(s))

# Generate peg combos
global pegs
pegs = []
with open('pegs') as file:
    for line in file:
        line = line.replace('\n', '')
        pegs.append([line])

new_guess = ["1","1","2","2"]
print("My first guess is", new_guess)
for i in range(10):
    global s
    s = []
    tuples = product(["1", "2", "3", "4", "5", "6"], repeat=4)
    for i in tuples:
        s.append(list(i))
    print(len(s))
    response = input("What's your response: ")
    guess(response, new_guess)
    new_guess = minimax()
    print(new_guess, "is my next guess.")
