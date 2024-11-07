# I rate this assignment a 0 because it just asked me to wrap my code from 10_06
# in a while loop, which I had already done. So I just copied and pasted it into
# here.

# Prompt the user with instructions for the program's purpose.
print("Please enter two numbers and the computer will add them.")
print("Enter 'q' to quit.")  # Informs the user they can type 'q' to exit the program.

# Start an infinite loop to continuously prompt the user for input until they choose to quit.
while True:
    # Prompt the user for the first number.
    first_number = input("\nFirst number: ")
    # Check if the user wants to quit.
    if first_number == 'q':
        break

    # Prompt the user for the second number.
    second_number = input("Second number: ")
    # Check if the user wants to quit.
    if second_number == 'q':
        break

    # Attempt to convert the inputs to integers and add them.
    try:
        answer = int(first_number) + int(second_number)
    # Handle cases where the user inputs non-numeric values, preventing the program from crashing.
    except ValueError:
        print("Please don't enter any letters.")  # Error message if input isn't a valid integer.
    else:
        # If the inputs are valid integers, display the sum.
        print(answer)