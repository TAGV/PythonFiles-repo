# Class to collect all objects in one list
class Items():
    counter = 0
    objlist = []
    def __init__(self,name,price):
        self.name = name
        self.price = price
        assert self.price >= 100,"The price is not more than or equal to 100"
        Items.counter += 1
        Items.objlist.append(self)      # Since this will be called atleast once for every object created

    def __repr__(self):
        return f"Items({self.name},{self.price})"

    def getCount(self):
        return Items.counter

    def getObjList(self):
        return Items.objlist

item1 = Items("Bag",100)
item2 = Items("Table",200)
item3 = Items("Chair",300)
#item4 = Items("Pebble",50)  # This will cause assertion error

print(item1)
print(item2)

print("No of Objects = ",Items.getCount(Items))
print(Items.getObjList(Items))