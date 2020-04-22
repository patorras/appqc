from tkinter import *
from PIL import ImageTk; Image
import sqlite3

root = Tk()
root.geometry("400x600")
root.title("Database")

# create a Database or connect to one
conn = sqlite3.connect('address_book.db')

# creates a crusor,
c = conn.cursor()

# create table
# since the table is created no need to create it everytine

#c.execute("""CREATE TABLE addresses (
        #first_name text,
        #last_name text,
        #address text,
        #city text,
        #state text,
        #zipcode integer
        #)""")

###############################################################################################################################################

# update function, will edit a record
def update():
    editor = Tk()
    editor.geometry("400x600")
    editor.title("Update a record")

    # Create Entry box
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0 ,column=1, padx=20, pady=(10, 0)) # the pady like that is for specific top and bottom, first numer is the top

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1 ,column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2 ,column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3 ,column=1)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4 ,column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5 ,column=1)


    # Create text box labels
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))

    l_name_label_editor = Label(editor, text="last Name")
    l_name_label_editor.grid(row=1, column=0)

    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)

    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)

    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column=0)

    zipcode_label_editor = Label(editor, text="zipcode")
    zipcode_label_editor.grid(row=5, column=0)

    # create save Button
    save_button = Button(editor, text="Save", command=update)
    save_button.grid(row=6, column=0, columnspan=2, pady=10, padx=30, ipadx=145)

    # create a Database or connect to one
    conn = sqlite3.connect('address_book.db')

    # creates a crusor,
    c = conn.cursor()

    # grabs the id number that is in the SELECT id number box in the root window
    redcord_id = delete_box.get()

    #query the database, oid means that we want to see the id's as well
    c.execute("SELECT * FROM addresses WHERE oid=" + redcord_id)
    records = c.fetchall()

    # loop thru results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])



    # creates a label to show the records
    query_label = Label(root, text=print_records)
    query_label.grid(row=13, column=0, columnspan=2)

    # commit changes
    conn.commit()

    # Close connection
    conn.close()




###############################################################################################################################################################

# Function to delete Entry
def delete():
    # create a Database or connect to one
    conn = sqlite3.connect('address_book.db')

    # creates a crusor,
    c = conn.cursor()

    # delete a record
    c.execute("DELETE from addresses WHERE oid=" + delete_box.get())

    # commit changes
    conn.commit()

    # Close connection
    conn.close()



# Create a submit function for the Database
def submit():
    # create a Database or connect to one
    conn = sqlite3.connect('address_book.db')

    # creates a crusor,
    c = conn.cursor()

    # Insert into adresses TABLE
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
            # create a dictionary to add the values
            {
                "f_name": f_name.get(),
                "l_name": l_name.get(),
                "address": address.get(),
                "city": city.get(),
                "state": state.get(),
                "zipcode": zipcode.get()
            })

    # commit changes
    conn.commit()

    # Close connection
    conn.close()

    # deletes the text in the entry boxes after submit
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# create query function to see the Records
def query():
    # create a Database or connect to one
    conn = sqlite3.connect('address_book.db')

    # creates a crusor,
    c = conn.cursor()

    #query the database, oid means that we want to see the id's as well
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()

    # Loop Thru results
    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "  " + str(record[6]) + "\n"

    # creates a label to show the records
    query_label = Label(root, text=print_records)
    query_label.grid(row=13, column=0, columnspan=2)

    # commit changes
    conn.commit()

    # Close connection
    conn.close()



# Create Entry box
f_name = Entry(root, width=30)
f_name.grid(row=0 ,column=1, padx=20, pady=(10, 0)) # the pady like that is for specific top and bottom, first numer is the top

l_name = Entry(root, width=30)
l_name.grid(row=1 ,column=1)

address = Entry(root, width=30)
address.grid(row=2 ,column=1)

city = Entry(root, width=30)
city.grid(row=3 ,column=1)

state = Entry(root, width=30)
state.grid(row=4 ,column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5 ,column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=10, column=1)

# Create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row=5, column=0)

delete_label = Label(root, text="Select ID Number")
delete_label.grid(row=10, column=0)




# Create submit button
submit_button = Button(root, text="Add record to Database", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=110,)

# Create a Query Button
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=(5, 10), padx=10, ipadx=137)

# Create delete Button
delete_button = Button(root, text="Delete Entry With ID", command=delete)
delete_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=116)

# Create a update button
update_button = Button(root, text="Update Record with ID", command=update)
update_button.grid(row=12, column=0, columnspan=2, pady=2, padx=10, ipadx=110)

# commit changes
conn.commit()

# Close connection
conn.close()



root.mainloop()
