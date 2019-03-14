#Deshawn Smith
#3/7/1019

# Checks if two user inputs are equal

number1 = int(input("Emter in number 1: "))
number2 = int(input("Enter in number 2: "))

def numbercheck(n1, n2):
    if n1 == n2:
        print9("True")
        return True

    else:
        print("false")
        return False

#numbercheck(number1, number2)
print(numbercheck(number1, number2))
