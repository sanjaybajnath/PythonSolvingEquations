# Python Task - Approximating Solutions
# Sanjay Bajnath


# The equation given by the user is in the form ax + b = c. This function returns the value of c when x = n.
def F(n):
    return (b + (a * n))


print("This program will approximate a solution for the equation ax + b = c.")
print("It will look for a solution, x, such that ax + b is within one step size of c.")
correct_equation = False
while (correct_equation == False):
    # input_bad is used to make sure the user inputs numbers and not other characters.
    input_bad = True
    user_input = input("Enter a, b, and c, separated by commas.")
    user_input = user_input.replace(" ", "")

    num_list = user_input.split(",")
    while (input_bad):
        # not_number is the amount of user entries that are not numbers.
        not_number = 0
        for i in range(len(num_list)):
            try:
                num_list[i] = float(num_list[i])
            except:
                not_number += 1
        if (not_number == 0):
            input_bad = False
        else:
            # If there are more than 0 non-floatable characters, the user has to retry.
            input_bad = True
            print("Try again, but with numbers.")
            user_input = input("Enter a, b,and c, separated by commas.")
            user_input = user_input.replace(" ", "")
            num_list = user_input.split(",")
    a = num_list[0]
    b = num_list[1]
    c = num_list[2]
    print("Your equation is ", a, "x +", b, " =", c)
    ask = input("Are these equations correct? (Y or N)")
    if (ask == "y" or ask == "Y"):
        correct_equation = True
    else:
        correct_equation = False

bad_step = True
while (bad_step):
    step = input("Enter a step size: ")
    try:
        step = float(step)
        bad_step = False
    except:
        print(step, "is not a number. Try again.")
        bad_step = True
initial_step = step

bad_guess = True
while (bad_guess):
    guess = input("Enter an initial guess. x = ")
    try:
        guess = float(guess)
        bad_guess = False
    except:
        print(guess, "is not a number. Try again.")
        bad_guess = True
initial_guess = guess

steps_count = 0

# The while loop continues until the difference between F(guess) and c is less than or equal to half of a step size.
while (abs(c - F(guess)) > step / 2):
    if (F(guess) > c):  # The output of the function is too high when the current guess is the input.
        if (F(guess + step) > F(guess)):  # F is increasing, so the current guess is too far to the right.
            guess -= step
        else:  # F is decreasing, so the current guess is too far to the left.
            guess += step
    else:  # The output of the function is too high when the current guess is the input.
        if (F(guess + step) > F(guess)):  # F is increasing, so the current guess is too far to the left.
            guess += step
        else:  # F is decreasing, so the current guess is too far to the right.
            guess -= step

    # This prevents the program from infinitely switching between two guesses when the solution is in between the two guesses.
    if (F(guess) < c and F(guess + step) > c):
        step = step / 2
    elif (F(guess) > c and F(guess + step) < c):
        step = step / 2

    steps_count += 1

print("Your equation was", a, "x +", b, " =", c)
if (step != initial_step):
    print("Initially, the step size was", initial_step, ", but no solution could be found.")
    print("The step size was changed to", step)
else:
    print("The step size was", step)

print("The estimated solution is x =", guess)
print("This program found the estimated solution in", steps_count, "steps.")
