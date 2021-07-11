import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("JMeter Configuration")
        #setting window size
        width=1800
        height=1200
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_89=tk.Label(root)
        GLabel_89["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=24)
        GLabel_89["font"] = ft
        GLabel_89["fg"] = "#333333"
        GLabel_89["justify"] = "center"
        GLabel_89["text"] = "JMeter Configuration"
        GLabel_89.place(x=480,y=30,width=258,height=33)

        GLabel_628=tk.Label(root)
        ft = tkFont.Font(family='Times',size=20)
        GLabel_628["font"] = ft
        GLabel_628["fg"] = "#333333"
        GLabel_628["justify"] = "center"
        GLabel_628["text"] = "Select JMeter File"
        GLabel_628.place(x=370,y=100,width=194,height=30)

        GButton_753=tk.Button(root)
        GButton_753["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=20)
        GButton_753["font"] = ft
        GButton_753["fg"] = "#000000"
        GButton_753["justify"] = "center"
        GButton_753["text"] = "File Select"
        GButton_753["relief"] = "ridge"
        GButton_753.place(x=740,y=100,width=138,height=30)
        GButton_753["command"] = self.GButton_753_command

        GLabel_321=tk.Label(root)
        ft = tkFont.Font(family='Times',size=20)
        GLabel_321["font"] = ft
        GLabel_321["fg"] = "#333333"
        GLabel_321["justify"] = "center"
        GLabel_321["text"] = "VUser / Threads"
        GLabel_321.place(x=370,y=160,width=184,height=30)

        GLineEdit_857=tk.Entry(root)
        GLineEdit_857["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=20)
        GLineEdit_857["font"] = ft
        GLineEdit_857["fg"] = "#333333"
        GLineEdit_857["justify"] = "center"
        GLineEdit_857["text"] = "Entry"
        GLineEdit_857["relief"] = "ridge"
        GLineEdit_857.place(x=740,y=160,width=70,height=25)
        GLineEdit_857["validatecommand"] = "fileOpen"

        GLabel_861=tk.Label(root)
        ft = tkFont.Font(family='Times',size=20)
        GLabel_861["font"] = ft
        GLabel_861["fg"] = "#333333"
        GLabel_861["justify"] = "center"
        GLabel_861["text"] = "Select Load Generator"
        GLabel_861.place(x=380,y=220,width=180,height=37)

        GListBox_775=tk.Listbox(root)
        GListBox_775["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=20)
        GListBox_775["font"] = ft
        GListBox_775["fg"] = "#333333"
        GListBox_775["justify"] = "left"
        GListBox_775["relief"] = "ridge"
        GListBox_775.place(x=740,y=220,width=121,height=30)
        GListBox_775["listvariable"] = "LoadGen"

    def GButton_753_command(self):
        print("command")

    def fileOpen(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
