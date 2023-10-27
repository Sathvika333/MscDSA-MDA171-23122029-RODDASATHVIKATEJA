#develop a contact management program where users can add,edit,delete,and search contact details using a dictionary .the menu options would facilitate these actions
contactList = []


def detailsList():
    name = input("enter name")
    phno = input("enter contactno")
    mailid = input("enter the mailid")
    name = name.strip().title()
    phno = phno.strip()
    mailid = mailid.strip()
    contactList.append(name)
    contactList.append(phno)
    contactList.append(mailid)
    return name,phno,mailid

def delete():
    print("*"*30)
    for i in contactList:
        delval = detailsList.pop()
        print(delval)
    print("*"*30)

def searchlist(search):
    search =search.strip()
    print("*"*30)
    print("details in the list")
    print("*"*30)
    for name in detailsList:
        print(name)
    for phno in detailsList:
        print(phno)
    for mailid in detailsList:
        print(mailid)
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


        


