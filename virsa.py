import wikipedia
import wolframalpha
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(700, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Virsa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hey!!This is Virsa <3 Your own Python Digital Assistant. How would you like me to help? ;)")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(680,40))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        x = self.txt.GetValue()
        x=x.lower()
        try:
            #wolframalpha
            app_id = "VHE3G8-52LEE6LGXW"
            client = wolframalpha.Client(app_id)
            res = client.query(x)
            answer = next(res.results).text
            print (answer)
        except:
            #wikipedia
            print (wikipedia.summary(x))


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
