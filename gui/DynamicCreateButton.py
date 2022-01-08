import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="yiduiyi", size=(300, 400), pos=(100, 100))
        self.Center()
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel, pos=(100, 10))

        # 动态创建button
        btn = dict()
        for i in range(5):
            btn["btn" + str(i)] = wx.Button(parent=panel, label='OK', size=(60, 20), pos=(10, i * 20 + 10))

            self.Bind(wx.EVT_BUTTON, self.on_click,
                      btn.get("btn" + str(i)))  # wx.EVT_BUTTON是按钮单击事件类型，self.on_click是事件处理，b是事件源

    def on_click(self, event):
        print(event)
        self.statictext.SetLabel("shanghai_life")
        print(111)


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print("tuichu")
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()
