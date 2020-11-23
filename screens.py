# this file has the contents that will go into the main frame for one of the options we are doing
from tkinter import * 
import parameters

#NOTES from Oliver
# 1. Add limits to the inputs, i.e. once a user passes an input check to see if it is within the correct range, alert them if it isn't. 
# /\ Check table 7 in PACEMAKER Document
# ALSO; Ask TA about Atrial/Ventricular Sensitivity?? (Do we need to include those)
# 2. Add unit labels for each input i.e. [ms, V, mV, sec] etc.
# 3. Add a button to load the most last inputted parameters (may as well make use of the save file)

# Add a button to each pacing mode screen to transmit the variables for serial communication and when the button it will also display the egram.


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
		self.goDOO = Button(self.contentFrame, text="DOO SCREEN", command = lambda: self.DOO()).pack()
		self.goAOOR = Button(self.contentFrame, text="AOOR SCREEN", command = lambda: self.AOOR()).pack()
		self.goAAIR = Button(self.contentFrame, text="AAIR SCREEN", command = lambda: self.AAIR()).pack()
		self.goVOOR = Button(self.contentFrame, text="VOOR SCREEN", command = lambda: self.VOOR()).pack()
		self.goVVIR = Button(self.contentFrame, text="VVIR SCREEN", command = lambda: self.VVIR()).pack()
		self.goDOOR = Button(self.contentFrame, text="DOOR SCREEN", command = lambda: self.DOOR()).pack()
		self.goDDDR = Button(self.contentFrame, text="DDDR SCREEN **", command = lambda: self.DDDR()).pack()
		self.deviceText = Label(self.optionsFrame, text="Currently connected to 'users' pacemaker", fg="green").pack()  # Have to change this value based on the users device
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

	def DOO(self):
		self.removeContent()
		self.DOOcontent = Label(self.contentFrame, text ="DOO Programmable Variables").pack()
				
		# programmable parameters inputs
		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit").pack()
		self.LRLInput = Entry(self.contentFrame)
		self.LRLInput.pack()
		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit").pack()
		self.URLInput = Entry(self.contentFrame)
		self.URLInput.pack()
		self.FixedAVDelayLabel = Label(self.contentFrame, text="Fixed AV Delay (ms)").pack()
		self.FixedAVDelayInput = Entry(self.contentFrame)
		self.FixedAVDelayInput.pack()
		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude").pack()
		self.AtrAmplitudeInput = Entry(self.contentFrame)
		self.AtrAmplitudeInput.pack()
		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width").pack()
		self.AtrPulseWidthInput = Entry(self.contentFrame)
		self.AtrPulseWidthInput.pack()
		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude").pack()
		self.VentAmplitudeInput = Entry(self.contentFrame)
		self.VentAmplitudeInput.pack()
		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width").pack()
		self.VentPulseWidthInput = Entry(self.contentFrame)
		self.VentPulseWidthInput.pack()

		#save parameters button - will have to be updated
		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeDOO(self.LRLInput.get(),self.URLInput.get(),self.FixedAVDelayInput.get(),self.AtrAmplitudeInput.get(),self.AtrPulseWidthInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get())).pack()  # Saves the parameters to the master file

		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup

	def AOOR(self):
		self.removeContent()
		self.AOORcontent = Label(self.contentFrame, text ="AOOR Programmable Variables").pack()

		#programmable parameters inputs
		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit").pack()
		self.LRLInput = Entry(self.contentFrame)
		self.LRLInput.pack()
		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit").pack()
		self.URLInput = Entry(self.contentFrame)
		self.URLInput.pack()
		self.MaxSensorRateLabel = Label(self.contentFrame, text="Maximum Sensor Rate (ms?)").pack()
		self.MaxSensorRateInput = Entry(self.contentFrame)
		self.MaxSensorRateInput.pack()
		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude").pack()
		self.AtrAmplitudeInput = Entry(self.contentFrame)
		self.AtrAmplitudeInput.pack()
		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width").pack()
		self.AtrPulseWidthInput = Entry(self.contentFrame)
		self.AtrPulseWidthInput.pack()
		self.ActivityThresholdLabel = Label(self.contentFrame, text="Activity Threshold").pack()
		self.ActivityThresholdInput	= Entry(self.contentFrame)
		self.ActivityThresholdInput.pack()
		self.ReactionTimeLabel = Label(self.contentFrame, text="Reaction Time").pack()
		self.ReactionTimeInput = Entry(self.contentFrame)
		self.ReactionTimeInput.pack()
		self.ResponseFactorLabel = Label(self.contentFrame, text="Response Factor").pack()
		self.ResponseFactorInput = Entry(self.contentFrame)
		self.ResponseFactorInput.pack()
		self.RecoveryTimeLabel = Label(self.contentFrame, text="Recovery Time").pack()
		self.RecoveryTimeInput = Entry(self.contentFrame)
		self.RecoveryTimeInput.pack()

		# call the write fuctions stored in the parameters.py module
		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeAOOR(self.LRLInput.get(),self.URLInput.get(),self.MaxSensorRateInput.get(),self.AtrAmplitudeInput.get(),self.AtrPulseWidthInput.get(),self.ActivityThresholdInput.get(),self.ReactionTimeInput.get(),self.ResponseFactorInput.get(),self.RecoveryTimeInput.get())).pack()  # Saves the parameters to the master file
		
		# Other menu buttons
		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup

	def AAIR(self):  
		self.removeContent()
		self.AAIRcontent = Label(self.contentFrame, text ="AAIR Programmable Variables").pack()
				
		#programmable parameters inputs
		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit").pack()
		self.LRLInput = Entry(self.contentFrame)
		self.LRLInput.pack()
		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit").pack()
		self.URLInput = Entry(self.contentFrame)
		self.URLInput.pack()
		self.MaxSensorRateLabel = Label(self.contentFrame, text="Maximum Sensor Rate (ms?)").pack()
		self.MaxSensorRateInput = Entry(self.contentFrame)
		self.MaxSensorRateInput.pack()
		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude").pack()
		self.AtrAmplitudeInput = Entry(self.contentFrame)
		self.AtrAmplitudeInput.pack()
		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width").pack()
		self.AtrPulseWidthInput = Entry(self.contentFrame)
		self.AtrPulseWidthInput.pack()
		self.ARP = Label(self.contentFrame, text="Atrial Refractory Period (ARP)").pack()
		self.ARPInput = Entry(self.contentFrame)
		self.ARPInput.pack()
		self.HysteresisLabel = Label(self.contentFrame, text="Hysteresis").pack()
		self.HysteresisInput = Entry(self.contentFrame)
		self.HysteresisInput.pack()
		self.RateSmoothingLabel = Label(self.contentFrame, text="Rate Smoothing").pack()
		self.RateSmoothingInput = Entry(self.contentFrame)
		self.RateSmoothingInput.pack()
		self.ActivityThresholdLabel = Label(self.contentFrame, text="Activity Threshold").pack()
		self.ActivityThresholdInput	= Entry(self.contentFrame)
		self.ActivityThresholdInput.pack()
		self.ReactionTimeLabel = Label(self.contentFrame, text="Reaction Time").pack()
		self.ReactionTimeInput = Entry(self.contentFrame)
		self.ReactionTimeInput.pack()
		self.ResponseFactorLabel = Label(self.contentFrame, text="Response Factor").pack()
		self.ResponseFactorInput = Entry(self.contentFrame)
		self.ResponseFactorInput.pack()
		self.RecoveryTimeLabel = Label(self.contentFrame, text="Recovery Time").pack()
		self.RecoveryTimeInput = Entry(self.contentFrame)
		self.RecoveryTimeInput.pack()

		# Going to have to modify this button functions
		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeAAIR(self.LRLInput.get(),self.URLInput.get(),self.MaxSensorRateInput.get(),self.AtrAmplitudeInput.get(),self.AtrPulseWidthInput.get(),self.ARPInput.get(),self.HysteresisInput.get(),self.RateSmoothingInput.get(),self.ActivityThresholdInput.get(),self.ReactionTimeInput.get(),self.ResponseFactorInput.get(),self.RecoveryTimeInput.get())).pack()  # Saves the parameters to the master file

		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup

	def VOOR(self): 
		self.removeContent()
		self.VOORcontent = Label(self.contentFrame, text ="VOOR Programmable Variables").pack()
				
		# programmable parameters inputs
		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit").pack()
		self.LRLInput = Entry(self.contentFrame)
		self.LRLInput.pack()
		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit").pack()
		self.URLInput = Entry(self.contentFrame)
		self.URLInput.pack()
		self.MaxSensorRateLabel = Label(self.contentFrame, text="Maximum Sensor Rate (ms?)").pack()
		self.MaxSensorRateInput = Entry(self.contentFrame)
		self.MaxSensorRateInput.pack()
		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude").pack()
		self.VentAmplitudeInput = Entry(self.contentFrame)
		self.VentAmplitudeInput.pack()
		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width").pack()
		self.VentPulseWidthInput = Entry(self.contentFrame)
		self.VentPulseWidthInput.pack()
		self.ActivityThresholdLabel = Label(self.contentFrame, text="Activity Threshold").pack()
		self.ActivityThresholdInput	= Entry(self.contentFrame)
		self.ActivityThresholdInput.pack()
		self.ReactionTimeLabel = Label(self.contentFrame, text="Reaction Time").pack()
		self.ReactionTimeInput = Entry(self.contentFrame)
		self.ReactionTimeInput.pack()
		self.ResponseFactorLabel = Label(self.contentFrame, text="Response Factor").pack()
		self.ResponseFactorInput = Entry(self.contentFrame)
		self.ResponseFactorInput.pack()
		self.RecoveryTimeLabel = Label(self.contentFrame, text="Recovery Time").pack()
		self.RecoveryTimeInput = Entry(self.contentFrame)
		self.RecoveryTimeInput.pack()


		# Going to have to modify this button function
		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeVOOR(self.LRLInput.get(),self.URLInput.get(),self.MaxSensorRateInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get(),self.ActivityThresholdInput.get(),self.ReactionTimeInput.get(),self.ResponseFactorInput.get(),self.RecoveryTimeInput.get())).pack()  # Saves the parameters to the master file

		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup

	def VVIR(self):
		self.removeContent()
		self.VIIRcontent = Label(self.contentFrame, text ="VVIR Programmable Variables").pack()
				
		# programmable parameters inputs
		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit").pack()
		self.LRLInput = Entry(self.contentFrame)
		self.LRLInput.pack()
		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit").pack()
		self.URLInput = Entry(self.contentFrame)
		self.URLInput.pack()
		self.MaxSensorRateLabel = Label(self.contentFrame, text="Maximum Sensor Rate (ms?)").pack()
		self.MaxSensorRateInput = Entry(self.contentFrame)
		self.MaxSensorRateInput.pack()
		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude").pack()
		self.VentAmplitudeInput = Entry(self.contentFrame)
		self.VentAmplitudeInput.pack()
		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width").pack()
		self.VentPulseWidthInput = Entry(self.contentFrame)
		self.VentPulseWidthInput.pack()
		self.VRP = Label(self.contentFrame, text="Ventricular Refractory Period (VRP)").pack()
		self.VRPInput = Entry(self.contentFrame)
		self.VRPInput.pack()
		self.HysteresisLabel = Label(self.contentFrame, text="Hysteresis").pack()
		self.HysteresisInput = Entry(self.contentFrame)
		self.HysteresisInput.pack()
		self.RateSmoothingLabel = Label(self.contentFrame, text="Rate Smoothing").pack()
		self.RateSmoothingInput = Entry(self.contentFrame)
		self.RateSmoothingInput.pack()
		self.ActivityThresholdLabel = Label(self.contentFrame, text="Activity Threshold").pack()
		self.ActivityThresholdInput	= Entry(self.contentFrame)
		self.ActivityThresholdInput.pack()
		self.ReactionTimeLabel = Label(self.contentFrame, text="Reaction Time").pack()
		self.ReactionTimeInput = Entry(self.contentFrame)
		self.ReactionTimeInput.pack()
		self.ResponseFactorLabel = Label(self.contentFrame, text="Response Factor").pack()
		self.ResponseFactorInput = Entry(self.contentFrame)
		self.ResponseFactorInput.pack()
		self.RecoveryTimeLabel = Label(self.contentFrame, text="Recovery Time").pack()
		self.RecoveryTimeInput = Entry(self.contentFrame)
		self.RecoveryTimeInput.pack()

		# write inputs to file
		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeVVIR(self.LRLInput.get(),self.URLInput.get(),self.MaxSensorRateInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get(),self.VRPInput.get(),self.HysteresisInput.get(),self.RateSmoothingInput.get(),self.ActivityThresholdInput.get(),self.ReactionTimeInput.get(),self.ResponseFactorInput.get(),self.RecoveryTimeInput.get())).pack()  # Saves the parameters to the master file

		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup

	def DOOR(self):
		self.removeContent()
		self.DOORcontent = Label(self.contentFrame, text ="DOOR Programmable Variables").pack()
				
		# programmable parameters inputs
		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit").pack()
		self.LRLInput = Entry(self.contentFrame)
		self.LRLInput.pack()
		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit").pack()
		self.URLInput = Entry(self.contentFrame)
		self.URLInput.pack()
		self.MaxSensorRateLabel = Label(self.contentFrame, text="Maximum Sensor Rate (ms?)").pack()
		self.MaxSensorRateInput = Entry(self.contentFrame)
		self.MaxSensorRateInput.pack()
		self.FixedAVDelayLabel = Label(self.contentFrame, text="Fixed AV Delay (ms)").pack()
		self.FixedAVDelayInput = Entry(self.contentFrame)
		self.FixedAVDelayInput.pack()
		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude").pack()
		self.AtrAmplitudeInput = Entry(self.contentFrame)
		self.AtrAmplitudeInput.pack()
		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width").pack()
		self.AtrPulseWidthInput = Entry(self.contentFrame)
		self.AtrPulseWidthInput.pack()
		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude").pack()
		self.VentAmplitudeInput = Entry(self.contentFrame)
		self.VentAmplitudeInput.pack()
		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width").pack()
		self.VentPulseWidthInput = Entry(self.contentFrame)
		self.VentPulseWidthInput.pack()
		self.ActivityThresholdLabel = Label(self.contentFrame, text="Activity Threshold").pack()
		self.ActivityThresholdInput	= Entry(self.contentFrame)
		self.ActivityThresholdInput.pack()
		self.ReactionTimeLabel = Label(self.contentFrame, text="Reaction Time").pack()
		self.ReactionTimeInput = Entry(self.contentFrame)
		self.ReactionTimeInput.pack()
		self.ResponseFactorLabel = Label(self.contentFrame, text="Response Factor").pack()
		self.ResponseFactorInput = Entry(self.contentFrame)
		self.ResponseFactorInput.pack()
		self.RecoveryTimeLabel = Label(self.contentFrame, text="Recovery Time").pack()
		self.RecoveryTimeInput = Entry(self.contentFrame)
		self.RecoveryTimeInput.pack()

		#save parameters button - will have to be updated
		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeDOOR(self.LRLInput.get(),self.URLInput.get(),self.MaxSensorRateInput.get(),self.FixedAVDelayInput.get(),self.AtrAmplitudeInput.get(),self.AtrPulseWidthInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get(),self.ActivityThresholdInput.get(),self.ReactionTimeInput.get(),self.ResponseFactorInput.get(),self.RecoveryTimeInput.get())).pack()  # Saves the parameters to the master file

		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup


