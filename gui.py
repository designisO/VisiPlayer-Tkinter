from tkinter import *
from tkinter import filedialog

# The Menu Creation

def new_file():
    text.delete(0.0, END)

# New File function
def file_new():
    file_new_frame.pack(fill="both", expand=1)

# To open a new file


def open_file():
    file1 = filedialog.askopenfile(mode='r')
    data = file1.read()
    text.delete(0.0, END)
    text.insert(0.0, data)

# To save a file


def save_file():
    filename = "Untiled.txt"
    data = txt.get(0.0, END)
    file1 = open(filename, 'w')
    file1.write(data)

# I Hope you understand the code. No cheating Sir / Maam.
# Created by DesignIsOrion

# To save as


def save_as():
    file1 = filedialog.asksaveasfile(mode-'w')
    data = text.get(0.0, END)
    file1.write(data)



# GUI Code

root = Tk()
root.title("VisiNote App")
root.geometry("300x600")
root.config(bg="black")


# Main Screen


# Menu
mymenu = Menu(root)
root.config(menu=mymenu)
list1 = Menu()
list1.add_command(label="New file", command=file_new)
list1.add_command(label="Open file", command=open_file)
list1.add_command(label="Save", command=save_file)

file_new_frame = Frame(root, width=300, height=600, bg="green")


# Created by Orion3000

mymenu.add_cascade(label="File", menu=list1)


root.config(menu=mymenu)
root.mainloop()

