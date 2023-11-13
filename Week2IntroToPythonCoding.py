

def ctof(celsius):
    f = (celsius * 9/5) + 32
    return f
;
def ftoc(farenheit):
    c = (farenheit - 32) * 5 / 9
    return c

print("Welcome to my temperature converting machine.")
print("Choose one to convert 'Celsius' to 'Farenheit'.")
print("Choose two to convert 'Farenheit' to 'Celsius'")

choice = int(input(">> "))

if choice == 1:
    celsius = float(input("Enter your temperature in celsius: "))
    converted_temp = ctof(celsius)
    print("Here is your temperature in farenheit: " + str(converted_temp))

if choice == 2:
    farenheit = float(input("Enter your temperature in farenheit: "))
    converted_temp2 = ftoc(farenheit)
    print("Here is your temperature in celsius: " + str(converted_temp2))


