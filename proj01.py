# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#user :name
# user_name= raw_input("enter your name")
# print "my name is" + user_name
# #users grade level;
# user_grade = raw_input("what grade are you in?")
# print "I'm in" + user_grade + " grade"
# #Then, it prints out a sentence that says the number of years until they graduate.
#
# years_until_graduation= 12-int(user_grade)
# print "you will graduate in" , int(years_until_graduation) , "years"
# Part II:
# This program asks the user for his/her name and birth month.
user_name= raw_input("enter name here")
print "my name is" + user_name
birth_month= raw_input ("what month were you born")
print"My birth month is" + birth_month

# Then, it prints a sentence that says the number of days and months until their birthday
current_month= 7
current_day= 9
birthday_day= raw_input("what day is your birthday")
if birth_month > 8:
    months_til_birth= int(birth_month) - int(current_month)
elif birth_month == 8:
    months_til_birth = int(birth_month)-int(current_month)
else: months_til_birth = 12-(int(current_month)-int(birth_month))
print int(months_til_birth), "months til your birthday"

if birthday_day > 9:
    days_til_birth= int(birthday_day) - int(current_day)


# If you complete extensions, describe your extensions here!
