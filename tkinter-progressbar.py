import sys
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
        
        self.pb = ttk.Progressbar(self.parent, orient='horizontal', length=400, mode='determinate')
        self.pb.pack({'side':'right'})
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.parent = master
        self.pack()
        self.createWidgets()
        self.pb["maximum"] = 200
        self.pb.start()
        
        #self.pb["value"] = 30
        
root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()