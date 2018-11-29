#Sanjay Bajnath               11/26/18
# Python Project 1 - Solving Equations

print("Hello. This program solves equations in the form ax+b=c.")
correct = "N"
#This while loop is used to verify that the correct equation is being solved.
while (correct == "N" or correct =="n"):
    #user_input is the string of numbers that the user inputs.
    user_input = input("Enter a, b, and c, separated by commas. ")
    #numbers_list turns the string into an array and removes the commas.
    numbers_list = user_input.split(",")
    #a,b, and c are the numbers from the array, without whitespace.
    a = float(numbers_list[0].strip())
    b = float(numbers_list[1].strip())
    c = float(numbers_list[2].strip())
    #If any of the numbers are divisible by 1, they are integers.
    if(a%1==0):
        a = int(a)
    if(b%1==0):
        b = int(b)
    if(c%1==0):
        c = int(c)
    print("Your equation is: ",a,"x +",b," = ",c,".")
    #The user identifies whether the equation is correct, and this affects the condition of the while loop.
    correct = input("Is this correct? (Type Y or N)")

#If the coefficient for x is 0, there are either infinitely many solutions or no solutions.
if(a==0):
    if(b-c == 0):
        print("There are infinitely many solutions! Any value of x will satisfy this equation.")
    else:
        print("There are no solutions! No value for x will satisfy this equation.")

else:
    #The equation is solved step by step.
    print("Subtract ",b," from both sides of the equation.")
    print(a,"x +",b,"-",b," = ",c,"-",b)
    print(a,"x =",(c-b))
    check_continue = input("Press Enter to continue.")

    #This while loop stops the program from moving on until the user presses enter.
    while (check_continue != ""):
        check_continue = input("Press Enter to continue")
    
    print("Divide both sides of the equation by ",a)
    print(a,"x/",a,"=",(c-b),"/",a)
    if((c-b)%a == 0):
        print("x =",int((c-b)/a))
    else:
        print("x =",(c-b),"/",a)
    check_continue = input("Press Enter to continue.")

    while (check_continue != ""):
        check_continue = input("Press Enter to continue")

    print("The solution is:")
    if((c-b)%a == 0):
        print("x =",int((c-b)/a))
    else:
        print("x =",(c-b),"/",a)
 
    check = input("Would you like to check this solution? (Y or N)")
    if (check == "Y" or check == "y"):
        print(a,"x +",b," = ",c)
        if((c-b)%a == 0):
            print(a,"(",((c-b)/a) ,") +",b," = ",c)
        else:
            print(a,"(",(c-b),"/",a ,") +",b," = ",c)
            
        print((c-b),"+",b,"=",c)
        print(c,"=",c)
        print("It works!")
