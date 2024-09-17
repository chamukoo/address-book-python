import tkinter as tk
from tkinter import messagebox, simpledialog

# Lists to hold contact information
contactsList = [" "]
firstnames = []
lastnames = []
addresses = []
numbers = []


# Main window
root = tk.Tk()
root.title("Address Book")
root.geometry("450x250")


# Function to display the main menu
def mainMenu():
    # Clear the current content
    for widget in root.winfo_children():
        widget.destroy()

    # Create a frame for the menu on the left side
    menu_frame = tk.Frame(root, width=200)
    menu_frame.pack(side="left", fill="y")

    # Title
    title = tk.Label(menu_frame, text="MAIN MENU", font=("Helvetica", 16))
    title.pack(pady=10)

    # Buttons for different menu options
    tk.Button(menu_frame, text="Add Contact", width=20, command=addContact).pack(pady=5, padx=10)
    tk.Button(menu_frame, text="Edit Contact", width=20, command=editContact).pack(pady=5, padx=10)
    tk.Button(menu_frame, text="Delete Contact", width=20, command=deleteContact).pack(pady=5, padx=10)
    tk.Button(menu_frame, text="Search Address Book", width=20, command=searchContact).pack(pady=5, padx=10)
    tk.Button(menu_frame, text="Exit", width=20, command=exitProgram).pack(pady=5)

    # Create a frame for displaying contacts on the right side
    contacts_frame = tk.Frame(root, width=150, bg="lightgrey")
    contacts_frame.pack(side="right", fill="both", padx=10, pady=20, expand=True)

    # Create a scrollbar
    scrollbar = tk.Scrollbar(contacts_frame, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    # Create a listbox to display the first and last names
    contacts_listbox = tk.Listbox(contacts_frame, yscrollcommand=scrollbar.set, font=("Helvetica", 10))
    contacts_listbox.pack(side="left", fill="both", expand=True)

    # Configure scrollbar to scroll the listbox
    scrollbar.config(command=contacts_listbox.yview)

    # Display only the first and last names in the listbox
    for index, contact in enumerate(contactsList[1:], start=1):
        contacts_listbox.insert(tk.END, f"{index}. {firstnames[index-1]} {lastnames[index-1]}")


# Function to add a contact
def addContact():
    def submit():
        first = first_entry.get()
        last = last_entry.get()
        address = address_entry.get()
        phone = phone_entry.get()

        if not first or not last or not address or not phone:
            messagebox.showerror("Error", "All fields are required!")
            return

        # Add details to respective lists
        firstnames.append(first)
        lastnames.append(last)
        addresses.append(address)
        numbers.append(phone)
        contact = f"{first: <20}{last: <20}{address: <60}{phone: <15}"
        contactsList.append(contact)

        messagebox.showinfo("Success", "The contact has been successfully added!")
        add_window.destroy()
        mainMenu()

    # Open a new window for adding a contact
    add_window = tk.Toplevel(root)
    add_window.title("Add Contact")
    add_window.geometry("350x250")
    add_window.configure(bg='light pink')

    # Create a canvas for custom background
    canvas = tk.Canvas(add_window, width=310, height=210, bg='light pink', highlightthickness=0)
    canvas.pack(pady=10)

    # Create a rounded rectangle with shadow
    canvas.create_rectangle(10, 10, 370, 270, fill='white', outline='white', width=0)
    canvas.create_rectangle(15, 15, 365, 265, fill='white', outline='white', width=0)

    # Create a frame on top of the canvas
    form_frame = tk.Frame(add_window, bg='white')
    form_frame.place(x=20, y=20, width=300, height=200)

    # Form fields
    tk.Label(form_frame, text="First Name:", bg='white').grid(row=0, column=0, padx=10, pady=7, sticky='w')
    first_entry = tk.Entry(form_frame)
    first_entry.grid(row=0, column=1, padx=10, pady=6)

    tk.Label(form_frame, text="Last Name:", bg='white').grid(row=1, column=0, padx=10, pady=7, sticky='w')
    last_entry = tk.Entry(form_frame)
    last_entry.grid(row=1, column=1, padx=10, pady=6)

    tk.Label(form_frame, text="Address:", bg='white').grid(row=2, column=0, padx=10, pady=7, sticky='w')
    address_entry = tk.Entry(form_frame)
    address_entry.grid(row=2, column=1, padx=10, pady=6)

    tk.Label(form_frame, text="Phone Number:", bg='white').grid(row=3, column=0, padx=10, pady=7, sticky='w')
    phone_entry = tk.Entry(form_frame)
    phone_entry.grid(row=3, column=1, padx=10, pady=7)

    # Submit button
    tk.Button(form_frame, text="Submit", command=submit, bg='pink', fg='black').grid(row=4, columnspan=2, pady=10)

# Function to edit a contact
def editContact():
    entry_num = simpledialog.askinteger("Input", "Enter the entry number you want to modify:")
    if entry_num is None or entry_num >= len(contactsList) or entry_num < 1:
        messagebox.showerror("Error", "Invalid Entry Number!")
        return

    first = simpledialog.askstring("Input", "Enter New First Name:")
    last = simpledialog.askstring("Input", "Enter New Last Name:")
    address = simpledialog.askstring("Input", "Enter New Address:")
    phone = simpledialog.askstring("Input", "Enter New Contact Number:")

    # Modify the contact
    modifiedContact = f"{first: <20}{last: <20}{address: <60}{phone: <15}"
    contactsList[entry_num] = modifiedContact
    firstnames[entry_num-1] = first
    lastnames[entry_num-1] = last
    addresses[entry_num-1] = address
    numbers[entry_num-1] = phone

    messagebox.showinfo("Success", "Contact modified successfully!")
    mainMenu()


# Function to delete a contact
def deleteContact():
    entry_num = simpledialog.askinteger("Input", "Enter the entry number you want to delete:")
    if entry_num is None or entry_num >= len(contactsList) or entry_num < 1:
        messagebox.showerror("Error", "Invalid Entry Number!")
        return

    contactsList.pop(entry_num)
    firstnames.pop(entry_num-1)
    lastnames.pop(entry_num-1)
    addresses.pop(entry_num-1)
    numbers.pop(entry_num-1)

    messagebox.showinfo("Success", "Contact deleted successfully!")
    mainMenu()


# Function to search contacts
def searchContact():
    def display_search_results(search_term):
        result_window = tk.Toplevel(root)
        result_window.title("Search Results")
        result_window.geometry("700x500")

        header = tk.Label(result_window, text="Entry\t\tFirst Name\t\tLast Name\t\tAddress\t\tPhone Number", font=("Helvetica", 12))
        header.pack(pady=5)

        found = False
        for index, contact in enumerate(contactsList[1:], start=1):
            if search_term.lower() in contact.lower():
                result_label = tk.Label(result_window, text=f"{index}\t\t{contact}", font=("Helvetica", 10))
                result_label.pack()
                found = True

        if not found:
            result_label = tk.Label(result_window, text="No contacts found!", font=("Helvetica", 12), fg="red")
            result_label.pack(pady=10)

    search_term = simpledialog.askstring("Input", "Enter a search term (name/address/phone):")
    if search_term:
        display_search_results(search_term)


# Function to exit the program
def exitProgram():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.quit()


# Start the program with the main menu
mainMenu()

# Run the Tkinter event loo
root.mainloop()
