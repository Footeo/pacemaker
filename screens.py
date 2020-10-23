# this file has the contents that will go into the main frame for one of the options we are doing
from tkinter import * 

class Screens:
	def __init__(self, contentFrame, optionsFrame):
		self.contentFrame = contentFrame
		self.optionsFrame = optionsFrame
		
	def removeContent(self):
		for widget in self.contentFrame.winfo_children():
			widget.destroy()
		for widget in self.optionsFrame.winfo_children():
			widget.destroy()		
	
		
	def mainScreen(self):
		self.removeContent()
		self.introText = Label(self.contentFrame, text = "main screen content here!").pack()
		self.goAOO = Button(self.contentFrame, text ="AOO SCREEN", command = lambda: self.AOO()).pack()
		self.goAAI = Button(self.contentFrame, text ="AAI SCREEN", command = lambda: self.AAI()).pack()
		self.goVOO = Button(self.contentFrame, text ="VOO SCREEN", command = lambda: self.VOO()).pack()
		self.goVVI = Button(self.contentFrame, text ="VVI SCREEN", command = lambda: self.VVI()).pack()
		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
	
	def AOO(self):
		self.removeContent()
		self.AOOcontent = Label(self.contentFrame, text ="AOO content is now here! ").pack()
		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()

	def AAI(self):
		self.removeContent()
		self.AOOcontent = Label(self.contentFrame, text ="AAI content is now here! ").pack()
		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()

		
	def VOO(self):
		self.removeContent()
		self.AOOcontent = Label(self.contentFrame, text ="VOO content is now here! ").pack()
		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()

	def VVI(self):
		self.removeContent()
		self.AOOcontent = Label(self.contentFrame, text ="VVI content is now here! ").pack()
		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()