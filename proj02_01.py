# Name:
# Date:

# proj02: sum

# Write a program that prompts the user to enter numbers, one per line,
# ending with a line containing 0, and keep a running sum of the numbers.
# Only print out the sum after all the numbers are entered
# (at least in your final version). Each time you read in a number,
# you can immediately use it for your sum,
# and then be done with the number just entered.

#Example:
# Enter a number to sum, or 0 to indicate you are finished: 4
# Enter a number to sum, or 0 to indicate you are finished: 5
# Enter a number to sum, or 0 to indicate you are finished: 2
# Enter a number to sum, or 0 to indicate you are finished: 10
# Enter a number to sum, or 0 to indicate you are finished: 0
#The sum of your numbers is: 21

# counter = 0
# s=""
# #key word while
# while counter <= 10:
#      print counter
#      counter = counter + 1
#      s=s+"a" #shows that you can also use this with other variables besides integers
#      if counter == 5:
#          break
# sum = 0
#
# number_one = int(raw_input("enter number here"))
# number_two= number_one
# sum = sum + number_one
#
# while  number_one > 0 and number_two > 0:
#     number_two = int(raw_input("enter number here"))
#
#     sum = sum + number_two
#
# print "the sum of your numbers is", int(sum)

#key word is for

#loop over a range of #s

# s= "vsa"
# for letter in s:
#     print letter
#     if letter == "s":
#         print "this is an s"
#

# number_of_numbers = int(raw_input("How many Fibonacci number do you want to generate?"))
# previous_number = 0
# current_number = 1
#
#
# for next_number in range(number_of_numbers):
#     print current_number
#     next_number = previous_number + current_number
#     previous_number = current_number
#     current_number = next_number

number_of_numbers = int(raw_input("how many fibonacci numbers do you want to generate?"))
previous_number = 0
current_number = 1
next_number = 0
while next_number is > 0:
    print current_number
    next_number = previous_number + current_number
    previous_number = current_number
    current_number = next_number
