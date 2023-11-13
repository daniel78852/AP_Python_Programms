#The exercises below are to better grasp the concepts of strings and substrings
#String vs Substring
#Concatination
#String Methods upper, lower, split, join

# Create a String set of values "Hello World."

myVar = "Hello World"
#print(myVar)

#Find the position of a substring using .find() method
#var = var.find("substring you are looking for")
sub_string = myVar.find("l")
#print(sub_string)


#Replacing substrings using the replace()
#newVar = var.replace("word to  be replace",""Word to replace with")

sub_string2 = myVar.replace("World", "Daniel")
#print(sub_string2)



#___________________________________________________________________________________

#String Formatting
# Many ways to format a string
#1. Concatination using the "+" sign


#2. String Interpolation (f-string) Python3.6 and up


#3 The str.format() method.

#3.1 Can also format the order in which they appear by placing the index inside
# {} bracets

# you also have the "%" Formatting and Template Strings  by importing string and Template


#Using the split()
myString = "Helly Yanick, How are you, today?"

split_String = myString.split()
#print(split_String)
#print(split_String[3:5])
#split_String = "a".join()
#print(split_String)


#Using Join
list1 = ["Welcome", "to", "the", "class"]
x = " Monkey ". join(list1)
print(x)

#Using index()
