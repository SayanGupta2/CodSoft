class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact.name} - {contact.phone_number} - {contact.email} - {contact.address}")

    def search_contact(self, keyword):
        matching_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                matching_contacts.append(contact)
        if not matching_contacts:
            print("No matching contacts found.")
        else:
            print("\nMatching Contacts:")
            for index, contact in enumerate(matching_contacts, start=1):
                print(f"{index}. {contact.name} - {contact.phone_number} - {contact.email} - {contact.address}")

    def update_contact(self, contact_index, new_phone_number, new_email, new_address):
        if 0 <= contact_index < len(self.contacts):
            contact = self.contacts[contact_index]
            contact.phone_number = new_phone_number
            contact.email = new_email
            contact.address = new_address
            print("Contact updated successfully!")
        else:
            print("Invalid contact index.")

    def delete_contact(self, contact_index):
        if 0 <= contact_index < len(self.contacts):
            del self.contacts[contact_index]
            print("Contact deleted successfully!")
        else:
            print("Invalid contact index, No contact Found.")

def main():
    contact_book = ContactBook()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_book.search_contact(keyword)
        elif choice == '4':
            contact_index = int(input("Enter contact index to update: "))
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_book.update_contact(contact_index - 1, new_phone_number, new_email, new_address)
        elif choice == '5':
            contact_index = int(input("Enter contact index to delete: "))
            contact_book.delete_contact(contact_index - 1)
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
