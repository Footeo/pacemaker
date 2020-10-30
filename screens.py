# this file has the contents that will go into the main frame for one of the options we are doing
from tkinter import * 

class Screens:
	def __init__(self, contentFrame, optionsFrame):
		self.contentFrame = contentFrame
		self.optionsFrame = optionsFrame
		# self.logout = logout
		
	def removeContent(self):
		for widget in self.contentFrame.winfo_children():
			widget.destroy()
		for widget in self.optionsFrame.winfo_children():
			widget.destroy()		
	
		
	def mainScreen(self):
		self.removeContent()
		self.introText = Label(self.contentFrame, text = "Selection Screen").pack()
		self.goAOO = Button(self.contentFrame, text ="AOO SCREEN", command = lambda: self.AOO()).pack()
		self.goAAI = Button(self.contentFrame, text ="AAI SCREEN", command = lambda: self.AAI()).pack()
		self.goVOO = Button(self.contentFrame, text ="VOO SCREEN", command = lambda: self.VOO()).pack()
		self.goVVI = Button(self.contentFrame, text ="VVI SCREEN", command = lambda: self.VVI()).pack()
		self.deviceText = Label(self.contentFrame, text="Currently connected to 'Oliver's' pacemaker").pack()  # add a visual indicator showing when the DCM detects a new PACEMAKER device
		self.back = Button(self.optionsFrame, text ="Logout", command = lambda: self.mainDisplay()).pack()  # This will be the logout function, have to return to other screen
	
	def AOO(self):
		self.removeContent()
		self.AOOcontent = Label(self.contentFrame, text ="AOO Programmable Variables").pack()

		# Add programmable variables
		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit").pack()
		self.LRLInput = Entry(self.contentFrame).pack()
		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit").pack()
		self.URLInput = Entry(self.contentFrame).pack()
		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude").pack()
		self.AtrApmlitudeInput = Entry(self.contentFrame).pack()
		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width").pack()
		self.AtrPulseWidthInput = Entry(self.contentFrame).pack()
		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude").pack()
		self.VentAmplitudeInput = Entry(self.contentFrame).pack()
		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width").pack()
		self.VentPulseWidthInput = Entry(self.contentFrame).pack()
		self.VRP = Label(self.contentFrame, text="Ventricular Refractory Period (VRP)").pack()
		self.VRPInput = Entry(self.contentFrame).pack()
		self.ARP = Label(self.contentFrame, text="Atrial Refractory Period (ARP)").pack()
		self.ARPInput = Entry(self.contentFrame).pack()

		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbuttonremoveme = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbuttonremoveme2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup

	def AAI(self):
		self.removeContent()
		self.AOOcontent = Label(self.contentFrame, text ="AAI Programmable Variables").pack()
				
		# Add programmable variables
		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit").pack()
		self.LRLInput = Entry(self.contentFrame).pack()
		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit").pack()
		self.URLInput = Entry(self.contentFrame).pack()
		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude").pack()
		self.AtrApmlitudeInput = Entry(self.contentFrame).pack()
		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width").pack()
		self.AtrPulseWidthInput = Entry(self.contentFrame).pack()
		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude").pack()
		self.VentAmplitudeInput = Entry(self.contentFrame).pack()
		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width").pack()
		self.VentPulseWidthInput = Entry(self.contentFrame).pack()
		self.VRP = Label(self.contentFrame, text="Ventricular Refractory Period (VRP)").pack()
		self.VRPInput = Entry(self.contentFrame).pack()
		self.ARP = Label(self.contentFrame, text="Atrial Refractory Period (ARP)").pack()
		self.ARPInput = Entry(self.contentFrame).pack()

		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbuttonremoveme = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbuttonremoveme2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup
		
	def VOO(self):
		self.removeContent()
		self.AOOcontent = Label(self.contentFrame, text ="VOO Programmable Variables").pack()
				
		# Add programmable variables
		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit").pack()
		self.LRLInput = Entry(self.contentFrame).pack()
		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit").pack()
		self.URLInput = Entry(self.contentFrame).pack()
		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude").pack()
		self.AtrApmlitudeInput = Entry(self.contentFrame).pack()
		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width").pack()
		self.AtrPulseWidthInput = Entry(self.contentFrame).pack()
		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude").pack()
		self.VentAmplitudeInput = Entry(self.contentFrame).pack()
		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width").pack()
		self.VentPulseWidthInput = Entry(self.contentFrame).pack()
		self.VRP = Label(self.contentFrame, text="Ventricular Refractory Period (VRP)").pack()
		self.VRPInput = Entry(self.contentFrame).pack()
		self.ARP = Label(self.contentFrame, text="Atrial Refractory Period (ARP)").pack()
		self.ARPInput = Entry(self.contentFrame).pack()

		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbuttonremoveme = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbuttonremoveme2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup

	def VVI(self):
		self.removeContent()
		self.AOOcontent = Label(self.contentFrame, text ="VVI Programmable Variables").pack()
				
		# Add programmable variables
		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit").pack()
		self.LRLInput = Entry(self.contentFrame).pack()
		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit").pack()
		self.URLInput = Entry(self.contentFrame).pack()
		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude").pack()
		self.AtrApmlitudeInput = Entry(self.contentFrame).pack()
		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width").pack()
		self.AtrPulseWidthInput = Entry(self.contentFrame).pack()
		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude").pack()
		self.VentAmplitudeInput = Entry(self.contentFrame).pack()
		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width").pack()
		self.VentPulseWidthInput = Entry(self.contentFrame).pack()
		self.VRP = Label(self.contentFrame, text="Ventricular Refractory Period (VRP)").pack()
		self.VRPInput = Entry(self.contentFrame).pack()
		self.ARP = Label(self.contentFrame, text="Atrial Refractory Period (ARP)").pack()
		self.ARPInput = Entry(self.contentFrame).pack()

		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbuttonremoveme = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbuttonremoveme2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup

		# add an indicator button at bottom of the screen that tells us if we are transmitting/receiving
	def addTxRxDisplay(self):
		self.txrx = Button(self.optionsFrame, text ="Transmitting/Receiving", bg="white", fg="black")
		self.txrx.pack()
		self.txrx.configure(state=DISABLED)
		
        # call colorTxRx(1) to turn indicator light on and (0) to turn it off
	def colorTxRx(self, type):
		if (type==1):
			self.txrx.configure(bg="yellow")
		else:
			self.txrx.configure(bg="white")

	# def logout(self):
