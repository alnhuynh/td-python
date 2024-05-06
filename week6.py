# tkinter test
from tkinter import *

main = Tk()
main.title("My Bomb")
Label(main, text="This is the bomb:", font=("", 10, "bold"),
height=2).grid(row=0, column=0)
Label(main, text="An entry example:", height=2).grid(row=1, column=0)
widget1 = Entry(main, width=40)
widget1.grid(row=1, column=1)
Label(main, text="A checkbox example:", height=2).grid(row=2, column=0)
widget2 = Checkbutton(main, text="Smart")
widget2.grid(row=2, column=1)
Label(main, text="A radiobutton example:", height=2).grid(row=3, column=0)
foo=IntVar()
widget3 = Radiobutton(main, text="Armed", variable=foo, value=1)
widget3.grid(row=3, column=1)
widget4 = Radiobutton(main, text="Disarmed", variable=foo, value=2)
widget4.grid(row=4, column=1)

# Make a listbox with a scrollbar. Don't worry about the scrollbar
# placement... we'll fix this when we dive deeper into layouts
Label(main, text="A listbox with scrollbar example:", height=2).grid(row=5,
column=0)
choices = ["Small", "Medium", "Large", "Mondo", "Gargantuan", "Wow"]

widget5 = Listbox(main, height=4, selectmode=SINGLE)
for size in choices:
    widget5.insert(END, size)

widget6 = Scrollbar(main, command=widget5.yview)
widget5.configure(yscrollcommand=widget6.set)
widget5.grid(row=5, column=1)
widget6.grid(row=5, column=2)

Label(main, text="A slider example:", height=2).grid(row=6, column=0)
widget7 = Scale(main, orient=HORIZONTAL, length=100, from_=0, to=100,
tickinterval=25, showvalue=TRUE)
widget7.grid(row=6, column=1)

Label(main, text="A multi-line text example:", height=2).grid(row=7, column=0)
widget8 = Text(main, height=4, width=40)
widget8.grid(row=7, column=1)

Label(main, text="A button example:", height=2).grid(row=8, column=0)
widget10 = Button(main, text="Boom")
widget10.grid(row=8, column=1)
main.mainloop()