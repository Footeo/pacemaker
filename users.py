from tkinter import *

class Users:
    def __init__(self,uname,password):
        self.contentFrame = contentFrame
		self.screens = screens

	def registerDisplay(self):
		self.labelName = Label(self.uName, text ="Enter Username: ")
		self.labelName.pack()
		self.inputName = Entry(self.uName)
		self.inputName.pack()
		self.labelPass = Label (self.contentFrame, text="Exter Password: ")
		self.labelPass.pack()
		self.inputPass = Entry(self.contentFrame, show="*")
		self.inputPass.pack()
		self.message = Label(self.contentFrame, text="")
		self.message.pack()
		self.loginBtn = Button(self.contentFrame, text ="Login", command = self.loginGo)
		self.loginBtn.pack()
		self.registerBtn = Button(self.contentFrame, text ="Register new user") ### need to do a registration screen!
		self.registerBtn.pack()
		self.fubar = Label(self.contentFrame, text="for testing use name 'k' and the pass 'j' - anything else will give error")
		self.fubar.pack()
