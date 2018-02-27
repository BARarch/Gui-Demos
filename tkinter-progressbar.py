import sys
import time
from tkinter import *
import tkinter.ttk as ttk

class Application(Frame):
    def say_hi(self):
        print("Hi there, everyone!")
        
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT['text'] = "QUIT"
        self.QUIT['fg'] = "red"
        self.QUIT['command'] = self.quit
        self.QUIT.pack({"side": "left"})
        
        self.pgMove = Button(self)
        self.pgMove['text'] = "Move"
        self.pgMove['fg'] = "green"
        self.pgMove['command'] = self.move_progress
        self.pgMove.pack({"side": "left"})
        
        self.pb = ttk.Progressbar(self, orient='horizontal', length=400, mode='determinate')
        self.pb.pack({'side':'right'})
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.parent = master
        self.pack()
        self.createWidgets()
        self.pb["maximum"] = 200
        #self.pb['value'] = 50
        
    def move_progress(self):
        for i in range(20):
            self.pb.step()
            self.update()
            time.sleep(.02)
        #self.pb.start()
        
        #self.pb["value"] = 30
        
root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()