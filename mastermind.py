import itertools
import sys

def scorer(guess, response):
    out = []
    for i in range(len(s)):
        score = ""
        matching = len(set(guess) & set(s[i]))
        pegs = sum(1 for v1, v2 in zip(guess,s[i]) if v1 == v2)
        for j in range(pegs):
            score += "B"
        for j in range(matching - pegs):
            score += "W"

        # Creates list of those that don't match
        if score != response:
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
    if response == ["BBBB"]:
        sys.exit()

    # Gets rid of bad choices
    remove = scorer(new_guess, response)
    for i in range(len(remove)):
        s.remove(remove[i])
    print(len(s))

# Genberate guess combos
global s
s = []
tuples = itertools.product(["1", "2", "3", "4", "5", "6"], repeat=4)
for i in tuples:
    s.append(list(i))

# Generate peg combos
global pegs
pegs = []
with open('pegs') as file:
    for line in file:
        line = line.replace('\n', '')
        pegs.append(line)

new_guess = ["1","1","2","2"]
print("My first guess is", new_guess)
for i in range(10):
    response = input("What's your response: ")
    guess(response, new_guess)
    new_guess = minimax()
    print(new_guess, "is my next guess.")
