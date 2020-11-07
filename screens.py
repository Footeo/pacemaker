# this file has the contents that will go into the main frame for one of the options we are doing
from tkinter import * 
import parameters

class Screens:
	def __init__(self, contentFrame, optionsFrame):
		self.contentFrame = contentFrame
		self.optionsFrame = optionsFrame
		
		
	def removeContent(self): #Clears screens 
		for widget in self.contentFrame.winfo_children():
			widget.destroy()
		for widget in self.optionsFrame.winfo_children():
			widget.destroy()		
	
		
	def mainScreen(self):  #After user has logged in they have access to buttons for navigation
		self.removeContent()
		self.introText = Label(self.contentFrame, text = "Selection Screen").pack()
		self.goAOO = Button(self.contentFrame, text ="AOO SCREEN", command = lambda: self.AOO()).pack()
		self.goAAI = Button(self.contentFrame, text ="AAI SCREEN", command = lambda: self.AAI()).pack()
		self.goVOO = Button(self.contentFrame, text ="VOO SCREEN", command = lambda: self.VOO()).pack()
		self.goVVI = Button(self.contentFrame, text ="VVI SCREEN", command = lambda: self.VVI()).pack()
		self.deviceText = Label(self.optionsFrame, text="Currently connected to 'Oliver's' pacemaker", fg="green").pack()  # add a visual indicator showing when the DCM detects a new PACEMAKER device
		self.back = Button(self.optionsFrame, text ="Logout", command = lambda: self.mainScreen()).pack()  # This will be the logout function, have to return to other screen
	
	def AOO(self):
		self.removeContent()
		self.AOOcontent = Label(self.contentFrame, text ="AOO Programmable Variables").pack()

		#programmable parameters inputs
		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit").pack()
		self.LRLInput = Entry(self.contentFrame)
		self.LRLInput.pack()
		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit").pack()
		self.URLInput = Entry(self.contentFrame)
		self.URLInput.pack()
		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude").pack()
		self.AtrApmlitudeInput = Entry(self.contentFrame)
		self.AtrApmlitudeInput.pack()
		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width").pack()
		self.AtrPulseWidthInput = Entry(self.contentFrame)
		self.AtrPulseWidthInput.pack()
		# call the write fuctions stored in the parameters.py module
		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeAOO(self.LRLInput.get(),self.URLInput.get(),self.AtrApmlitudeInput.get(),self.AtrPulseWidthInput.get())).pack()  # Saves the parameters to the master file
		# Other menu buttons
		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup

	def AAI(self):
		self.removeContent()
		self.AAIcontent = Label(self.contentFrame, text ="AAI Programmable Variables").pack()
				
		#programmable parameters inputs
		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit").pack()
		self.LRLInput = Entry(self.contentFrame)
		self.LRLInput.pack()
		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit").pack()
		self.URLInput = Entry(self.contentFrame)
		self.URLInput.pack()
		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude").pack()
		self.AtrApmlitudeInput = Entry(self.contentFrame)
		self.AtrApmlitudeInput.pack()
		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width").pack()
		self.AtrPulseWidthInput = Entry(self.contentFrame)
		self.AtrPulseWidthInput.pack()
		self.ARP = Label(self.contentFrame, text="Atrial Refractory Period (ARP)").pack()
		self.ARPInput = Entry(self.contentFrame)
		self.ARPInput.pack()

		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeAAI(self.LRLInput.get(),self.URLInput.get(),self.AtrApmlitudeInput.get(),self.AtrPulseWidthInput.get(),self.ARPInput.get())).pack()  # Saves the parameters to the master file

		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup

		
	def VOO(self):
		self.removeContent()
		self.VOOcontent = Label(self.contentFrame, text ="VOO Programmable Variables").pack()
				
		# programmable parameters inputs
		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit").pack()
		self.LRLInput = Entry(self.contentFrame)
		self.LRLInput.pack()
		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit").pack()
		self.URLInput = Entry(self.contentFrame)
		self.URLInput.pack()
		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude").pack()
		self.VentAmplitudeInput = Entry(self.contentFrame)
		self.VentAmplitudeInput.pack()
		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width").pack()
		self.VentPulseWidthInput = Entry(self.contentFrame)
		self.VentPulseWidthInput.pack()
		#save parameters button
		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeVOO(self.LRLInput.get(),self.URLInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get())).pack()  # Saves the parameters to the master file

		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup


	def VVI(self):
		self.removeContent()
		self.VIIcontent = Label(self.contentFrame, text ="VVI Programmable Variables").pack()
				
		# programmable parameters inputs
		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit").pack()
		self.LRLInput = Entry(self.contentFrame)
		self.LRLInput.pack()
		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit").pack()
		self.URLInput = Entry(self.contentFrame)
		self.URLInput.pack()
		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude").pack()
		self.VentAmplitudeInput = Entry(self.contentFrame)
		self.VentAmplitudeInput.pack()
		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width").pack()
		self.VentPulseWidthInput = Entry(self.contentFrame)
		self.VentPulseWidthInput.pack()
		self.VRP = Label(self.contentFrame, text="Ventricular Refractory Period (VRP)").pack()
		self.VRPInput = Entry(self.contentFrame)
		self.VRPInput.pack()

		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeVVI(self.LRLInput.get(),self.URLInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get(),self.VRPInput.get())).pack()  # Saves the parameters to the master file

		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup


		# add an indicator button at bottom of the screen that tells us if we are transmitting/receiving
	def addTxRxDisplay(self):
		self.txrx = Button(self.optionsFrame, text ="Transmitting/Receiving", bg="white", fg="black")
		self.txrx.pack()
		self.txrx.configure(state=DISABLED)
		
        # call colorTxRx(1) to turn indicator light on and (0) to turn it off
	def colorTxRx(self, type):
		if (type==1):
			self.txrx.configure(bg="lightgreen")
		else:
			self.txrx.configure(bg="white")

