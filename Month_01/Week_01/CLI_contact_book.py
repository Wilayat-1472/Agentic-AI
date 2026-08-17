

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display_contact(self):
        print(f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}")

contact_list = [
    Contact("ali","1234567890","ali@example.com"),
    Contact("ahmed","0987654321","ahmed@example.com"),
    Contact("sara","5555555555","sara@example.com")]

        

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
            contact_list.append(Contact(name, phone, email))
            print("Contact added successfully!")
    elif choice == "2":
        print("contact_list:")
        for c in contact_list:
            c.display_contact()
    elif choice == "3":
        search_name=input("Enter the name of the contact to search: ").strip()
        for c in contact_list:
            if c.name == search_name:
                c.display_contact()
                break
        else:
            print("Contact not found.")

    elif choice == "4":
        delete_name=input("Enter the name of the contact to delete: ")
        for c in contact_list:
            if c.name == delete_name:
               contact_list.remove(c)
               print("Contact deleted.")
               break
        else:
           print("Contact not found.")
    elif choice == "5":
            print("Exiting...")
            break
    else:
            print("Invalid choice. Please enter a number between 1 and 5.")
    
