import div
contacts_list = {}
def add_contact():
    name = input("Name: ")
    number = input("Number: ")
    contacts_list[name] = number
    return number

def view_contact():
    if not contacts_list:
        print("No Contacts yet!")
    else:
        for i, (name, number) in enumerate(contacts_list.items(), 1):
            print(f"{i}. {name}: {number}")

def search_contact():
    if not contacts_list:
        print("No Contacts yet!")
    else:
        name = input("Name: ")
        if name in contacts_list:
            print(f"Number : {contacts_list[name]}")
        else:
            print("Sorry this person is not in your contact!")

def del_contact():
    if not contacts_list:
        print("No Contacts yet!")
    else:
        name = input("Name: ")
        if name in contacts_list:
            del contacts_list[name]
            print(f"{name} is succesfully deleted from your contacts!")
        else:
            print("Sorry this person is not in your contact!")

while True:
    print("CONTACT BOOK")
    print("-----------")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Quit")
    print()
    option = input("Choose an option (number): ")
    option = div.valid_int(option, "please enter the number of either menu!")
    if option is None:
        continue
    match option:
        case 1:
            add_contact()
        case 2:
            view_contact()
        case 3:
            search_contact()
        case 4:
            del_contact()
        case 5:
            print("Thankyou for using this program!")
            break
        case _:
            print("Please enter the number of either menu!")