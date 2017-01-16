# Loved this program, taken from the code exercise on the Interactive Python website
# http://interactivepython.org/runestone/static/pythonds/Introduction/DefiningFunctions.html
# The theorem states that a monkey hitting keys at random on a typewriter keyboard for an 
# infinite amount of time will almost surely type a given text, such as the complete works 
# of William Shakespeare.

import random

# Function to create random sentences of the same length as input string

def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res += alphabet[random.randrange(27)]
    return res     

# Function to get the score of the random string

def score(goal, textstring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == textstring[i]:
            numSame = numSame + 1
    return float(numSame) / len(goal)
    

def main():
    
    goalstring = 'methinks it is like a weasel'
    newstring = generateOne(28)
    best = 0
    newscore = score(goalstring, newstring)
    while newscore < 1:
        if newscore > best:
            print newscore, newstring
            best = newscore
        newstring = generateOne(28)
        newscore = score(goalstring, newstring)

main()
