#Deshawn Smith
#2/28/2019

#Multiplies all values in a list

def multiplyList(numbers):
    total = 1
    for n in numbers:
        total = 1
        total = total * n
    return(total)

n = [1, 5, 3, -8, 10]

print(multiplyList(n))

print(multiplyList([1, 2, 3]))
