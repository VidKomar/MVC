# model_view_controller.py
# Model!
# Packaging CRUD operations into a single class.

import basic_backend
import MVC_exceptions

class ModelBasic(object): # Class with several methods for CRUD operations
    def __init__(self, application_items):
        self._item_type = "product"
        self.create_items(application_items)

    @property
    def item_type(self):
        return self._item_type 
    
    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type # When assigning a new value to item_type. Assigns it _item_type

    def create_item(self, name, price, quantity):
        basic_backend.create_item(name, price, quantity)

    def create_items(self, items):
        basic_backend.create_items(items)

    def read_item(self, name):
        return basic_backend.read_item(name)

    def read_items(self):
        return basic_backend.read_items()

    def update_item(self, name, price, quantity):
        basic_backend.update_item(name, price, quantity)

    def delete_item(self, name):
        basic_backend.delete_item(name)


# Creating a simple UI in shell. Principle is the same as PyQt GUI.
# No logic in View class, using normal functions!
# Replace class View with your own

class View(object):
    """
    Static methods are commonly used when a method does not require access to the instance or instance-specific data.
    They are self-contained and independent of the state of the object.
    You can think of static methods as utility functions that are related to the class
    but don't rely on any instance-specific information.

    Unlike regular methods, static methods don't have access to instance
    variables or other instance-specific attributes.
    They can only access other static methods or static variables within the same class.
    Static methods are defined within the class definition but are not associated
    with any particular instance of the class.

    Static methods are useful for organizing utility functions,
    performing calculations, or implementing helper methods that
    don't need to interact with instance-specific data.
    """
    @staticmethod
   
    def show_bullet_point_list(item_type, items): # Itemise list to show to user
        print("-{} List -".format(item_type.upper())) # Formating display of items
        for item in items: # List all items from items. Iterator is items.
            print("o {}".format(item)) # Show item in a list

    @staticmethod
    def show_numer_point_list(item_type, items): # Enumerated list of items (sequentially)
        print("-{} List -".format(item_type.upper()))
        for item in enumerate(items):
            print("{}. {}".format(i+1, item)) 

    @staticmethod
    def display_missing_item_error(item, err): # No specific item error
        print('We are sorry, we have no {}!'.format(item.upper()))
        print('{}'.format(err.args[0]))

    @staticmethod
    def display_item_already_stored_error(item, item_type, err): # Item already stored error
        print('Hey! We already have {} in our {} list!'.format(item.upper(), item_type))
        print('{}'.format(err.args[0]))