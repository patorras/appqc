from tkinter import *
import sqlite3
from datetime import date
import datetime

root = Tk()

root.title("Samples entry")
root.geometry("500x600")


# connects to database
#conn = sqlite3.connect('samples.db')

# Create a cursor
#c = conn.cursor()

# Create TABLE
#c.execute("""CREATE TABLE samples (
        #batch text,
        #moment text,
        #date datetime)""")



# function to submit entrys
def submit():
    # connects to database
    conn = sqlite3.connect('samples.db')

    # Create a cursor
    c = conn.cursor()

    # Fills the table
    c.execute("INSERT INTO samples VALUES(:batch, :moment, :date)",
    {
        "batch": e_batch.get(),
        "moment": clicked.get(),
        "date": datetime.datetime.now()
    })

    # commit the data
    conn.commit()

    # Close the connection
    conn.close()




# batch label
label_batch = Label(root, text="Batch")
label_batch.grid(row=0, column=0, pady=(20, 0))

# batch entry box
e_batch = Entry(root, width=35)
e_batch.grid(row=0, column=1, pady=(20, 0))

# dropdown box
# list of option
options = ["in", "out"]
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.config(width=5, font=('Helvetica', 12))
drop.grid(row=0, column=2, pady=(20, 0))


# submit button
submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=1, columnspan=3, pady=(10, 0))


root.mainloop()
