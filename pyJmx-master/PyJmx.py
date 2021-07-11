#Tkinter has different import names on different versions.
import tkinter
from tkinter import *
from tkinter import Frame
import tkinter.scrolledtext as tkst
#These are all standard LIbs


import subprocess, shlex, sys 

from threading import Thread
from multiprocessing import Queue
from time import sleep



#This is a local lib
import config

class RedirectText(object):
	""""""

	#----------------------------------------------------------------------
	def __init__(self, text_ctrl):
		"""Constructor"""
		self.output = text_ctrl
		self.fileno = sys.stdout.fileno
		#----------------------------------------------------------------------
	def write(self, string):
		""""""

		self.output.insert(tkinter.INSERT, string + "\n")

class window(tkinter.Frame):

	def __init__(self, root):
	#Defining a few convinience constants.
		# options for buttons
		#button_style = {'fill': tkconstants.BOTH, 'padx': 5, 'pady': 5}
		# define options for opening or saving a file
		self.root = root; #Need a pointer to this for later
		#TODO: need to find a 'nicer' way to kill the app outside of tkinter's scope.
		self.file_opt = options = {}
		options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
		options['initialdir'] = config.jmxFolderPath
		options['parent'] = self.root
		options['title'] = 'select a jmx file: '

		# setting up the Tkinter frame
		#root.geometry('{}x{}'.format(800, 600))
		self.frame = tkinter.Frame(root);
		self.frame.grid(column=0,row=0)
		self.frame.columnconfigure(0,weight=1)
		self.frame.rowconfigure(0,weight=1)

		self.console = tkst.ScrolledText(self.frame)
		self.console.grid(row=3, column=1, columnspan=6)

		self.re = RedirectText(self.console)
		sys.stdout = self.re
		#Define the Menu bar
		menubar=tkinter.Menu(self.frame)
		filemenu = tkinter.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Open JMX File...", command=self.getFilename)
		filemenu.add_command(label="Save", command=self.hello)
		filemenu.add_separator()
		filemenu.add_command(label="Restart pyJmx", command=self.restart)
		filemenu.add_command(label="Exit", command=self.root.quit)
		menubar.add_cascade(label="File", menu=filemenu)
		runMenu = tkinter.Menu(menubar, tearoff=0)
		runMenu.add_command(label="Jmeter GUI", command=self.hello)
		runMenu.add_command(label="JMX Test via Console", command=self.hello)
		runMenu.add_command(label="run Selected JMX", command=self.runJmeter)
		menubar.add_cascade(label="Run...", menu=runMenu)
		root.config(menu=menubar)
		# define buttons and labels
		self.currentFile = tkinter.StringVar()
		self.currentFile.set('[No file Chosen]')
		#Tkinter.Label(self.)

		fileInput = tkinter.Entry(self.frame, textvariable=self.currentFile, width=40)
		fileInput.grid(row=2, column=1, columnspan=5)
		tkinter.Button(self.frame, text='Run Test', command=self.runJmeter).grid(row=2, column=5, sticky=tkinter.E)
		# Initialize the Terminal
		self.process= subprocess.Popen("python --version", shell=True)




	def getFilename(self):
		# get filename
		filename = tkFileDialog.askopenfilename(**self.file_opt)
		if(filename != ''):
			self.currentFile.set(filename)

	def runJmeter(self):
		subprocess.call(config.setPathCommand, shell=True)
		jmxName = self.currentFile.get()
		if(jmxName == '' or jmxName == '[No file Chosen]'):
			self.userAlert("No jmx file is chosen yet.")
		else:
			jmxName=jmxName.replace('/','\\')
			# Comment out for Windows:
			#jmxName=jmxName.replace(' ','\ ')
			print(jmxName)
			# TODO: Display this output on the UI in a buffered text box, while still outputting to a time-stamped text file.
			cmdStr = config.jMeterPath+'jmeter.bat -n -t ' + jmxName + ' -l  testResults.jtl'
			print(cmdStr)
			#This method doesn't lock the UI, but only works on Linux
			#cmdStr = shlex.split(cmdStr)
			self.process = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE )
			print(self.process.communicate())
			#TODO: Stream the jmeter.log instead of console stdout


	def userAlert(self, message):
		tkMessageBox.showinfo("Alert:", message)

	def restart(self):
		subprocess.Popen('python App.py',shell=True)
		self.root.quit()

	def hello(self):
		tkMessageBox.showinfo("PyJMX","This feature is not implemented yet")
