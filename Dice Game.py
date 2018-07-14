import random

random_number = random.randint(1,6)
die = [1,2,3,4,5,6]
dice = [random_number]
user_input = raw_input("How many time would you like to play?")
guess_number = user_input
counter = 0
print die
print" "
print"------------------"
print" "
for random_number in dice:
    if random_number == 1 or random_number == 3 or random_number == 5:
        print "Player One Wins!! Play again?"
    else:
        print "Player 2 wins!!! Play again?"
print random_number