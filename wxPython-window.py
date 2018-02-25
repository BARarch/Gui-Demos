import wx

class bucky(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame Aka Window', size=(300,200))
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = bucky(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
