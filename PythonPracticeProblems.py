# Initialize an empty list to store the numbers
numbers = []
while True:
    user_input = input("Please enter a number: ") # asking for an user input
    try:
        # Try to convert the input to a float
        number = float(user_input) 
        print(f"You entered the number: {number}")
        numbers.append(number)
        if len(numbers) == 3 :
            print(f"The grades that has been provided are : {numbers}")
            break  # Exit the loop if the input is a valid number
    except ValueError:
        # If the input is not a valid number, print an error and continue the loop
        print("Invalid input. Please enter a valid number.")
average_grade = sum(numbers)/len(numbers)
if average_grade >= 90 and average_grade <= 100 :
    print(f"Grade A  : you're awesome")
else:
    print("Fail")

