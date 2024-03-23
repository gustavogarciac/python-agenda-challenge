contacts = []

from functions import add_contact, list_contacts, edit_contact, mark_as_favorite, list_favorites, delete_contact

while True:
  print("\n ========# Contact Agenda #=========")
  print("1. Add Contact")
  print("2. List Contacts")
  print("3. Edit Contact")
  print("4. Mark as Favorite")
  print("5. List Favorites")
  print("6. Delete Contact")
  print("7. Exit")

  option = input("Please select an option: ")

  if option == "1":
    contact_name = input("Please enter the contact name: ")
    contact_phone = input("Please enter the contact phone: ")
    contact_email = input("Please enter the contact email: ")
    add_contact(contacts, contact_name, contact_phone, contact_email)
  elif option == "2":
    list_contacts(contacts)
  elif option == "3": 
    list_contacts(contacts)
    contact_id = input("Please enter the contact ID: ")
    contact_name = input("Please enter the contact name: ")
    contact_phone = input("Please enter the contact phone: ")
    contact_email = input("Please enter the contact email: ")
    edit_contact(contacts, contact_id, contact_name, contact_phone, contact_email)
  elif option == '4':
    list_contacts(contacts)
    contact_id = input("Please enter the contact ID: ")
    mark_as_favorite(contacts, contact_id)
  elif option == '5':
    list_favorites(contacts)
  elif option == '6':
    list_contacts(contacts)
    contact_id = input("Please enter the contact ID: ")
    delete_contact(contacts, contact_id)
  elif option == "7":
    break

print("You selected option 7. Exiting...")