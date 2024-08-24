# Initialize an empty list to store the numbers
numbers = []
while True:
    user_input = input("Please enter a number: ") # asking for an user input
    try:
        # Try to convert the input to a float
        number = float(user_input) 
        print(f"You entered the number: {number}")
        if number < 100 :
            numbers.append(number)
            if len(numbers) == 3 :
                print(f"The grades that has been provided are : {numbers}")
                break  # Exit the loop if the input is a valid number
        else:
            print("The number should be less than 100. Please try again.")
    except ValueError:
        # If the input is not a valid number, print an error and continue the loop
        print("Invalid input. Please enter a valid number.")
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

