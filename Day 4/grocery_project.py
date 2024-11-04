### Mini Project



"""
**Project 1: Grocery List Manager**
Objective:
Create a simple grocery list manager where users can add items, view the list, and remove duplicates (using set functionality).

Steps:
Ask the user to input grocery items (comma-separated).  
Store these items in a list.  
Convert the list to a set to remove duplicates.  
Display the updated grocery list.  """

# asking for items
items = input("Please enter items name separated by commas: ")

# items converted into list
items_list = list(items)

items_list = items.strip().split(',')
# type casting
items_unique = set(items_list)

# Show unique items list
print(f"Thank you for entering items here is your unique list of items {items_unique}")

# end of function
# Water Bottle,  Coffee Mug,Snack Stash (Granola Bars, Nuts, etc.),First Aid Kit,Comfortable Chair Cushion
     
