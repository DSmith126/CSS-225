import math

#Deshawn Smith
#2/28/2019

#Calculates the area of a circle

#Function recieves radius and cuculates area of a circle
def areaOfCircle(radius):
    area = (radius ** 2) * math.pi
    return area

#x = areaOfCircle(10)

print("The area of the circle is ", areaOfCircle(10))

print("The area of the circle is ", areaOfCircle(20))

print("The area of the circle is ", areaOfCircle(30))
