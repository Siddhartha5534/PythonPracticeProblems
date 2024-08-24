#problem 1
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.
# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
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

