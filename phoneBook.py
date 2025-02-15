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