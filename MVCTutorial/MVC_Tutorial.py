# https://www.giacomodebidda.com/posts/mvc-pattern-in-python-introduction-and-basicmodel/

from basic_backend import *
import model_view_controller as MVC

my_items = [{"name": "bread", "price": 0.5, "quantity": 20},
             {"name": "milk", "price": 1.0, "quantity": 10},
             {"name": "wine", "price": 10, "quantity": 5}]

"""# Creating a new entry
create_items(my_items)
create_item("Beer", price= 3.0, quantity= 15)
# create_item("Beer", price= 3.0, quantity= 15) Raises exception, Beer already Stored.

# Reading entries
print("Read items")
print(read_items) # return [item for item in items]

# print(read_item("chocolate")) Raises expection ItemNotStored, due to it not being stored.
print("Reading milk?")
print(read_item("milk"))

# Updating entries
print("Update bread")
print(read_item("bread"))
update_item("bread", 2, 30) # Also ("bread", price= 2, quantity= 30) for more clarity
print(read_item("bread"))

# Deleting entry
print("Deleting Beer :(")
delete_item("Beer")

#print("Deleting non-exsisting chocolate")
#delete_item("chocolate")

#print(my_items)"""

# Test run of the created MVC

c = MVC.Controller(MVC.ModelBasic(my_items), MVC.View())
# c.show_items(bullet_points=True)
c.show_item("Chocolate")

#Git Push test - IGNORE