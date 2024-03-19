import tkinter as tk

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get("1.0", "end-1c")
    
    contacts_list.insert(tk.END, name)
    contact_dict[name] = {"phone": phone, "email": email, "address": address}
    
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete("1.0", tk.END)
    
def view_contact():
    name = contacts_list.get(contacts_list.curselection())
    phone = contact_dict[name]["phone"]
    email = contact_dict[name]["email"]
    address = contact_dict[name]["address"]
    
    name_entry.insert(0, name)
    phone_entry.insert(0, phone)
    email_entry.insert(0, email)
    address_entry.insert("1.0", address)
    
root = tk.Tk()
root.title("Address Book")
root.geometry("500x500")

name_label = tk.Label(root, text="Name")
phone_label = tk.Label(root, text="Phone")
email_label = tk.Label(root, text="Email")
address_label = tk.Label(root, text="Address")

name_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
email_entry = tk.Entry(root)
address_entry = tk.Text(root, height=5, width=30)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
view_button = tk.Button(root, text="View Contact", command=view_contact)

contacts_list = tk.Listbox(root)
contact_dict = {}

name_label.grid(row=0, column=0, sticky="W")
phone_label.grid(row=1, column=0, sticky="W")
email_label.grid(row=2, column=0, sticky="W")
address_label.grid(row=3, column=0, sticky="W")

name_entry.grid(row=0, column=1)
phone_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
address_entry.grid(row=3, column=1, rowspan=2)

add_button.grid(row=5, column=0, sticky="W")
view_button.grid(row=5, column=1, sticky="W")

contacts_list.grid(row=0, column=2, rowspan=6)

root.mainloop()