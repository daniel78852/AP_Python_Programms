"""#Exercise 1
def calculate_total(cart_items):
    # 1. Initialize a variable total to 0.
    total = 0

    # 2. Loop through each item in the cart.
    for item in cart_items:
        # 3. For each item, multiply its price by its quantity.
        item_total = item['price'] * item['quantity']

        # 4. Add the total price of the current item to the total.
        total += item_total

    # 5. Once all items have been processed, return the total.
    return total


# Example usage:
cart = [
    {'name': 'apple', 'price': 0.50, 'quantity': 2},
    {'name': 'banana', 'price': 0.30, 'quantity': 3},
    {'name': 'cherry', 'price': 0.20, 'quantity': 4}
]

# The function call should return the grand total for all items in the cart.
print(calculate_total(cart))  # Output will be the total cost of the items

#Exercise 2

def find_most_borrowed_book(books):
    # 1. Use the max function to find the book with the maximum value of times_borrowed.
    max_times_borrowed = 0
    most_borrowed_book = None
    for book in books:
        if book['times_borrowed'] > max_times_borrowed:
            max_times_borrowed = book['times_borrowed']
            most_borrowed_book = book

    # 2. Once the most borrowed book is identified, extract its title and author.
    title = most_borrowed_book['title']
    author = most_borrowed_book['author']

    # 3. Return a formatted string indicating the title and author of the most borrowed book.
    return f"The most borrowed book is '{title}' by {author}."


# Example usage:
library_books = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'times_borrowed': 100},
    {'title': '1984', 'author': 'George Orwell', 'times_borrowed': 150},
    # ... other books ...
]

# The function call should return the title and author of the most borrowed book.
print(find_most_borrowed_book(library_books))
# Output will be a string with the title and author of the most borrowed book"""


grocery_list = []
def grocery_calculator(name, price, quantity):

    grocery_dictionary = {
        "name":name,
        "price":price,
        "quantity": quantity
    }
    grocery_list.append(grocery_dictionary)

    for item in grocery_list:
        #print(item)
        total = item["price"] * item["quantity"]
        print(total)

grocery_calculator("Bananna", 2.50,3)


#Problem 2

def most_borrowed_book(book):
    return book["times_borrowed"]

def find_Most_borrowed_book(books):

    most_borrowed = max(books, key=most_borrowed_book)

    author = most_borrowed["author"]
    title = most_borrowed["title"]

    return f'The most borrowed book is {title} by {author}'


books_list = [
    {'title': 'Book A', 'author': 'Author A', 'times_borrowed': 1000},
    {'title': 'Book B', 'author': 'Author B', 'times_borrowed': 150},
    {'title': 'Book C', 'author': 'Author C', 'times_borrowed': 120}
]

#find_Most_borrowed_book(books_list)

print(find_Most_borrowed_book(books_list))


#most_borrowed_book_output = find_Most_borrowed_book(books_list)

#print(most_borrowed_book_output)




