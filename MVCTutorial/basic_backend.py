import MVC_exceptions # Import your own!

items = list()

def create_items(app_items):
    global items
    items = app_items

def create_item(name, price, quantity):
    global items
    results = list(filter(lambda x: x["name"] == name, items))
    
    if results:
        raise MVC_exceptions.ItemAlreadyStored("'{}' already Stored".format(name))
    else:
        items.append({"name": name, "price": price, "quantity": quantity})

def read_item(name):
    global items
    myitems = list(filter(lambda x: x["name"] == name, items))
    if myitems:
        return myitems[0]
    else:
        raise MVC_exceptions.ItemNotStored("Cant read '{}', because it is not stored".format(name))


def read_items():
    global items
    return [item for item in items]


# Update & delete functionalities

def update_item(name, price, quantity):
    global items
    idxs_items = list(filter(lambda i_x: i_x[1]["name"] == name, enumerate(items)))
    if idxs_items:
        i, item_to_update = idxs_items[0][0], idxs_items[0][1]
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        MVC_exceptions.ItemNotStored("Cant update '{}' because it is not stored".format(name))

def delete_item(name):
    global items
    idxs_items = list(
        filter(lambda i_x: i_x[1]["name"] == name, enumerate(items)))
    if idxs_items:
        i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
        del items[i]
    else:
        raise MVC_exceptions.ItemNotStored("Cant delete '{}'' because its not stored".format(name))


"""def main():

    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]

    # CREATE
    create_items(my_items)
    create_item('beer', price=3.0, quantity=15)
    # if we try to re-create an object we get an ItemAlreadyStored exception
    # create_item('beer', price=2.0, quantity=10)

    # READ
    print('READ items')
    print(read_items())
    # if we try to read an object not stored we get an ItemNotStored exception
    # print('READ chocolate')
    # print(read_item('chocolate'))
    print('READ bread')
    print(read_item('bread'))

    # UPDATE
    print('UPDATE bread')
    update_item('bread', price=2.0, quantity=30)
    print(read_item('bread'))
    # if we try to update an object not stored we get an ItemNotStored exception
    # print('UPDATE chocolate')
    # update_item('chocolate', price=10.0, quantity=20)

    # DELETE
    print('DELETE beer')
    delete_item('beer')
    # if we try to delete an object not stored we get an ItemNotStored exception
    # print('DELETE chocolate')
    # delete_item('chocolate')

    print('READ items')
    print(read_items())

if __name__ == '__main__':
    main()"""
