#Building a Contact Book app using dictionary

contact_book={
    "Home":9876543210,
    "Police":100,
    "Emergency":6324569812,
    "Ankita":8877456932
}

def display_contact_book():
    if not contact_book:
        print("\nContact book is empty.\n")
        return

    print("\n------ Contact Book ------")
    for name, number in contact_book.items():
        print(f"{name:<15} : {number}")
    print()


def add_contact():
    name = input("Enter contact name: ").strip()

    if name in contact_book:
        print("Contact already exists.\n")
        return

    try:
        number = int(input("Enter contact number: "))
        contact_book[name] = number
        print("Contact added successfully!\n")
    except ValueError:
        print("Please enter a valid phone number.\n")


def remove_contact():
    name = input("Enter contact name to remove: ").strip()

    if name in contact_book:
        del contact_book[name]
        print("Contact removed successfully!\n")
    else:
        print("Contact not found.\n")


def search_contact():
    name = input("Enter contact name to search: ").strip()

    if name in contact_book:
        print(f"{name}'s Number: {contact_book[name]}\n")
    else:
        print("Contact not found.\n")


def menu():
    while True:
        print("=" * 35)
        print("      CONTACT BOOK MENU")
        print("=" * 35)
        print("1. Display Contact Book")
        print("2. Add Contact")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("5. Exit")

        try:
            choice = int(input("\nEnter your choice (1-5): "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        if choice == 1:
            display_contact_book()

        elif choice == 2:
            add_contact()

        elif choice == 3:
            remove_contact()

        elif choice == 4:
            search_contact()

        elif choice == 5:
            print("\nThank you for using Contact Book!")
            break

        else:
            print("Invalid choice! Please try again.\n")


menu()