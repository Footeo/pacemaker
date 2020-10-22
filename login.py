from tkinter import *    

class Login:
	def __init__(self, contentFrame, screens):
		self.contentFrame = contentFrame
		self.screens = screens
		
	def loginClear(self): # clear the input text to need to reenter
		self.inputPass.delete(0,END)


	def loginDisplay(self):
		self.labelName = Label(self.contentFrame, text ="Enter Username: ")
		self.labelName.pack()
		self.inputName = Entry(self.contentFrame)
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


	def loginGo(self):
		#### obviously you need to check with real usernames that
		## you store on disk - for now user k and pass j lets you in!!!!
		if (self.inputName.get() != "k") or (self.inputPass.get()!="j"):
			self.message.configure(text="you entered INVALID login info!")
			self.loginClear() # dont leave pass entered, but we leave the username
		else:
			self.screens.mainScreen()
			
			

	