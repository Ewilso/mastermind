from multiprocessing import Process
def scorer(s, guess, pegs):
    out = []
    for i in range(len(s)):
        score = []
        for j in range(len(guess)):
            # Checks for right in right place
            if guess[j] == s[i][j]:
                score.append("B")
            else:
                # Otherwise checks for right in the wrong place. Only does the rest of the string to avoid duplication
                for k in range(j, len(guess)):
                    if guess[k] == s[i][j]:
                        score.append("W")
        # Generates list
        if score != pegs:
            out.append(s[i])

        return out

def minimax(s, pegs):
    min = []
    for i in range(1111,6667):
        # Calculates minimum no. possiblities removed
        eliminate = 1297
        for j in range(len(s)):
            for k in range(len(pegs)):
                score = len(scorer(s, str(i), pegs[k]))
                if score < eliminate:
                    eliminate = score
        min.append([str(i),eliminate])

    guess = ""
    max = 0
    # Finds the max of the min
    for i in range(len(min)):
        score = len(s) - min[i][1]
        if score > max:
            guess = min[i][0]
    return guess

def guess(response):
    # Generate possiblities
    s = []
    for i in range(1111,6667):
        s.append(str(i))

    # Generate peg combos
    pegs = []
    with open('pegs') as file:
        for line in file:
            line = line.replace('\n', '')
            pegs.append([line])
    print(pegs)

    # Formatting input from string to list
    sliced = []
    for char in response:
        sliced.append(char.upper())

    if sliced == ["B","B","B","B"]:
        return 0

    # Gets rid of bad choices
    remove = scorer(s, "1122", sliced)
    for i in range(len(remove)):
        s.remove(remove[i])

    print(minimax(s, pegs), "is my next guess.")

response = input("My guess is 1122, what's your response: ")
guess(response)
