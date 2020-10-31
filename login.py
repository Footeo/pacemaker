from tkinter import *  
import settings # global variables
import screens # screens.func() to get anything to run

global user

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
		self.loginBtn = Button(self.contentFrame, text ="Login", command = lambda: self.loginGo(self.inputName.get(),self.inputPass.get()))
		self.loginBtn.pack()
		self.registerBtn = Button(self.contentFrame, text ="Register new user", command = self.registerScreen) 
		self.registerBtn.pack()
		self.fubar = Label(self.contentFrame, text="")
		self.fubar.pack()


	## UPDATED TO CHECK USERNAME AND PASSWORDS

	def loginGo(self,uName,Pass):
		# check with usernames/passwords stored on file
		file = open("users.txt","r")
		lines = file.readlines()
		# print(lines)
		# FName,FPass = lines.strip("\n")
		for i in lines:
			stripped = i.strip("\n")
			FName,FPass = stripped.split("\t")
			if (uName == FName) and (Pass == FPass):
				settings.user = FName
				self.screens.mainScreen() 
				break
			else:
				self.message.configure(text="you entered INVALID login info!") 
				self.loginClear()  #This interacts with screens.py in the main.py file @ where .mainScreen() comes from
		file.close()
			
	
	## This is the function for registering a new user

	def registerScreen(self):
		self.registerText = Label(self.contentFrame, text ="Register a new user").pack()
		self.newNameLabel = Label(self.contentFrame, text ="Enter New Username: ").pack()
		self.newNameEntry = Entry(self.contentFrame)  			##Have to save this entry into a text file somehow
		self.newNameEntry.pack()
		self.newPassLabel = Label(self.contentFrame, text="Enter Password: ").pack()
		self.newPassEntry = Entry(self.contentFrame, show="*")  #have to save this password into a text file too 
		self.newPassEntry.pack()
		self.newPassLabel2 = Label(self.contentFrame, text="Reenter Password: ")
		self.newPassLabel2.pack()
		self.newPassEntry2 = Entry(self.contentFrame, show="*")  #have to save this password into a text file too 
		self.newPassEntry2.pack()
		self.registerMessage = Label(self.contentFrame, text="")
		self.registerMessage.pack()
		self.registerMessage2 = Label(self.contentFrame, text="")
		self.registerMessage2.pack()
		self.registerBtn = Button(self.contentFrame, text ="Enter", command = lambda: self.registerUser(self.newNameEntry.get(),self.newPassEntry.get(),self.newPassEntry2.get()))
		self.registerBtn.pack() #What if i make it call a function registerUser?

	##This is the code that will confirm the registration for the user.

	def registerUser(self,uName,p1,p2):
		file = open("users.txt","r")
		rows = 0
		lines = file.readlines() #make a list where each line of the file is an index in the list
		word2 = "str" ## will not be a useable username 'reserved'
		for i in lines:
			rows = rows + 1

		if (p1==p2):
			self.registerMessage.configure(text = "Passwords Match")
			for j in lines:
				for word in j.split("\t"):
					if(word == uName):
						print("Username already taken")
						self.registerMessage2.configure(text="Username already taken")
						word2 = word
			
				
			
			if(rows < 10 and (word2 != uName)): # append the new password and username
				file.close()
				file = open("users.txt",'a')
				file.write(uName + '\t') #append uName and pass to file
				file.write(p2 + "\n")
				file.close()
				file = open("parameters.txt","a")
				file.write("\n"+uName+"\nAOO\nAAI\nVOO\nVVI\nLRL") # when a new user is registered they get their own set of programmable parameteres added to the file
				file.close() 
				self.registerMessage2.configure(text = "New User registered")

			elif(rows < 10 and (word2 == uName)): 
				self.registerMessage2.configure(text = "Username already taken, try a different name")
				file.close()
			else:
				self.registerMessage.configure(text = "Max number of users have been reached")
				self.registerMessage2.configure(text = "")
				file.close()

		else:
			self.registerMessage.configure(text = "Passwords do not match, try again")
			file.close()