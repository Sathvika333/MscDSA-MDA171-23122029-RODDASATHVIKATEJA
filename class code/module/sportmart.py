#create a sportmart class,where you will have 
#inventory/shelf of items
#orders of customers

#create csv file which will store your inventory details and order details
#
#with the help of file handling techniques in python,read the file and create 
# an object for trinity store and populate the inventory items and orders into the trinity store
#
#to make sure that you have added all the items in your file,use s display method to show your 
# inventory and order history


        #with open("orders.csv","r") as csvfile:
         #   file = file.readlines()
          #  file.close()
class sportMart:
    def __init__(self):
        self.inventory ={}
        self.orders ={}

    def createInventory(self,product_id,product_name,price,quantity,units):
        temp ={
            "product_id":product_id,
            "product_name":product_name,
            "price":price,
            "quantity":quantity,
            "units":units
        }
        self.inventory[product_id] = temp
    
    def createorders(self,order_id,product_id,quantity,price,total):
        temp ={
            "order_id":order_id,                
            "product_id":product_id,
            "quantity":quantity,
            "price":price,
            "total":total
        }
        self.orders[order_id] = temp

    def printorders(self):
        print(self.orders)  

    def printinventory(self):
        print(self.inventory)

trinity = sportMart()
orders = open("module\orders.csv","r")
o_header = orders.readline()
o_data = orders.readlines()
for data in o_data:
    tmp = data.strip().split(',')
    total=int(tmp[2])*int(tmp[3])
    trinity.createorders(tmp[0],tmp[1],tmp[2],tmp[3],total)

trinity.printorders()
inventory = open("module\inventory.csv","r")
i_header = inventory.readline()
i_data = inventory.readlines()
for data in i_data:
    tmp = data.strip().split(',')
    print(tmp)
    trinity.createInventory(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4])

trinity.printinventory()













