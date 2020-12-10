def cleaner(s, guess, pegs):
    out = []
    for i in range(len(s)):
        score = []
        for j in range(len(guess)):
            # Checks for right in right place
            if guess[j] == s[i][j]:
                score.append("B")
            else:
                # Otherwise checks for right in the wrong place
                # Only does the rest of the string to avoid duplication
                for k in range(j, len(guess)):
                    if guess[k] == s[i][j]:
                        score.append("W")

        # Avoids going out of range
        if score != pegs:
            out.append(s[i])

        return out

def sorter(s):
    max = 0
    # Same as cleaner()
    for i in range(len(s)):
        score = ["B","B","B","B"]
        find = len(cleaner(s, s[i], score))
        if find > max:
            max = find
    return max

def first_guess(response, s):
    # Formatting input from string to list
    sliced = []
    for char in response:
        sliced.append(char.upper())

    if sliced == ["B","B","B","B"]:
        return 0

    # Gets rid of bad choices
    remove = cleaner(s, "1122", sliced)
    for i in range(len(remove)):
        s.remove(remove[i])

    next_guess = print(sorter(s), "is my next guess")

# Adding all possible guess combos
s = []
for i in range(1111,6667):
    s.append(str(i))

response = input("My guess is 1122, what's your response: ")
first_guess(response, s)
