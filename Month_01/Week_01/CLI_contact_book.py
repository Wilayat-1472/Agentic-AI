contact=[{"name":"ali","phone":"1234567890","email":"ali@example.com"},
         {"name":"ahmed","phone":"0987654321","email":"ahmed@example.com"},
         {"name":"sara","phone":"5555555555","email":"sara@example.com"}]

while True:
    print("Welcome to the Contact Book CLI!")
    print("Please choose an option:")
    print("1. Add a contact")
    print("2. View contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")

    choice= input("Enter your choice (1-5):")

    if choice == "1":
        name=input("Enter contact name: ")
        phone=input("Enter contact phone number: ")
        email=input("Enter contact email address: ")
        contact.append({"name": name, "phone": phone, "email": email})
    elif choice == "2":
        print("contact_list:")
        for c in contact:
         print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
    elif choice == "3":
        search_name=input("Enter the name of the contact to search: ")
        for c in contact:
            if c['name'] == search_name:
                print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
                break
        else:
            print("Contact not found.")
    elif choice == "4":
        delete_name=input("Enter the name of the contact to delete: ")
        for c in contact:
            if c['name'] == delete_name:
                contact.remove(c)
                print("Contact deleted.")
                break
        else:
            print("Contact not found.")
    elif choice == "5":
        print("Exiting...")
        break
    
