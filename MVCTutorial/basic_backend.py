import MVC_expections as MVC_expections # Import your own!

items = list()

def create_items(app_items):
    global items
    items = app_items

def create_item(name, price, quantity):
    global items
    results = list(filter(lambda x: x["name"] == name, items))
    
    if results:
        raise MVC_expections.ItemAlreadySorted("'{}' already sorted".format(name))
    else:
        items.append({"name": name, "price": price, "quantity": quantity})

def read_item(name):
    global items
    myitems = list(filter(lambda x: x["name"] == name, items))
    if myitems:
        return myitems[0]
    else:
        raise MVC_expections.ItemNotSorted("Cant read '{}', because it is not stored".format(name))
    
# Update & delete functionalities

def update_item(name, price, quantity):
    global items
    idxs_items = list(filter(lambda i_x: i_x[1]["name"] == name, enumerate(items)))
    if idxs_items:
        i, item_to_update = idxs_items[0][0], idxs_items[0][1]
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        MVC_expections.ItemNotStored("Cant update '{}' because it is not stored".format(name))")

def delete_item(name):
    global items
    idxs_items = list(
        filter(lambda i_x: i_x[1]["name"] == name, enumerate(items)))
    if idxs_items:
        i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
        del items[i]
    else:
        raise mvc_exc.ItemNotStored("Cant delete '{}'' because its not stored".format(name))


def read_items():
    global items
    return [item for item in items]