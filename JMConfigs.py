from tkinter import*
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, Canvas, Button
from tkinter.ttk import Frame, Label, Entry
import tkinter.font as tkFont
import tkinter as tk
from tkinter import messagebox

LARGE_FONT = ("Arial", 16)




class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        """    
        button = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        """
        button2 = tk.Button(self,text="Do you Want to Create a New JMeter Configuration", padx=10, pady=5,command=printValue)
        button2.pack()



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        """
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        """
        pname = messagebox.askyesno('Yes|No', 'Do you Want to Create a New Configuration?')
        print(pname)
   

        if pname == True:
            controller.show_frame(PageTwo)
        
        else:
            messagebox.showwarning('error', 'Something went wrong!')
            print(pname)
        """ 
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        """

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


class NewConfiguration(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        frame.tkraise()

# Creates action based on selection


def printValue():
    pname = messagebox.askyesno('Yes|No', 'Do you Want to Create a New Configuration?')
    print(pname)
   

    if pname == True:
        app=NewConfiguration(Frame)
    else:
        messagebox.showwarning('error', 'Something went wrong!')
        print(pname)
    

# Call's the Configuration settings.


class JMeterConfiguration(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		self.frames = {}
		for F in (StartPage, PageOne, PageTwo):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")
			self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

        #Button(frame1,text="Do you Want to Create a New JMeter Configuration", padx=10, pady=5,command=printValue).pack()
		
def main():

    root = Tk()
    root.geometry('1800x1200')

    root.resizable(width=True, height=True)
    root.title("Configuration ")
    app = JMeterConfiguration()

    root.mainloop()


if __name__ == "__main__":
    
	main()



