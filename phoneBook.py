contacts = []  

def add_contact():

    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact already exists!")
            return
    
    contacts.append({"name": name, "phone": phone})
    print("Contact added successfully!")

def view_contacts():
    
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        print("---------X-----------")

def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False
    for contact in contacts:
        if search_name in contact["name"].lower():
            print(f"Found: {contact['name']} - {contact['phone']}")
            found = True
    if not found:
        print("Contact not found.")

def delete_contact():
    delete_name = input("Enter name to delete: ").lower()
    for contact in contacts:
        if contact["name"].lower() == delete_name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")