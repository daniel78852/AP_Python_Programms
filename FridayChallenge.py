"""import math

#def savings(saved_money, money_to_save):
 #   new_monthly_savings = saved_money + money_to_save
  #  return new_monthly_savings * 3


#updated_savings = savings(100, 75)

#print(f'Your updated savings after 3 montsh is: $ {updated_savings}')

#ex2.

#ex 3.

#def plant_heights(weekly_growth=5):


 #   myList = []
  #  for i in range(weekly_growth):
   #     user_input = int(input("What were teh plants heights: "))
    #    myList.append(user_input)
     #   new_sum = sum(myList)/len(myList)
    #print( new_sum)
        #print(user_input)
        #print(myList)


#plant_heights()


#The Science Fair Project:"""
import math

"""def average_temperature():
    temp = []
    temperatures = int(input("How many temperatures will you be adding today?"))
    month_days = int(input("How many days this month? "))
   # print(">> ")

    for _ in range(temperatures):
        temp_data = int(input("What were teh temperatures? "))
        temp.append(temp_data)
        temp_data_avg = sum(temp)/month_days
    print(temp_data_avg)
    return temp_data_avg
temps = average_temperature()

print("You're temperatures are: ", temps)
"""

#def avg_temp(temperatures):

 #   if not temperatures: # Check the list make sure it is not empty
  #      return 0

   # total = sum(temperatures) #Create a new variable to hold the sum of the list in tempratures.
    #return total / len(temperatures) #Return the sum and divided by the length in the list temperatures

#monthly_temps = [25, 30, 99, 80 ] #Create the list to be used for calculations

#monthly_report = avg_temp(monthly_temps) #Create a variable set it equal to the function and pass the list of data
#print("Your monthly temperature avg. is: ", monthly_report)#Print your report


#def total_rainfall(rainfall):
 #   if not rainfall:
  #      return 0

   # return sum(rainfall)

#rainfall_data = [50,50]

#total_monthly_rainfall = total_rainfall(rainfall_data)
#print("The total rainfall for the month was: ", total_monthly_rainfall)

#def max_wind_speed(windspeed):
 #   if not windspeed:
  #      return 0

   # return max(windspeed)

#windspeed_data = [90, 100, 55, 200,44,55]

#monthly_windspeed_max = max_wind_speed(windspeed_data)
#print("This months highest windspeed was: ", monthly_windspeed_max)





#Triangles



def is_traingel():
    if a + b > c or b + c > a or c + a > b:
        print("This is a triangle")
        return True
    else:
        print("This aint no Tri")
        return False

def right_triangle():
    if pow(a,2) + pow(b,2) == pow(c,2):
        print("Right triangle")
        return True
    else:
        print("This is not a right triangle")
        return False

def perimeter():
    #print(a+b+c)
    return a+b+c

def area ():

    if right_triangle() == False:
        return 0

    p = perimeter()/2
    #print(p)
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("area: ", area)
    return area


def display_triangle():
    #middle = 0
    #smallest = 0
    #largest= 0
    if a >= b and a >= c:
        largest = a
        if b >= c:

            middle = b
            smallest = c

        else:
            middle = c
            smallest  = b

    elif b > a and b > c:
        largest = b
        if a >= c:
            smallest = c
        else:
            middle = c
            smallest = a

    else:
        largest = c
        smallest = b
        middle = a
    print("Smallest side: " + str(smallest))
    print("Middle side: " + str(middle))
    print("Largest side: " + str(largest))





#a = int(input("Side a>> "))
#b = int(input("side b>> "))
#c = int(input("side c>> "))

#is_traingel()
#right_triangle()
#perimeter()
#area()
#display_triangle()


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict) # prints out dictionsary

#iteration will print k, v
for k, v in thisdict.items():
    print(k, v)
print("_____________________________________________________________________")

#Will print values
for v in thisdict.values():
    print(v)
print("______________________________________________________________")

for k in thisdict.keys():
    print(k)