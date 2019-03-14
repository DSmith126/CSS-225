#Deshawn Smith
# 3/7/2019

# Checks if the sum of user inputs are equal to, great than, or less than

number1 = int(input("Enter in number 1: "))
number2 = int(input("Enter in number 2: "))

def numbercheck(n1, n2):
    if n1 + n2 == 10:
        print("equal")
    elif n1 + n2 > 10:
        print("greater than")
    else:
        print("less that")

#numbercheck(number1, number2)
print(numbercheck(number1, number2))
