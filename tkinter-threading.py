from mktinter import *
import tkinter.ttk as ttk
import time
import threading


def callback():
    total = sum(range(100000000))
    print(total)
    #label.config(text=total)
    
def handle_click():    
    t.start()

def move_progress():
    for i in range(20):
        pb.step()
        root.update()
        time.sleep(.02)

root = Tk()
t = threading.Thread(target=callback, daemon=True)
Button(root, text='Add it up', command=handle_click).pack()
pgMove = Button(root)
pgMove['text'] = "Move"
pgMove['fg'] = "green"
pgMove['command'] = move_progress
pgMove.pack()
pb = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
pb.pack()
label = Label(root)
label.pack()
root.mainloop()