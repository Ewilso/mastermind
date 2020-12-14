from itertools import product
import sys
import threading

def scorer(guess, response):
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
        if score != response:
            out.append(s[i])
#        else:
#            print(guess, s[i], score)
    return out

def mulitloop(min):
    for i in range(len(s)):
        # Calculates minimum no. possiblities removed
        eliminate = 0
        for k in range(len(pegs)):
            score = len(scorer(s[i], pegs[k]))
            if score < eliminate:
                eliminate = score
        min.append([s[i], eliminate])

def minimax():
    jobs = []
    min = []
    thread = threading.Thread(target=mulitloop(min))
    jobs.append(thread)

    for j in jobs:
        j.start()
    # Ensure all of the threads have finished
    for j in jobs:
        j.join()

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

    # Win clause
    if sliced == ["B","B","B","B"]:
        sys.exit()

    # Gets rid of bad choices
    remove = scorer(new_guess, sliced)
    for i in range(len(remove)):
        s.remove(remove[i])
    if len(s) == 0:
        print("Program Terminated")
        sys.exit()
    print(len(s))

# Generate possiblities
global s
s = []
tuples = product(["1", "2", "3", "4", "5", "6"], repeat=4)
for i in tuples:
    s.append(list(i))

# Generate peg combos
global pegs
pegs = []
with open('pegs') as file:
    for line in file:
        line = line.replace('\n', '')
        pegs.append([line])

new_guess = ["1","1","2","2"]
print("My first guess is", new_guess)
for i in range(6):
    response = input("What's your response: ")
    guess(response, new_guess)
    new_guess = minimax()
    print(new_guess, "is my next guess.")
