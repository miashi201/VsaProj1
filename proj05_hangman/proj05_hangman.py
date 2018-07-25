# Name: Belal and Mia   
# Date: 7/11/18


# proj05: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

word = choose_word(wordlist)
random = word
lst = []
for letter in random:
    lst.append(letter)
#print lst

blank = []
for letter in random:
    blank.append("_")
print blank

print "Welcome to Hangman!"
print "I am thinking of a word that is" ,len(lst), "letters long!"

counter = 0
guess = 20
var = string.lowercase
print "Available letters:" ,var

win = False
while guess > 0 and guess <= 20:
    if ("_") not in blank:
        win = True
        print ""
        print "------------------"
        print ""
        print "YAAAASSSSSSS QUEEN YOU WON!!!! <3"
        break
    user_input = raw_input("Choose a letter! ")
    print ""
    print "--------------------"
    print ""
    guess = guess - 1
    print "You have", int(guess), "left! "
    for letter in lst:
        if user_input == lst[counter]:
            blank[counter] = user_input
        counter = counter + 1
        # if ("_") not in blank:
        #     print "YAAAASSSSSSS QUEEN YOU WON!!!! <3"
        #     break
        # if ("_") in blank:
        #     print "You lost stupid </3"
        #     break
        # if guess > 10:
        #     print "You lose! TRY AGAIN"

    # guess = guess - 1
    # print "You have", int(guess), "left! "
    print blank

    # var = string.lowercase
    # print "Letters left:" ,var
    if user_input in blank:
        var = var.replace(user_input, "")
    print "Available letters:" ,var
    counter = 0
    # if user_input not in var:
    #     print "You've already chosen this letter! TRY AGAIN"
    #     guess = guess + 1
if win == False:
    print ""
    print "------------------"
    print ""
    print lst
    print ""
    print "------------------"
    print ""
    print "Oh no bby you lost :( </3"
if win == True:
    guess = 0


# if letter = user_input:







