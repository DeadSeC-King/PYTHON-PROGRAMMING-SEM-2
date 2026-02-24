# 6. Create a contact book (add, search, update, delete)

contacts = {}

while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif ch == "2":
        name = input("Search name: ")
        print("Phone:", contacts.get(name, "Not found"))

    elif ch == "3":
        name = input("Name to update: ")
        if name in contacts:
            contacts[name] = input("New phone: ")
        else:
            print("Not found")

    elif ch == "4":
        name = input("Name to delete: ")
        contacts.pop(name, None)

    elif ch == "5":
        break
