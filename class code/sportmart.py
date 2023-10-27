class sportMart:
    def _init_(self):
        self.inventory ={}
        self.orders = {}
    def createInventory(self,ProductID,ProductName,Quantity,Price):
        temp = {
            "productid": ProductID,
            "productname" : ProductName,
            "quantity": Quantity,
            "price": Price

        }
        self.inventory[ProductID] = temp 

    def createOrder(self,Orderid,ProductID,Quantity,price,total):
        temp = {
            'orderid' : Orderid,
            'productid': ProductID,
            'quantity': Quantity,
            'price': price,
            'total': total
        }
        self.orders[Orderid] = temp

    def printOrders(self):
        print(self.orders)

    def printInventory(self):
        print(self.inventory)


trinity = sportMart()
orders = open("module\orders.csv","r")
o_header = orders.readline()
o_data= orders.readlines()

for data in o_data :
    tmp = data.strip().split(',')
    trinity.createOrder(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4])

trinity.printOrders()
inventory = open("Inventory.csv","r")
i_header = inventory.readline()
i_data = inventory.readlines()
for data in o_data:
    tmp = data.strip().split(',')
    trinity.createInventory(tmp[0],tmp[1],tmp[2],tmp[3])

trinity.printOrders()
inventory = open("Inventory.csv","r")
i_header = inventory.readline()
i_data = inventory.readlines()
for data in o_data:
    tmp = data.strip().split(',')
    trinity.createInventory(tmp[0],tmp[1],tmp[2],tmp[3])
