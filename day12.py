import csv
import os
FILENAME = "contacts.csv"
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    #check for duplicates
    with open(FILENAME, "a", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
           if row["Name"].lower() == name.lower():
               print("Contact name already exists")
               return
    
    with open(FILENAME, 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("Contact added")


def view_contacts():
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) < 1:
            print("No contacts found")
            return
        
        print("\n Your contacts: \n")

        for row in rows[1:]:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()

def search_contact():
    term = input("Enter the name to search: ").strip().lower()
    found = False

    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower():
                print(f"{row['Name']} | 📞 {row['Phone']} | ✉️ {row['Email']}")
                found = True

    if not found:
        print("No matching contact found")
def update_contact():
    name = input("Enter the contact name to update: ").strip()

    contacts = []
    found = False

    with open(FILENAME, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["Name"].lower() == name.lower():
                print("\nContact Found!")
                print(f"Current Phone : {row['Phone']}")
                print(f"Current Email : {row['Email']}")

                new_phone = input("Enter new phone: ").strip()
                new_email = input("Enter new email: ").strip()

                row["Phone"] = new_phone
                row["Email"] = new_email

                found = True

            contacts.append(row)

    if found:
        with open(FILENAME, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["Name", "Phone", "Email"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(contacts)

        print("✅ Contact updated successfully.")
    else:
        print("❌ Contact not found.")


def delete_contact():
    name = input("Enter the contact name to delete: ").strip()

    contacts = []
    found = False

    with open(FILENAME, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["Name"].lower() == name.lower():
                found = True
                continue      # Skip this contact
            contacts.append(row)

    if found:
        with open(FILENAME, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["Name", "Phone", "Email"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(contacts)

        print("🗑️ Contact deleted successfully.")
    else:
        print("❌ Contact not found.")



def main():

    while True:
        print("\n📒 Contact Book")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thanks for using our software.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()


