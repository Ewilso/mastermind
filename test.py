def mastermindScore(s,guess):
    score = []
    matching = len(set(guess) & set(s[0]))
    pegs = sum(1 for v1, v2 in zip(guess,s[0]) if v1 == v2)
    for i in range(pegs):
        score.append("B")
    for i in range(matching - pegs):
        score.append("W")
    return score

print(mastermindScore([['1','1','3','4']],['3','4','3','4']))
