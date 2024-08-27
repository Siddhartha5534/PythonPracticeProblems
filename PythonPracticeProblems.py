#problem 1
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.
# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
"""
#solution
# Initialize an empty list to store the numbers
numbers = []
while True:
    user_input = input("Please enter a number: ") # asking for an user input
    try:
        number = float(user_input) # Try to convert the input to a float
        print(f"You entered the number: {number}")
        if number <=  100 : # checking if the number is less than 100
            numbers.append(number) # if the previous line is true , appending the number to the list
            if len(numbers) == 3 : # checking the length of the list - restricted to 3
                print(f"The grades that has been provided are : {numbers}") 
                break  # Exit the loop if the input is a valid number # if 3 numbers are added to the list break out of the while loop
        else:
            print("The number should be less than 100. Please try again.") # letting the user know that the number is not less than or equal to 100
    except ValueError:
        # If the input is not a valid number, print an error and continue the loop
        print("Invalid input. Please enter a valid number.") # catching the error raised in the "try" block
average_grade = sum(numbers)/len(numbers)
if average_grade >= 90 and average_grade <= 100 :
    print(f"Grade A  : you're awesome")
elif average_grade >= 80 and average_grade < 90 :
    print(f"Grade B  : Keep Going")
elif average_grade >= 70 and average_grade < 80 :
    print(f"Grade C  : Try Harder")
elif average_grade >= 60 and average_grade < 70 :
    print(f"Grade D  : Wake Up")
elif average_grade >= 0 and average_grade < 60 :
    print(f"Grade F  : Wake Up")
else:
    print("Fail")
"""

#problem 2
# Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:
# "I love you"
# "a little"
# "a lot"
# "passionately"
# "madly"
# "not at all"
# If there are more than 6 petals, you start over with "I love you" for 7 petals, "a little" for 8 petals and so on.
# When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.
# Your goal in this kata is to determine which phrase the girls would say at the last petal for a flower of a given number of petals. The number of petals is always greater than 0.
"""
#solution
SONG_LYRICS = ["I love you","a little","a lot","passionately","madly","not at all"]
while True:
    user_input = input("HOW MANY PETALS IN THE FLOWER? ") # asking for an user input
    try:
        number = int(user_input) # Try to convert the input to an int
        if number <=  len(SONG_LYRICS) : # checking if the number is less than OR EQUAL TO 6
                print(f"The number of petals in the flower is: {number}")
                for numbers in range(number):
                    print(SONG_LYRICS[numbers])
                    numbers = numbers + 1
                break  # Exit the loop if the input is a valid number # if numbers exceeds the list length,  break out of the while loop
        else:
            print("The number should be less than 7. Please try again.") # letting the user know that the number is not less than or equal to 100
    except ValueError:
        # If the input is not a valid number, print an error and continue the loop
        print("Invalid input. Please enter a valid number.") # catching the error raised in the "try" block
"""

#problem 3
#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
"""
#solution
def evenodd():
    while True:
        user_input = input("Enter a number of your choice ") # asking for an user input
        try:
            number = int(user_input) # Try to convert the input to an int
            if number % 2 == 0:
                #print("It's an even number")
                return number
                break
            else:
                #print("it's an odd number")
                return number
                break
        except ValueError: # If the input is not a valid number, print an error and continue the loop
            print("Invalid input. Please enter a valid number.") # catching the error raised in the "try" block

new_variable  = evenodd()*2
print(new_variable)
"""
#problem 4
#Create a combat function that takes the player's current health and the amount of damage recieved, and returns the player's new health. Health can't be less than 0.
"""
def combat_function():
    while True:
        user_input = input("Enter a player's current health ") # asking for an user input
        user_input1 = input("Enter a player's damage received ") # asking for an user input
        try:
            current_health = int(user_input) # Try to convert the input to an int
            damage_received = int(user_input1) # Try to convert the input to an int
            new_health = current_health - damage_received
            if new_health > 0:
                print(f"New helth is {new_health}")
                break
            else:
                print(f"Abort !!")
                break
        except ValueError: # If the input is not a valid number, print an error and continue the loop
            print("Invalid input. Please enter a valid number.") # catching the error raised in the "try" block
combat_function()
"""
#problem 5
#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current number and previous sum.
"""
previous_sum = 0
number = 0
#for number in range(11):
while number <= 10:
    sum_of_numbers = previous_sum + number
    print(f"the sum of the current and previous number {sum_of_numbers}")
    previous_sum = sum_of_numbers
    number =number + 1
"""
#problem 6
#Write a function to check palindrome number
"""
def palindromenumber():
    while True:
        user_input = input("Enter a number of your choice ") # asking for an user input
        try:
            number = int(user_input) # Try to convert the input to an int
            original_number = number
            revised_number = 0
            while number > 0 :
                remainder = number % 10
                revised_number = revised_number * 10 + remainder
                number = number // 10
            if original_number == revised_number :
                print("palindrome number")
                return revised_number
                break
            else :
                print("Not a palindrome number")
                return revised_number
                break
        except ValueError: # If the input is not a valid number, print an error and continue the loop
            print("Invalid input. Please enter a valid number.") # catching the error raised in the "try" block

print(palindromenumber())
"""
"""
def palindromenumber():
    while True:
        user_input = input("Enter a number of your choice ") # asking for an user input
        try:
            number = int(user_input) # Try to convert the input to an int
            revised_number_as_string = str(number)[::-1]
            revised_number = int(revised_number_as_string)
            if number == revised_number :
                print("palindrome number")
                return revised_number
                break
            else :
                print("Not a palindrome number")
                return revised_number
                break
        except ValueError: # If the input is not a valid number, print an error and continue the loop
            print("Invalid input. Please enter a valid number.") # catching the error raised in the "try" block

palindromenumber()
"""

