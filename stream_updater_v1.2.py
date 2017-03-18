#smash 4 stream updater
#version 1.2 by Alonzo Castanon (github.com/alonzoc1)
#changes from v1.1:
# --now runs a GUI by default!
# --if anyone wants to make their own interface, they can use the
# now modular functions to change filenames

import os
import shutil
from tkinter import *
from tkinter.ttk import *
import string

#globals
T1 = ""

def change_player_tag(i, p):#if p = 1 change player one, if 2 change player 2
    if p==1:
        player1 = open('player1.txt','w')
        player1.write(i)
        player1.close()
    elif p==2:
        player2 = open('player2.txt','w')
        player2.write(i)
        player2.close()

def change_set_count(i, p):
    if p==1:
        set1 = open("set1.txt", "w")
        set1.write(i)
        set1.close()
    elif p==2:
        set2 = open("set2.txt", "w")
        set2.write(i)
        set2.close()

def change_match_title(i):
    match = open("match.txt", "w")
    match.write(i)
    match.close()

def change_fighter(i, p):
    if p==1:
        i += '.png'
        path = os.getcwd()
        path += "\\Ico\\"
        path2 = path+i
        path3 = path+"current1.png"
        try:
            shutil.copyfile(path2, path3)
        except:
            print("change_fighter failed, check filenames")
            return 0
    elif p==2:
        i += '.png'
        path = os.getcwd()
        path += "\\Ico\\"
        path2 = path + i
        path3 = path + "current2.png"
        try:
            shutil.copyfile(path2, path3)
        except:
            print("change_fighter failed, check filenames")
            return 0
    return 1


def main():
    def exe():
        change_player_tag(TAG1.get(), 1)
        change_player_tag(TAG2.get(), 2)
        change_set_count(SET1.get(), 1)
        change_set_count(SET2.get(), 2)
        change_match_title(MATCH.get())
        #print(FIGHTER1.get(),FIGHTER2.get())
        change_fighter(FIGHTER1.get(), 1)
        change_fighter(FIGHTER2.get(), 2)
    
    #gui
    top = Tk()
    top.wm_title("Smash 4 Stream Updater v1.2")
    top.resizable(0,0)
    TAG1 = StringVar()
    TAG2 = StringVar()
    SET1 = StringVar()
    SET2 = StringVar()
    MATCH = StringVar()
    FIGHTER1 = StringVar()
    FIGHTER2 = StringVar()
    #labels
    p1 = Label(top, text = "Tag 1")
    p2 = Label(top, text = "Tag 2")
    c1 = Label(top, text = "Character 1")
    c2 = Label(top, text = "Character 2")
    s1 = Label(top, text = "Set Count 1")
    s2 = Label(top, text = "Set Count 2")
    m = Label(top, text = "Match Title")

    p1.place(x=10, y=10)
    p2.place(x=10, y=30)
    c1.place(x=10, y=50)
    c2.place(x=10, y=70)
    s1.place(x=10, y=90)
    s2.place(x=10, y=110)
    m.place(x=10, y=130)

    #entry boxes
    p1e = Entry(top, textvariable = TAG1,width=18)
    p2e = Entry(top, textvariable = TAG2,width=18)
    s1e = Entry(top, textvariable = SET1,width=18)
    s2e = Entry(top, textvariable = SET2,width=18)
    me = Entry(top, textvariable = MATCH,width=18)

    p1e.place(x=90, y=10)
    p2e.place(x=90, y=30)
    s1e.place(x=90, y=90)
    s2e.place(x=90, y=110)
    me.place(x=90, y=130)
    #comboboxes

    fighters = ("bayonetta", "bowser", "bowser_jr", "captain_falcon", "charizard",
                "cloud", "corrin_female", "corrin_male", "dark_pit", "diddy_kong",
                "donkey_kong", "dr_mario", "duck_hunt", "falco", "fox", "ganondorf",
                "greninja", "gw", "ike", "jigglypuff",'king_dedede','kirby','link',
                'little_mac','lucario','lucas','lucina','luigi','mario','marth',
                'megaman','meta_knight','mewtwo','mii_fight','mii_gun','mii_sword',
                'ness','olimar','pacman','palutena','peach','pikachu','pit','rob',
                'robin_female','robin_male','rosalina','roy','ryu','samus','sheik',
                'shulk','sonic','toon_link','villager','wario','wft_female',
                'wft_male','yoshi','zelda','zss')#jesus
    c1c =Combobox(top, values=fighters, state="readonly", textvariable=FIGHTER1,width=15)
    c2c =Combobox(top, values=fighters, state="readonly", textvariable=FIGHTER2,width=15)

    c1c.place(x=90,y=50)
    c2c.place(x=90,y=70)
    execute = Button(top, text = "Execute!", command = exe)
    execute.place(x=60, y=170)
    top.geometry("220x200")
    top.mainloop()



if __name__ == "__main__":
    main()
