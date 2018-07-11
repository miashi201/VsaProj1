# coding=utf-8
# Name:
# Date:
# var = ["cat", "b"]
# var2 = ["a", "b", "cat",3]
# #index - 0 indexed
# # one item
# print var2[3]
# #slice of list
# print var2[0:3]
# #all but first
# print var2 [1:]
# #all but last
# print var2 [:-1]
#
# #replace
# var2[0] = "tree"
# print var2
#
# #loop
# # to change
# counter = 0 #
# for item in var2: #each item in the list (var2)
#     if item == "cat": #checking each item in order to find "cat"
#         var2[counter] = "dog" # when "cat is found changes it to dog
#         counter = counter + 1 #sets the counter = to itself + 1 and allows us to keep track of where we are in thr list
# #add to a list
# var2.append(28)
# print var2
# #add to an empty list
# lst = []
# s = "This is a string"
# for letter in s:
# lst.append (letter)
# print lst
"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # and write a program that prints out all the elements of the list that are less than 5.
# counter = 0
# for item in a:
#     if item < 5:
#         print item
#         counter = counter + 1

# lst = []
#
# for item in a:
#          if item < 5:
#             lst.append(item)
# print lst

number = raw_input("Enter a number")

lst = []
counter = 0
for item in a:
    if item < number:
        lst.append(item)
    counter = counter + 1
print lst









#Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
# same_elements = []
#
# Take a list, say for example this one:

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# and write a program that replaces all “a” with “*”.
# counter = 0
# old_letter= "a"
# new_letter= "*"
#
# for item in d:
#     if item == old_letter:
#         d[counter]= new_letter
#     counter = counter + 1
# print d








#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.

# word = raw_input("Please enter a word, and I will tell you if it's a palindrome!")
# possible_palindrome = []
# for letter in word:
#         possible_palindrome.append(letter)
#
# for letter in possible_palindrome:
#     if possible_palindrome[0] == possible_palindrome[-1]:
#         print "Your word is a palindrome"


