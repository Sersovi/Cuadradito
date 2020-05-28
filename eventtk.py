# -*- coding: utf-8 -*-
"""
An object reacting to an action
"""

def main():
    running()

def running():

    import tkinter as tk
    import time
    
    
    
    frame = tk.Tk()
    canvas = tk.Canvas(frame, width=400,height=400)
    btn_start = tk.Button(frame, text = "Start Game!", command=moveright)
    
    canvas.pack()
    btn_start.pack()
    
    canvas.create_polygon(100,100,100,110,110,110,110,100)
    
    def printest():
        print("command works")
    
    def moveup(event):
        while True:
            canvas.move(1,0,-1)
            canvas.update()
            time.sleep(0.02)
     
    def moveright(event):
        while True:
            canvas.move(1,1,0)
            canvas.update()
            time.sleep(0.02)
            
    def moveleft(event):
        while True:
            canvas.move(1,-1,0)
            canvas.update()
            time.sleep(0.02)
            
    def movedown(event):
        while True:
            canvas.move(1,0,1)
            canvas.update()
            time.sleep(0.02)
            
    canvas.bind('<KeyPress-Up>', moveup) # <- It BINDS(event, reaction)
    canvas.bind('<KeyPress-Down>', movedown)
    canvas.bind('<KeyPress-Right>', moveright)
    canvas.bind('<KeyPress-Left>', moveleft)
    
    
    frame.mainloop()

if __name__ == '__main__':
    main()