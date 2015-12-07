#! /usr/bin/env python
#coding=utf-8

import wx


class Frame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(600, 400))
        print "Frame init"
        panel = wx.Panel(self)
        
        button1 = wx.Button(panel, label='click', pos=(400, 20), size=(40, 30))
        self.Bind(wx.EVT_BUTTON, self.Calcuate, button1)
        
        statusBar = self.CreateStatusBar()
        menuBar = wx.MenuBar()
        menu_File = wx.Menu()
        menu_Exit = menu_File.Append(-1, "&Exit")
        menuBar.Append(menu_File, "&File")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnExit, menu_Exit)

    def textFieldData(self):
        return (("First Name", (10, 50)),
                ("Last Name", (10, 80)))
    
    def createTextFields(self, panel):
        for eachLabel, eachPos in self.textFieldData():
            self.createCaptionedText(panel, eachLabel, eachPos)
            
    def createCaptionedText(self, panel, label, pos):
        static = wx.StaticText(panel, wx.NewId(), label, pos)
        static.SetBackgroundColour("White")
        textPos = (pos[0] + 75, pos[1])
        wx.TextCtrl(panel, wx.NewId(), "", size=(100,-1), pos=textPos)    
        
    def Calcuate(self, event):
        print 'calcuating'
        dlg = wx.SingleChoiceDialog(None, "Which number", 'single choice',
                                    ['0', '1','2','3','4','5','6','7','8','9','10'])
        if dlg.ShowModal() == wx.ID_OK:
            response = dlg.GetStringSelection()
        print int(response)
        
    def OnExit(self, event):
        self.Destroy()

class App(wx.App):
    
    def OnInit(self):
        self.frame = Frame(None, -1, 'hehe')

        self.frame.Show()
        return True

def main():
    app = App()
    app.MainLoop()
    
if __name__ == '__main__':
    main()