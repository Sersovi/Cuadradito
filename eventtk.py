# -*- coding: utf-8 -*-
"""
An object reacting to an action
"""


import tkinter as tk
import time

def moveup(event=None): ### arg = None hace que se pueda dejar vacio, o que se pueda llenar
    while True: ### <--- loop infinito que no acaba aunque salgas de la fnc.
        canvas.move(poly1,0,-1)
        canvas.update()
        time.sleep(0.02)
 
def moveright(event=None):
    while True:
        canvas.move(poly1,1,0)
        canvas.update()
        time.sleep(0.02)
        
def moveleft(event=None):
    while True:
        canvas.move(poly1,-1,0)
        canvas.update()
        time.sleep(0.02)
        
def movedown(event=None):
    while True:
        canvas.move(poly1,0,1)
        canvas.update()
        time.sleep(0.02)

frame = tk.Tk()
canvas = tk.Canvas(frame, width=400,height=400)
# btn_start = tk.Button(frame, text = "Start Game!", command = moveup) ### moveup --el argumento-- != moveup() --el return de la fnc--

canvas.pack()


poly1 = canvas.create_rectangle(200,200,210,210)

        
canvas.bind('<KeyPress>w', moveup) # <- It BINDS(event, reaction)
canvas.bind('<KeyPress>s', movedown)
canvas.bind('<KeyPress>d', moveright)
canvas.bind('<KeyPress>a', moveleft)


frame.mainloop()