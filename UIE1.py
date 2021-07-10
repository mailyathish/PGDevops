import tkinter as tk
from tkinter import ttk, filedialog

LARGE_FONT = ("Arial", 12)
MEDIUM_FONT = ("Arial", 11)
REGULAR_FONT = ("Arial", 10)

text_z = ["Select file 1", "Select the file 2", "Select file 3", "Select file 4"]

window=tk.Tk()

def click(): 
    z = tk.filedialog.askopenfilename(initialdir = "/",title = "Select file", filetypes = ( ("JMeter files", "*.jmx"), ("All files", "*.*") ) )
    a[i-2].insert(tk.END, z)
    z[i] = a[i-2].get()

##Main program
#There is an image I will add at the end on row=0
ttk.Label(window, text="file load", font = LARGE_FONT, background = "white").grid(row=1, column=1, columnspan=3, padx=20, pady = 10, sticky="W")

a = [tk.StringVar(window) for i in range(len(text_z))]

for i in range(2,len(text_z)+2): 
    Label_z = ttk.Label(window, text=text_z[i-2], background="white").grid(row= 2*i, column=0,columnspan=3, padx=10, pady=2, sticky="W")
    a[i-2] = ttk.Entry(window, width=60, background="gray")
    a[i-2].grid(row= 2*i+1, column=0, columnspan=3, padx=10, sticky="WE")
    ttk.Button(window, text="Search", width=10, command=click).grid(row= 2*i+1, column=3, padx=5, sticky="W")

window.mainloop()