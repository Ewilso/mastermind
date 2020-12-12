from multiprocessing import Process
from itertools import product

def scorer(s, guess, pegs):
    out = []
    for i in range(len(s)):
        score = []
        for j in range(len(guess)):
            # Checks for right in right place
            #print(guess[j], s[i][j])
            if guess[j] == s[i][j]:
                score.append("B")
            else:
                # Otherwise checks for right in the wrong place. Only does the rest of the string to avoid duplication
                for k in range(j + 1,len(guess)):
                    if guess[k] == s[i][j]:
                        score.append("W")
                for k in range(j - 1):
                    if guess[k] == s[i][j]:
                        score.append("W")
        # Generates list
        if score != pegs:
            out.append(s[i])
    return out

def minimax(s, pegs):
    min = []
    for i in range(len(s)):
        # Calculates minimum no. possiblities removed
        eliminate = 0
        for j in range(len(s)):
            for k in range(len(pegs)):
                score = len(scorer(s, s[i], pegs[k]))
                if score < eliminate:
                    eliminate = score
        min.append([s[i], eliminate])

    guess = ""
    max = 0
    # Finds the max of the min
    for i in range(len(min) - 1, -1, -1):
        current = len(s) - min[i][1]
        if current > max:
            guess = min[i][0]
            max = current
    return guess

def guess(response, s, pegs, new_guess):
    # Formatting input from string to list
    sliced = []
    for char in response:
        sliced.append(char.upper())

    # Win clause
    if sliced == ["B","B","B","B"]:
        return 0

    # Gets rid of bad choices
    remove = scorer(s, new_guess, sliced)
    for i in range(len(remove)):
        s.remove(remove[i])
    print(len(s))

# Generate possiblities
s = []
tuples = product(["1", "2", "3", "4", "5", "6"], repeat=4)
for i in tuples:
    s.append(list(i))

# Generate peg combos
pegs = []
with open('pegs') as file:
    for line in file:
        line = line.replace('\n', '')
        pegs.append([line])

new_guess = ["1","1","2","2"]
print("My first guess is", new_guess)
for i in range(6):
    response = input("What's your response: ")
    print(new_guess)
    guess(response, s, pegs, new_guess)
    new_guess = minimax(s, pegs)
    print(new_guess, "is my next guess.")
