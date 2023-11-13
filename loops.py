import math
import random

even_counter = 0
odd_counter = 0

numbers_list = []
for numbers in range(1,101):
    numbers = random.randint(1,100)
    #print(numbers)
    numbers_list.append(numbers)

    if numbers % 2 == 1:
        #print(numbers, " Odd")
        odd_counter +=1
    else:
        #print(numbers, " Even")
        even_counter += 1

#print(numbers_list)
#print("Odds are: ", odd_counter)
#print("Evens are: ", even_counter)
#max_number = max(numbers_list)
#print("Max: ", max_number)
#min_number = min(numbers_list)
#print("Min: ", min_number)
#total =sum(numbers_list)
#print("Total sum: ", total)



#Part 2
import random


def generate_random_numbers(total_numbers):
    """Generate a list of random numbers."""
    numbers_list = [random.randint(1, 100) for _ in range(total_numbers)]
    return numbers_list


def count_even_odd(numbers_list):
    """Count the number of even and odd numbers in the list."""
    even_counter = 0
    odd_counter = 0

    for number in numbers_list:
        if number % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1

    return even_counter, odd_counter


def display_numbers_and_counts(numbers_list, even_counter, odd_counter):
    """Display the numbers, counts of even and odd, and other statistics."""
 #   print("Numbers List:", numbers_list)
 #   print("Evens count:", even_counter)
 #   print("Max number:", max(numbers_list))
 #   print("Min number:", min(numbers_list))
 #   print("Total sum:", sum(numbers_list))


# Generate a list of 100 random numbers
#numbers_list = generate_random_numbers(100)

# Count the number of even and odd numbers
#even_counter, odd_counter = count_even_odd(numbers_list)

# Display the numbers and their counts
#display_numbers_and_counts(numbers_list, even_counter, odd_counter)


"""______________________________________________________________________________"""
#Practice:

for i in range(1,6):
    for k in range(1, i+1):
        print(k, end=" ")
    print()
