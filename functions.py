def add_contact(contacts, name, phone, email):
  try:
    contact = {
      "name": name,
      "phone": phone,
      "email": email,
      "favorite": False
    }
    contacts.append(contact)
    print("Contact added successfully")
  except Exception as e:
    print("An error occurred: ", e)

def list_contacts(contacts):
  for index, contact in enumerate(contacts):
    favorite = '[✔]' if contact["favorite"] else '[ ]'
    print("\n Contact ID: ", index + 1)
    print('#----------------------#')
    print("Name: ", contact["name"])
    print("Phone: ", contact["phone"])
    print("Email: ", contact["email"])
    print("Favorite: ", favorite)
    print('#----------------------#')

def edit_contact(contacts, contact_id, name, phone, email):
  try:
    formatted_contact_id = eval(contact_id) -1
    contact = contacts[formatted_contact_id]
    contact["name"] = name
    contact["phone"] = phone
    contact["email"] = email
    print("Contact updated successfully")
  except Exception as e:
    print("An error occurred: ", e)

def mark_as_favorite(contacts, contact_id):
  try:
    formatted_contact_id = eval(contact_id) - 1
    contact = contacts[formatted_contact_id]
    contact['favorite'] = True
    print("Contact marked as favorite")
  except Exception as e:
    print("An error occurred: ", e)

def list_favorites(contacts):
  for index, contact in enumerate(contacts):
    if contact['favorite']:
      favorite = '[✔]' if contact["favorite"] else '[ ]'
      print("\n Contact ID: ", index + 1)
      print('#----------------------#')
      print("Name: ", contact["name"])
      print("Phone: ", contact["phone"])
      print("Email: ", contact["email"])
      print("Favorite: ", favorite)
      print('#----------------------#')

def delete_contact(contacts, contact_id):
  try:
    formatted_contact_id = eval(contact_id) - 1
    contacts.pop(formatted_contact_id)
    print("Contact deleted successfully")
  except Exception as e:
    print("An error occurred: ", e)