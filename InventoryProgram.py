inventory_list = [] #Create the empty list

def add_item(name, quantity, price):

    items = { #Set items to a dictionary
        "Name": name,
        "Quantity": quantity,
        "Price": price
    }

    inventory_list.append(items) #Add dictionary elements to the list
    print(f'{name} has been added to your list')


def remove_item(name):
    for i in inventory_list: #iterates through a list
    
        if i["Name"] == name: #Use the Name that is the key value from the dictionary that has been addeed tot he list
            inventory_list.remove(i) #Remove item
            print(f'{name}, has been removed from your inventory list')
    
    return f"{name}, not found in your inventory list. "


def display_inventory():
    for items in inventory_list:#iterate throgh the list

        print(items)#Print all items

def update_item(name, new_quantity, new_price):
    for item in inventory_list:#iterate through the list
        if item["Name"] == name: #Same as before
            item["Quantity"] = new_quantity#We are now resetting the value of Quantity to new_quantity
            item["Price"] = new_price#Same as above
            print(f"{name} has been updated")
            print(f"New quantity is {new_quantity}.")
            print(f"New price is {new_price}.")
    return f"Item not found in your inventory oist."
    #print(f"{name}, not found.")

def search_item(name):
    for item in inventory_list: #iterate throgh the ist
        if item["Name"] == name: #look for the item in thelist using the key value saved to the list
            print(f'Item {item["Name"]}, has been found', item)
            return 
    
    print(f'{item["Name"]} not found', item)



add_item("Apple", 5, 1.50)
add_item("Banana", 2, 2.40)

display_inventory()
remove_item("Banana")
display_inventory()
#print(remove_item("Orange"))
item_removed = remove_item("Orange")
print(item_removed)




