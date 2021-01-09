# age_converter.py
from datetime import date
import calendar

print("\n\nHello, my name is Brady.\n")

dte = date.today()

def month_length(m, y):
    leap = 0
    if y % 4 == 0: #is year divisible by 4?
        leap = 1
    if y % 100 == 0 and y % 400 != 0: #year divisible by 100, but not 400
        leap = 0
    if m == 2: #February special case
        return 28 + leap
    big_months = [1,3,5,7,8,10,12] #31 day months
    if m in big_months:
        return 31
    return 30

while True: #checks whether user inputs a valid month
    user_month = int(input("Please enter your birth month as a number:\n"))
    if 1 <= user_month <= 12:
        while True: #checks if user inputs a valid day based on month and year
            user_day = int(input("\nPlease enter your birth day as a "
            "number:\n"))
            if user_day < 1 or user_day > 31:
                print("\nI'm sorry, that's not a valid day.\n")
            user_year = int(input("\nPlease enter your birth year:\n"))
            if 1 <= user_day <= month_length(user_month, user_year):
                break
            else:
                print("\nI'm sorry, that's not a valid day in the "
                "month and year you chose.\n")
        break
    else:
        print("\nI'm sorry, that's not a valid month.\n")


if dte.month == user_month and dte.day == user_day:
    print("\nHappy Birthday!\n")

else:
    print("\nThank you.\n")

# difference between today's date and my birthdate
delta1 = dte - date(2002, 5, 7)

# difference between today's date and user's birthdate
delta2 = dte - date(user_year, user_month, user_day)

age_secs = delta1.days * 24 * 60 * 60
user_secs = delta2.days * 24 * 60 * 60

user_month = calendar.month_name[user_month]

if delta1 == delta2: #special case that we share a birthday
    print("Hold on, I was born on May 7th, 2002...")
    print("And you were too!\n")
    print(f"That makes us both {age_secs:,} seconds old!\n")

else: #don't want to repeat any of the users info if we share a b-day
    print("I was born on May 7th, 2002", end=", ")
    print(f"which makes me {age_secs:,} seconds old!\n")
    
    print(f"You were born on {user_month}", end= " ")
    
    # if statements so that the "x1st", "x2nd", and "x3rd" special cases work
    if user_day % 10 == 1:  # if the date is "x1st"
        print(f"{user_day}st, {user_year}", end=", ")

    elif user_day % 10 == 2:  # if the date is "x2nd"
        print(f"{user_day}nd, {user_year}", end=", ")

    elif user_day % 10 == 3:  # if the date is "x3rd"
        print(f"{user_day}rd, {user_year}", end=", ")

    else: #all other "xth" numbers
        print(f"{user_day}th, {user_year}", end=", ")

    #the end of the sentence is the same for all 
    print(f"which makes you {user_secs:,} seconds old!\n")