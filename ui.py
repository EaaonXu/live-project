import wx


class Start(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "福建十三水", size=(1276, 729), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        self.Center()
        self.init_p = None
        self.InitStart()

    def InitStart(self):
        self.init_p = wx.Panel(self)
        b1 = wx.Button(self.init_p, label='服饰', pos=(400, 150), size=(200, 100))
        b1.Bind(wx.EVT_BUTTON, self.Onb1)
        b2 = wx.Button(self.init_p, label='美食', pos=(700, 150), size=(200, 100))
        b2.Bind(wx.EVT_BUTTON, self.Onb2)
        b3 = wx.Button(self.init_p, label='商圈', pos=(400, 400), size=(200, 100))
        b3.Bind(wx.EVT_BUTTON, self.Onb3)
        b4 = wx.Button(self.init_p, label='人均消费', pos=(700, 400), size=(200, 100))
        b4.Bind(wx.EVT_BUTTON, self.Onb4)

    def Onb1(self, event):
        pass

    def Onb2(self, event):
        pass

    def Onb3(self, event):
        pass

    def Onb4(self, event):
        pass


if __name__ == '__main__':
    app = wx.App()
    frame = Start()
    frame.Show()
    app.MainLoop()