## BONUS (Only do once all else is done)  
# More functions exist beyond this one \/

	def DDDR(self):
		self.removeContent()
		self.DDDRcontent = Label(self.contentFrame, text ="DDDR Programmable Variables").pack()
				
		# programmable parameters inputs
		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit").pack()
		self.LRLInput = Entry(self.contentFrame)
		self.LRLInput.pack()
		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit").pack()
		self.URLInput = Entry(self.contentFrame)
		self.URLInput.pack()
		self.MaxSensorRateLabel = Label(self.contentFrame, text="Maximum Sensor Rate (ms?)").pack()
		self.MaxSensorRateInput = Entry(self.contentFrame)
		self.MaxSensorRateInput.pack()
		self.FixedAVDelayLabel = Label(self.contentFrame, text="Fixed AV Delay (ms)").pack()
		self.FixedAVDelayInput = Entry(self.contentFrame)
		self.FixedAVDelayInput.pack()
		self.DynamicAVDelayLabel = Label(self.contentFrame, text="Dynamic AV Delay (ms)").pack()
		self.DynamicAVDelayInput = Entry(self.contentFrame)
		self.DynamicAVDelayInput.pack()
		self.SensedAVDelayOffsetLabel = Label(self.contentFrame, text="Sensed AV Delay Offset (ms)").pack()
		self.SensedAVDelayOffsetInput = Entry(self.contentFrame)
		self.SensedAVDelayOffsetInput.pack()
		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude").pack()
		self.AtrApmlitudeInput = Entry(self.contentFrame)
		self.AtrApmlitudeInput.pack()
		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width").pack()
		self.AtrPulseWidthInput = Entry(self.contentFrame)
		self.AtrPulseWidthInput.pack()
		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude").pack()
		self.VentAmplitudeInput = Entry(self.contentFrame)
		self.VentAmplitudeInput.pack()
		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width").pack()
		self.VentPulseWidthInput = Entry(self.contentFrame)
		self.VentPulseWidthInput.pack()
		self.VRP = Label(self.contentFrame, text="Ventricular Refractory Period (VRP)").pack()
		self.VRPInput = Entry(self.contentFrame)
		self.VRPInput.pack()
		self.ARP = Label(self.contentFrame, text="Atrial Refractory Period (ARP)").pack()
		self.ARPInput = Entry(self.contentFrame)
		self.ARPInput.pack()
		self.HysteresisLabel = Label(self.contentFrame, text="Hysteresis").pack()
		self.HysteresisInput = Entry(self.contentFrame)
		self.HysteresisInput.pack()
		self.RateSmoothingLabel = Label(self.contentFrame, text="Rate Smoothing").pack()
		self.RateSmoothingInput = Entry(self.contentFrame)
		self.RateSmoothingInput.pack()
		## ATR Mode (on/off button?)
		# ATR Fallback - fallback to VVIR
		# ATR Duration - Atrial tachycardia happens, wait a programmed number of cariac cycles
		self.ATRDurationLabel = Label(self.contentFrame, text="ATR Duration").pack()
		self.ATRDurationInput = Entry(self.contentFrame)
		self.ATRDurationInput.pack()
		self.ActivityThresholdLabel = Label(self.contentFrame, text="Activity Threshold").pack()
		self.ActivityThresholdInput	= Entry(self.contentFrame)
		self.ActivityThresholdInput.pack()
		self.ReactionTimeLabel = Label(self.contentFrame, text="Reaction Time").pack()
		self.ReactionTimeInput = Entry(self.contentFrame)
		self.ReactionTimeInput.pack()
		self.ResponseFactorLabel = Label(self.contentFrame, text="Response Factor").pack()
		self.ResponseFactorInput = Entry(self.contentFrame)
		self.ResponseFactorInput.pack()
		self.RecoveryTimeLabel = Label(self.contentFrame, text="Recovery Time").pack()
		self.RecoveryTimeInput = Entry(self.contentFrame)
		self.RecoveryTimeInput.pack()

		#save parameters button - will have to be updated
		# self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeVVI(self.LRLInput.get(),self.URLInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get(),self.VRPInput.get())).pack()  # Saves the parameters to the master file

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

