from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Camper List')
listFrame = Frame(root)


global names, weeks, notes
names = ['Joe', 'Marc', 'Emma', 'Brian']
def msg(*args):
    messagebox.showinfo(f'{names[0]} Info', f'{names[0]} is')

def add():
    nameBox.insert(END, 'e')
    


button = Button(listFrame, text = 'touch me', command = add)

listVar = StringVar(value=names)
nameBox = Listbox(listFrame, height = 3, listvariable = listVar)

weeks = [['Week 1', 'Week 3', 'Week 4'], ['Week 2', 'Week 3'], ['Week 6'], ['Week 6', 'Week 7']]
#weekListVar = StringVar(value=weeks)
#weekBox = Listbox(listFrame, height = 3, listvariable = weekListVar)
notes = ['AAAAAAAAA', 'BBBBBBBB', 'CCCCCCCCCCC', 'DDDDDDD']



listFrame.grid(padx = 10, pady = 10)
nameBox.grid(row  = 1, column = 1)
#weekBox.grid(row = 1, column = 2)
button.grid(row = 2, column = 1)


root.mainloop
