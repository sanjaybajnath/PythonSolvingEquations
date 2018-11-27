#Sanjay Bajnath               11/26/18
# Python Project 1 - Solving Equations


correct = "N"
while (correct == "N"):
    user = input("Enter a, b, and c, separated by commas. ")
    numbers = user.split(",")
    a = float(numbers[0].strip())
    b = float(numbers[1].strip())
    c = float(numbers[2].strip())
    print("Your equation is: ",a,"x +",b," = ",c,".")
    correct = input("Is this correct? (Type Y or N)")

print("Subtract ",b," from both sides of the equation.")
print(a,"x +",b,"-",b," = ",c,"-",b)
print(a,"x =",(c-b))
check_continue = input("Press Enter to continue.")

while (check_continue != ""):
    check_continue = input("Press Enter to continue")

print("Divide both sides of the equation by ",a)
print(a,"x =",(c-b))

check_continue = input("Press Enter to continue.")

while (check_continue != ""):
    check_continue = input("Press Enter to continue")


print("x =",((c-b)/a))
 
check = input("Would you like to check this solution? (Y or N)")
if (check == "Y"):
    print(a,"x +",b," = ",c)
    print(a,"(",((c-b)/a) ,") +",b," = ",c)
    print((c-b),"+",b,"=",c)
    print(c,"=",c)
    print("It works!")
