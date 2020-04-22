from tkinter import *

root = Tk()

root.title("Samples entry")

# batch label
label_batch = Label(root, text="Batch")
label_batch.grid(row=0, column=0)

# label for moment
label_moment = Label(root, text="Moment")
label_moment.grid(row=0, column=1)


# batch entry box
e_batch = Entry(root, width=35)
e_batch.grid(row=1, column=0)

# moment entry box
e_moment = Entry(root, width=35)
e_moment.grid(row=1, column=1)


# button
ok_button = Button(root, width=35, text="OK")
ok_button.grid(row=2, column=0)

root.mainloop()
