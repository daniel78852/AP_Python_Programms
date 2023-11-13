import math
def is_triangle():
    result = False
    if sideA + sideB > sideC:
    if sideA + sideC > sideB:
    if sideB + sideC > sideA:
    result = True
    return result
def is_right_triangle():
 if sideA > sideB and sideA > sideC:
 result = sideB ** 2 + sideC ** 2 == sideA ** 2
 elif sideB > sideA and sideB > sideC:
 result = sideA ** 2 + sideC ** 2 == sideB ** 2
 else:
 result = sideA ** 2 + sideB ** 2 == sideC ** 2
 return result
def perimeter():
 return sideA + sideB + sideC
def area():
 if is_triangle() == False:
 return 0
 p = perimeter() / 2
 area = math.sqrt(p*(p-sideA)*(p-sideB)*(p-sideC))
 return area
def display_triangle():
 if sideA >= sideB and sideA >= sideC:
 largest = sideA
 if sideB >= sideC:
 middle = sideB
 smallest = sideC
 else:
 middle = sideC
 smallest = sideB
 elif sideB >= sideA and sideB >= sideC:
 largest = sideB
 if sideA >= sideC:
 middle = sideA
 smallest = sideC
 else:
 middle = sideC
 smallest = sideA
 else:
 largest = sideC
 if sideB >= sideA:
 middle = sideB
 smallest = sideA
 else:
 middle = sideA
 smallest = sideB
 print("Smallest Side: " + str(smallest))
 print("Medium Side: " + str(middle))
 print("Largest Side: " + str(largest))
sideA = int(input("Enter your first triangle side: "))
sideB = int(input("Enter your second triangle side: "))
sideC = int(input("Enter your third triangle side: "))
if is_triangle() == True:
 print("This is a true triangle.")
else:
 print("This is not a true triangle.")
if is_right_triangle() == True:
 print("This is a right triangle.")
else:
 print("This is not a right triangle.")
print("The perimeter of the triangle is " + str(perimeter()))
print("The area of the triangle is " + str(area()))
display_triangle()