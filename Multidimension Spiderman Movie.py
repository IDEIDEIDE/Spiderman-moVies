#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 18:30:49 2021

@author: clockshield
"""

from tkinter import *
import random
root=Tk()
root.title("Spiderma")
root.geometry("400x400")

Label = Label(root)
spiderman_1d = ["Tom", "Andrew", "Tom"]
print(spiderman_1d[1])
spiderman_2d = [["Tom", "SPiderman Homecoming"], ["Andrew", "The Amazing Spiderman"], ["Tom", "Spiderman No Way Home Cause homeless"]]
print(spiderman_2d[2])
spiderman_3d = [[["Tom", "Spiderman", "Homecoming"], ["Anndrew", "Spiderman", "The Amazinng"], ["Tom", "Spiderman", "Homelesz SHelter so no way home"]]]

def merge():
    Label["text"] = "The actor for Spideman " + spiderman_3d[0][0][2] + " is " + spiderman_3d[0][0][0] + ". He plays the role " + spiderman_3d[0][0][1]  
btn = Button(root,text="spiderman",command=merge)
btn.place(relx = 0.5, rely = 0.4, anchor=CENTER)
Label.place(relx = 0.5, rely = 0.5, anchor=CENTER)
root.mainloop()