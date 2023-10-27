nameList = []

def storename():
    name = input("enter the name to be stored ")
    name = name.strip().title()
    nameList.append(name)
    return name

def listNames():
    print("*"*30)
    print("names in the list")
    print("*"*30)
    for name in nameList:
        print(name)
    print("*"*30)

def searchName(search):
    search = search.strip().title()
    found = False
    for name in nameList:
        if name == search:
            found = True
            break
    if found ==True:
            print("Name exist in the list")
    else:
        print("name doesnt exist")

def exit():
    if choice ==4:
        exit()

print("*"*30)
print("Name Management - application")
print("*"*30)
while True:
    print("*"*30)
    print("1.enter name:")
    print("2.list the Names")
    print("3.search for a name")
    print("4.exit")
    print("*"*30)

    choice = input("Enter your Choice :")
    print("your choice:",choice)

    if int(choice)==1:
        name = storename()
        print("name () added successfully :",format(name))
    elif int(choice) == 2:
        listNames()
    elif int(choice) == 3:
        name = input("enter a name to be search")
        searchName(name)
    elif int(choice) == 4:
        exit()
    else:
        pass


        


