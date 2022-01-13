from tkinter import *
import random
import os

def music():
    file = os.listdir("habibi")
    return file
def run_music ():
    fmusic = music()
    pmusic = random.choice(fmusic)
    music_path = os.path.join(os.curdir , 'habibi' , pmusic)
    os.startfile(music_path)
    print(music_path)

screen = Tk()
screen.geometry("500x300")
screen.configure(bg = "blue")

title = Label(screen , text = "music application" , bg = 'blue' , fg = 'yellow'  , font=("italic" ,20 ))
title.pack()

btn = Button(screen , text = "play music" , bg = 'blue' , fg = 'yellow' , command = run_music , font=(" " , 22))
btn.pack()

screen.mainloop()
