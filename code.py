import mysql.connector
from tkinter import *
from tkinter import messagebox

# connecting mysql
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",   
        password="",  
        database="healthcare_system"
    )

# Function to add patient to database
def add_patient():
    con = connect_db()
    cursor = con.cursor()
    
    sql = "INSERT INTO patients (name, age, gender, contact, address) VALUES (%s, %s, %s, %s, %s)"
    values = (name_entry.get(), age_entry.get(), gender_var.get(), contact_entry.get(), address_entry.get())
    
    cursor.execute(sql, values)
    con.commit()
    con.close()
    
    messagebox.showinfo("Success", "Patient Added Successfully!")
    clear_entries()
    view_patients()

# Function to view all patients
def view_patients():
    con = connect_db()
    cursor = con.cursor()
    
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    
    patient_list.delete(0, END)  
    for row in rows:
        patient_list.insert(END, row)
    
    con.close()

# Function to clear input fields
def clear_entries():
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    contact_entry.delete(0, END)
    address_entry.delete(0, END)
    gender_var.set("")


root = Tk()
root.title("Healthcare Management System")
root.geometry("600x400")

# Labels and Entries
Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=10)
age_entry = Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=10)

Label(root, text="Gender:").grid(row=2, column=0, padx=10, pady=10)
gender_var = StringVar()
gender_entry = OptionMenu(root, gender_var, "Male", "Female", "Other")
gender_entry.grid(row=2, column=1, padx=10, pady=10)

Label(root, text="Contact:").grid(row=3, column=0, padx=10, pady=10)
contact_entry = Entry(root)
contact_entry.grid(row=3, column=1, padx=10, pady=10)

Label(root, text="Address:").grid(row=4, column=0, padx=10, pady=10)
address_entry = Entry(root)
address_entry.grid(row=4, column=1, padx=10, pady=10)

# Buttons
Button(root, text="Add Patient", command=add_patient).grid(row=5, column=0, columnspan=2, pady=10)
Button(root, text="View Patients", command=view_patients).grid(row=6, column=0, columnspan=2, pady=10)

# Listbox to display patients
patient_list = Listbox(root, height=10, width=50)
patient_list.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
