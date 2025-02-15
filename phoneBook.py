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

