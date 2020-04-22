# tkinter Cheat Sheet


### imports:
``` python
# imports everything
from tkinter import *
# import PIL to be used for images
from PIL import ImageTk, Image
```
---

### Main_Functions:
```python
Tk() # creates the main window
```
* root.geometry: size of the window
* root.title: Title of the window
* root.iconbitmap: the icon of the window

##### Example:
```python
# creates the main window
root = Tk()
# Size of the window
root.geometry("400x400")
# Title of the Window
root.title("Database")
# adds a icon to the window, in linux needs to be "xbm" file and use a "@" before it,
#in windows needs to be type .ico
root.iconbitmap("@""icon.xbm")
```
---
##### Tkinter Variables

* Tkinter variables are a bit different

> Examples:
```python
v = StringVar() # initialize the Tkinter variable in this case a string
e = Entry(root, textvariable=v).pack() # creates a insert box, what you write there is assign to v
s = v.get() # s gets what was inserted to the box
----------------------------------------------------------------------------
i = IntVar()
b = BooleanVar()
d = DoubleVar()

```

---
#### Create a new Window
```python
# creates a new window and assigns it to top
top = Toplevel()
# defines the name of the window
top.title("Second Widnow")
# Size of the window
root.geometry("400x400")
```
---
#### Label_Widget:
```python
# Creates a label widget, can be used for display text or images in the screen
>Label()
```
* 1st parameter the window where the button will appear
* text: the string that appears in the button, or a variable
* image: to show a image in the screen

Examples:
```python
# Just shows to the screen the text My label
my_label = Label(root, text="My label").pack()
# Just shows to the screen the variable var
my_Label = Label(root, text=var).pack()
# Just shows to the screen the image (need to create first the image variable)
my_Label = Label(root, image=my_img).pack()
# Gets the value that was passed by the varable get
my_label= Label(root, text=var.get())
```
---

#### Button_Widget:
```python
# Creates a button widget
Button()
```
* 1st parameter the window where the button will appear
* text: the string that appears in the button, or a variable
* command: a function to do sometinh, use lambda if is necessary to pass arguments to the function
* command: top.destroy, will close the window

Examples
```python
my_button = Button(root, text="Click Me", command=function).pack()
my_button = Button(root, text="Click Me", command=lambda: function()).pack()
# will close the window
btn2 = Button(root, text="Close Window", command=top.destroy).pack()
# fg and bg is the color of the letter and the background
myButton = Button(root, text="Click me", command=myClick, fg="blue", bg="red")
```
---
#### Insert images
```python
# defines a variable of a image
my_imgage = ImageTk.PhotoImage(Image.open('images/iamge.jpg'))
```
* after that image variable we need to assign it to a Label

Example:
```python
my_label = Label(root, image=my_imgage).pack()
```
---

#### Entry Boxes
```python
# Create Entry box
f_name = Entry(root, width=30)
f_name.grid(row=0 ,column=1, padx=20, pady=(10, 0))
```
* 1 argument is the window we want to show it
* width is the width of the entry Box
* the pay with a tuple the first number is the bottom y axis and the second is the top y axis
* Normally is accompany by a label widget
* We can use the entry.insert, to insert some variable or text to the box
* The entry.get() to grab what was passed to the entry box is also possible
* The entry.delete() will delete what is in the entry box at the moment, from 0 to END or what you prefer

>Examples:
```python
f_name = Entry(root, width=30)
f_name.grid(row=0 ,column=1, padx=20, pady=(10, 0))
f_name.get()
f_name.insert(0, var))
f_name.delete(0, END)
```
