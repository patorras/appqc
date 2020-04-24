from tkinter import *
import sqlite3
import datetime
from PIL import ImageTk, Image

root = Tk()

root.title("Samples entry")
root.geometry("500x600")



#########################################################################################################################################
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

    # Shows what was just inserted
    my_label = Label(root, text=e_batch.get())
    my_label.grid(row=2, column=1, pady=(100, 0))

    # deletes the entry box
    e_batch.delete(0, END)

##############################################################################################################################################

def edit():
    second = Tk()
    second.geometry("500x600")
    second.title("Edit Window")

    # label
    label_id = Label(second, text="ID")
    label_id.grid(row=0, column=0)

    label_batch = Label(second, text="Batch")
    label_batch.grid(row=1, column=0)

    label_moment = Label(second, text="Moment")
    label_moment.grid(row=2, column=0)

    label_date = Label(second, text="Date")
    label_date.grid(row=3, column=0)

    # Entry boxes
    e_id = Entry(second, width=35)
    e_id.grid(row=0, column=1)

    e_batch = Entry(second, width=35)
    e_batch.grid(row=1, column=1)

    e_moment = Entry(second, width=35)
    e_moment.grid(row=2, column=1)

    e_date = Entry(second, width=35)
    e_date.grid(row=3, column=1)



##############################################################################################################################################

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

# Edit
edit = Button(root, text="Edit", command=edit)
edit.grid(row=3, columnspan=3, pady=(10, 0))




root.mainloop()
