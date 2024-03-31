import math
def area():
    a = float(input("Give the length of side a: "))
    b = float(input("Give the length of side b: "))
    c = float(input("Give the length of side c: "))
    s = (a+b+c)/2 #calculates semiperimeter
    area_squared = abs(s*(s-a)*(s-b)*(s-c))#begins calculating the area and makes positive
    print(area_squared)
    area = math.sqrt(area_squared) #completes calculating area by sqrting
    print("The area is " + str(area)) #prints result

area() #calls instance of function
