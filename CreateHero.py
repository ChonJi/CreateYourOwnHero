from tkinter import *
from PIL import ImageTk, Image

from BattleMage import BattleMage
from Warrior import Warrior
from Mage import Mage
from Peasant import Peasant


def click():

    try:
        name = hero_name_textentry.get()
        life = life_textentry.get()
        mana = mana_textentry.get()

        if int(life) >= 100 and int(mana) <= 99:
            character = Warrior(name, life, mana)
        elif int(life) >= 100 and int(mana) >= 100:
            character = BattleMage(name, life, mana)
        elif int(life) <= 99 and int(mana) >= 100:
            character = Mage(name, life, mana)
        else:
            character = Peasant(name, life, mana)

        output.delete(0.0, END)
        output.insert(END, character)

    except:
        output.delete(0.0, END)
        output.insert(END, 'Wypełnij, proszę, wszystkie pola.')

def close_window():
    my_app.destroy()
    exit()

my_app = Tk()
my_app.title('CREATE YOUR OWN MUM!')
my_app.configure(background = 'black')

logo = ImageTk.PhotoImage(Image.open('photos\layout.jpg'))

Label(my_app, image = logo, bg = 'black').grid(sticky = N)
Label(my_app, text = "Hero's Name:", bg = 'black', fg = 'white', font = 'gothic 10').grid(row = 1, sticky = W)
Label(my_app, text = 'Life:', bg = 'black', fg = 'white', font = 'gothic 10', bd = 1).grid(row = 3, sticky = W)
Label(my_app, text = 'Mana:', bg = 'black', fg = 'white', font = 'gothic 10', bd = 1).grid(row = 5, sticky = W)

hero_name_textentry = Entry(my_app, width = 13, bg ='white')
hero_name_textentry.grid(row = 2, sticky = W)
life_textentry = Entry(my_app, width = 13, bg ='white')
life_textentry.grid(row = 4, sticky = W)
mana_textentry = Entry(my_app, width = 13, bg ='white')
mana_textentry.grid(row = 6, sticky = W)

Button(my_app, text = 'Create a hero!', width = 11, command = click).grid(row = 12, pady = 1, sticky = W)
Button(my_app, text = "I don't want to create another hero!", width = 29, command = close_window).grid(row = 12, sticky = E)

output = Text(my_app, width = 53, height = 6, wrap = WORD, bg = 'white')
output.grid(row = 11, pady = 10, columnspan = 2, sticky = N)

my_app.mainloop()