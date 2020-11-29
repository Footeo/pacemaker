# this file has the contents that will go into the main frame for one of the options we are doing
from tkinter import * 
import parameters
import settings #for user global
import readtosend #reads from the parameters file to prepare values for serialcom

#NOTES from Oliver
# 1. Add limits to the inputs, i.e. once a user passes an input check to see if it is within the correct range, alert them if it isn't. Also need to check for things like LRL > URL
# /\ Check table 7 in PACEMAKER Document
# 2. Add the currently logged in user on the screen
# 2. Add a button to load the last inputted parameters (may as well make use of the save file)
# 3. Work on serial communication functions (create the bones of the functions and change the arguments when Zuri informs us what the byte sizes are)
# Add a button to each pacing mode screen to transmit the variables for serial communication and when the button it will also display the egram.
# Also have to add the EGRAM real time graph using PyQt that will be done after serial communication I think but we can also work on the bones of that now



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
		self.introText = Label(self.contentFrame, text = "Selection Screen").grid(row=0,column=2,padx=35)
		self.selectMode = Label(self.contentFrame, text="1. Select a Mode").grid(row=1,column=2,pady=5,padx=35)
		self.goAOO = Button(self.contentFrame, text ="AOO MODE", command = lambda: self.AOO(),activebackground='red').grid(row=2,column=0,padx=35,pady=5)
		self.goAAI = Button(self.contentFrame, text ="AAI MODE", command = lambda: self.AAI(),activebackground='red').grid(row=2,column=1,padx=35)
		self.goVOO = Button(self.contentFrame, text ="VOO MODE", command = lambda: self.VOO(),activebackground='red').grid(row=2,column=2)
		self.goVVI = Button(self.contentFrame, text ="VVI MODE", command = lambda: self.VVI(),activebackground='red').grid(row=2,column=3,padx=35)
		self.goDOO = Button(self.contentFrame, text="DOO MODE", command = lambda: self.DOO(),activebackground='red').grid(row=2,column=4,padx=35)
		self.goAOOR = Button(self.contentFrame, text="AOOR MODE", command = lambda: self.AOOR(),activebackground='red').grid(row=3,column=0,pady=5)
		self.goAAIR = Button(self.contentFrame, text="AAIR MODE", command = lambda: self.AAIR(),activebackground='red').grid(row=3,column=1)
		self.goVOOR = Button(self.contentFrame, text="VOOR MODE", command = lambda: self.VOOR(),activebackground='red').grid(row=3,column=2)
		self.goVVIR = Button(self.contentFrame, text="VVIR MODE", command = lambda: self.VVIR(),activebackground='red').grid(row=3,column=3)
		self.goDOOR = Button(self.contentFrame, text="DOOR MODE", command = lambda: self.DOOR(),activebackground='red').grid(row=3,column=4)
		# self.goDDDR = Button(self.contentFrame, text="DDDR SCREEN **", command = lambda: self.DDDR()).pack()
		who = StringVar()
		who.set("Currently connected to "+settings.user+"'s pacemaker")
		self.deviceText1 = Label(self.optionsFrame, textvariable=who, fg="green").grid(row=10,sticky="S")  # Have to change this value based on the users device
		

		#LRL,URL,MRS,FAVD,AtrAmp,VentAmp,AtrPW,VentPW,AtrSense,VentSense,VRP,ARP,PVARP,RateSmooth,ActivityThresh,ReactTime,RespFact,RecoveryTime
		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit (BPM)").pack()
		self.LRLInput = Entry(self.contentFrame)
		self.LRLInput.pack()
		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit (BPM)").pack()
		self.URLInput = Entry(self.contentFrame)
		self.URLInput.pack()
		self.MaxSensorRateLabel = Label(self.contentFrame, text="Maximum Sensor Rate (BPM)").pack()
		self.MaxSensorRateInput = Entry(self.contentFrame)
		self.MaxSensorRateInput.pack()
		self.FixedAVDelayLabel = Label(self.contentFrame, text="Fixed AV Delay (V)").pack()
		self.FixedAVDelayInput = Entry(self.contentFrame)
		self.FixedAVDelayInput.pack()
		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude (V)").pack()
		self.AtrAmplitudeInput = Entry(self.contentFrame)
		self.AtrAmplitudeInput.pack()
		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude (V)").pack()
		self.VentAmplitudeInput = Entry(self.contentFrame)
		self.VentAmplitudeInput.pack()
		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width (ms)").pack()
		self.AtrPulseWidthInput = Entry(self.contentFrame)
		self.AtrPulseWidthInput.pack()
		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width (ms)").pack()
		self.VentPulseWidthInput = Entry(self.contentFrame)
		self.VentPulseWidthInput.pack()
		self.AtrSenseLabel = Label(self.contentFrame, text="Atrial Amplitude (V)").pack()
		self.AtrSenseInput = Entry(self.contentFrame)
		self.AtrSenseInput.pack()
		self.VentSenseLabel = Label(self.contentFrame, text="Ventricular Amplitude (V)").pack()
		self.VentSenseInput = Entry(self.contentFrame)
		self.VentSenseInput.pack()
		self.VRP = Label(self.contentFrame, text="Ventricular Refractory Period (ms)").pack()
		self.VRPInput = Entry(self.contentFrame)
		self.VRPInput.pack()
		self.ARP = Label(self.contentFrame, text="Atrial Refractory Period (ms)").pack()
		self.ARPInput = Entry(self.contentFrame)
		self.ARPInput.pack()
		self.PVARP = Label(self.contentFrame, text="Post Ventricular Atrial Refractory Period (ms)").pack()
		self.PVARPInput = Entry(self.contentFrame)
		self.PVARPInput.pack()
		self.RateSmoothingLabel = Label(self.contentFrame, text="Rate Smoothing (%)").pack()
		self.RS = StringVar(self.contentFrame)
		self.RS.set("OFF") #Default
		self.RateSmoothingInput = OptionMenu(self.contentFrame,self.RS,"OFF","3","6","9","12","15","18","21","25")
		self.RateSmoothingInput.pack()
		self.ActivityThresholdLabel = Label(self.contentFrame, text="Activity Threshold ").pack()
		self.ATI = StringVar(self.contentFrame) 
		self.ATI.set("Medium") #Default
		self.ActivityThresholdInput	= OptionMenu(self.contentFrame,self.ATI,"High","Medium","Low") 
		self.ActivityThresholdInput.pack()
		self.ReactionTimeLabel = Label(self.contentFrame, text="Reaction Time (ms)").pack()
		self.ReactionTimeInput = Entry(self.contentFrame)
		self.ReactionTimeInput.pack()
		self.ResponseFactorLabel = Label(self.contentFrame, text="Response Factor").pack()
		self.ResponseFactorInput = Entry(self.contentFrame)
		self.ResponseFactorInput.pack()
		self.RecoveryTimeLabel = Label(self.contentFrame, text="Recovery Time (min)").pack()
		self.RecoveryTimeInput = Entry(self.contentFrame)
		self.RecoveryTimeInput.pack()


# 	def AOO(self):
# 		self.removeContent()
# 		self.AOOcontent = Label(self.contentFrame, text ="AOO Programmable Variables").grid(row=0, column=3)

# 		#programmable parameters inputs
# 		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit (BPM)").grid(row=1, column=3)
# 		self.LRLInput = Entry(self.contentFrame)
# 		self.LRLInput.grid(row=0, column=3)
# 		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit (BPM)").grid(row=0, column=3)
# 		self.URLInput = Entry(self.contentFrame)
# 		self.URLInput.grid(row=0, column=3)
# 		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude (V)").grid(row=0, column=3)
# 		self.AtrApmlitudeInput = Entry(self.contentFrame)
# 		self.AtrApmlitudeInput.grid(row=0, column=3)
# 		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width (ms)").grid(row=0, column=3)
# 		self.AtrPulseWidthInput = Entry(self.contentFrame)
# 		self.AtrPulseWidthInput.grid(row=0, column=3)
# 		# call the write fuctions stored in the parameters.py module
# 		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeAOO(self.LRLInput.get(),self.URLInput.get(),self.AtrApmlitudeInput.get(),self.AtrPulseWidthInput.get())).grid(row=0, column=3) # Saves the parameters to the master file
# 		# Other menu buttons
# 		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).grid(row=0, column=3,sticky="S")
# 		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: readtosend.readparameters(1)).grid(row=0, column=3, sticky="S")
# 		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).grid(row=0, column=3,sticky="S") #OFF button
# 		self.addTxRxDisplay() # add the txrx setup

# 	def AAI(self):
# 		self.removeContent()
# 		self.AAIcontent = Label(self.contentFrame, text ="AAI Programmable Variables").pack()
				
# 		#programmable parameters inputs
# 		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit (BPM)").pack()
# 		self.LRLInput = Entry(self.contentFrame)
# 		self.LRLInput.pack()
# 		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit (BPM)").pack()
# 		self.URLInput = Entry(self.contentFrame)
# 		self.URLInput.pack()
# 		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude (V)").pack()
# 		self.AtrApmlitudeInput = Entry(self.contentFrame)
# 		self.AtrApmlitudeInput.pack()
# 		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width (ms)").pack()
# 		self.AtrPulseWidthInput = Entry(self.contentFrame)
# 		self.AtrPulseWidthInput.pack()
# 		self.ARP = Label(self.contentFrame, text="Atrial Refractory Period (ms)").pack()
# 		self.ARPInput = Entry(self.contentFrame)
# 		self.ARPInput.pack()
# 		self.PVARP = Label(self.contentFrame, text="Post Ventricular Atrial Refractory Period (ms)").pack()
# 		self.PVARPInput = Entry(self.contentFrame)
# 		self.PVARPInput.pack()
# 		self.AtrSensitivitiyLabel = Label(self.contentFrame, text="Atrial Sensitivity (V)").pack()  
# 		self.AtrSensitivityInput = Entry(self.contentFrame)
# 		self.AtrSensitivityInput.pack()
		
# 		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeAAI(self.LRLInput.get(),self.URLInput.get(),self.AtrApmlitudeInput.get(),self.AtrPulseWidthInput.get(),self.ARPInput.get(),self.PVARPInput.get(),self.AtrSensitivityInput.get())).pack()  # Saves the parameters to the master file

# 		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
# 		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: readtosend.readparameters(2)).pack(side=LEFT)
# 		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
# 		self.addTxRxDisplay() # add the txrx setup

		
# 	def VOO(self):
# 		self.removeContent()
# 		self.VOOcontent = Label(self.contentFrame, text ="VOO Programmable Variables").pack()
				
# 		# programmable parameters inputs
# 		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit (BPM)").pack()
# 		self.LRLInput = Entry(self.contentFrame)
# 		self.LRLInput.pack()
# 		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit (BPM)").pack()
# 		self.URLInput = Entry(self.contentFrame)
# 		self.URLInput.pack()
# 		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude (V)").pack()
# 		self.VentAmplitudeInput = Entry(self.contentFrame)
# 		self.VentAmplitudeInput.pack()
# 		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width (ms)").pack()
# 		self.VentPulseWidthInput = Entry(self.contentFrame)
# 		self.VentPulseWidthInput.pack()

# 		#save parameters button
# 		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeVOO(self.LRLInput.get(),self.URLInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get())).pack()  # Saves the parameters to the master file

# 		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
# 		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: readtosend.readparameters(3)).pack(side=LEFT)
# 		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
# 		self.addTxRxDisplay() # add the txrx setup


# 	def VVI(self):
# 		self.removeContent()
# 		self.VIIcontent = Label(self.contentFrame, text ="VVI Programmable Variables").pack()
				
# 		# programmable parameters inputs
# 		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit (BPM)").pack()
# 		self.LRLInput = Entry(self.contentFrame)
# 		self.LRLInput.pack()
# 		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit (BPM)").pack()
# 		self.URLInput = Entry(self.contentFrame)
# 		self.URLInput.pack()
# 		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude (V)").pack()
# 		self.VentAmplitudeInput = Entry(self.contentFrame)
# 		self.VentAmplitudeInput.pack()
# 		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width (ms)").pack()
# 		self.VentPulseWidthInput = Entry(self.contentFrame)
# 		self.VentPulseWidthInput.pack()
# 		self.VRP = Label(self.contentFrame, text="Ventricular Refractory Period (ms)").pack()
# 		self.VRPInput = Entry(self.contentFrame)
# 		self.VRPInput.pack()
# 		self.VentSensitivitiyLabel = Label(self.contentFrame, text="Ventricular Sensitivity (V)").pack()  ##HAVE TO CHANGE IN PARAMETERS FILE
# 		self.VentSensitivityInput = Entry(self.contentFrame)
# 		self.VentSensitivityInput.pack()

# 		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeVVI(self.LRLInput.get(),self.URLInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get(),self.VRPInput.get(),self.VentSensitivityInput.get())).pack()  # Saves the parameters to the master file

# 		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
# 		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: readtosend.readparameters(4)).pack(side=LEFT)
# 		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
# 		self.addTxRxDisplay() # add the txrx setup

# 	def DOO(self):
# 		self.removeContent()
# 		self.DOOcontent = Label(self.contentFrame, text ="DOO Programmable Variables").pack()
				
# 		# programmable parameters inputs
# 		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit (BPM)").pack()
# 		self.LRLInput = Entry(self.contentFrame)
# 		self.LRLInput.pack()
# 		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit (BPM)").pack()
# 		self.URLInput = Entry(self.contentFrame)
# 		self.URLInput.pack()
# 		self.FixedAVDelayLabel = Label(self.contentFrame, text="Fixed AV Delay (ms)").pack()
# 		self.FixedAVDelayInput = Entry(self.contentFrame)
# 		self.FixedAVDelayInput.pack()
# 		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude (V)").pack()
# 		self.AtrAmplitudeInput = Entry(self.contentFrame)
# 		self.AtrAmplitudeInput.pack()
# 		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width (ms)").pack()
# 		self.AtrPulseWidthInput = Entry(self.contentFrame)
# 		self.AtrPulseWidthInput.pack()
# 		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude (V)").pack()
# 		self.VentAmplitudeInput = Entry(self.contentFrame)
# 		self.VentAmplitudeInput.pack()
# 		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width (ms)").pack()
# 		self.VentPulseWidthInput = Entry(self.contentFrame)
# 		self.VentPulseWidthInput.pack()

# 		#save parameters button - will have to be updated
# 		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeDOO(self.LRLInput.get(),self.URLInput.get(),self.FixedAVDelayInput.get(),self.AtrAmplitudeInput.get(),self.AtrPulseWidthInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get())).pack()  # Saves the parameters to the master file

# 		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
# 		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: readtosend.readparameters(5)).pack(side=LEFT)
# 		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
# 		self.addTxRxDisplay() # add the txrx setup

# 	def AOOR(self):
# 		self.removeContent()
# 		self.AOORcontent = Label(self.contentFrame, text ="AOOR Programmable Variables").pack()

# 		#programmable parameters inputs
# 		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit (BPM)").pack()
# 		self.LRLInput = Entry(self.contentFrame)
# 		self.LRLInput.pack()
# 		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit (BPM)").pack()
# 		self.URLInput = Entry(self.contentFrame)
# 		self.URLInput.pack()
# 		self.MaxSensorRateLabel = Label(self.contentFrame, text="Maximum Sensor Rate (BPM)").pack()
# 		self.MaxSensorRateInput = Entry(self.contentFrame)
# 		self.MaxSensorRateInput.pack()
# 		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude (V)").pack()
# 		self.AtrAmplitudeInput = Entry(self.contentFrame)
# 		self.AtrAmplitudeInput.pack()
# 		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width (ms)").pack()
# 		self.AtrPulseWidthInput = Entry(self.contentFrame)
# 		self.AtrPulseWidthInput.pack()
# 		self.ActivityThresholdLabel = Label(self.contentFrame, text="Activity Threshold").pack()
# 		self.ATI = StringVar(self.contentFrame) #dummy definition
# 		self.ATI.set("Medium") #Default
# 		self.ActivityThresholdInput	= OptionMenu(self.contentFrame,self.ATI,"High","Medium","Low") #These dropdowns might come back around to fuck me in serial communication
# 		self.ActivityThresholdInput.pack()
# 		self.ReactionTimeLabel = Label(self.contentFrame, text="Reaction Time (ms)").pack()
# 		self.ReactionTimeInput = Entry(self.contentFrame)
# 		self.ReactionTimeInput.pack()
# 		self.ResponseFactorLabel = Label(self.contentFrame, text="Response Factor").pack()
# 		self.ResponseFactorInput = Entry(self.contentFrame)
# 		self.ResponseFactorInput.pack()
# 		self.RecoveryTimeLabel = Label(self.contentFrame, text="Recovery Time (min)").pack()
# 		self.RecoveryTimeInput = Entry(self.contentFrame)
# 		self.RecoveryTimeInput.pack()

# 		# call the write fuctions stored in the parameters.py module
# 		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeAOOR(self.LRLInput.get(),self.URLInput.get(),self.MaxSensorRateInput.get(),self.AtrAmplitudeInput.get(),self.AtrPulseWidthInput.get(),self.ATI.get(),self.ReactionTimeInput.get(),self.ResponseFactorInput.get(),self.RecoveryTimeInput.get())).pack()  # Saves the parameters to the master file
		
# 		# Other menu buttons
# 		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
# 		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: readtosend.readparameters(6)).pack(side=LEFT)
# 		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
# 		self.addTxRxDisplay() # add the txrx setup

# 	def AAIR(self):  
# 		self.removeContent()
# 		self.AAIRcontent = Label(self.contentFrame, text ="AAIR Programmable Variables").pack()
				
# 		#programmable parameters inputs
# 		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit (BPM)").pack()
# 		self.LRLInput = Entry(self.contentFrame)
# 		self.LRLInput.pack()
# 		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit (BPM)").pack()
# 		self.URLInput = Entry(self.contentFrame)
# 		self.URLInput.pack()
# 		self.MaxSensorRateLabel = Label(self.contentFrame, text="Maximum Sensor Rate (BPM)").pack()
# 		self.MaxSensorRateInput = Entry(self.contentFrame)
# 		self.MaxSensorRateInput.pack()
# 		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude (V)").pack()
# 		self.AtrAmplitudeInput = Entry(self.contentFrame)
# 		self.AtrAmplitudeInput.pack()
# 		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width (ms)").pack()
# 		self.AtrPulseWidthInput = Entry(self.contentFrame)
# 		self.AtrPulseWidthInput.pack()
# 		self.ARP = Label(self.contentFrame, text="Atrial Refractory Period (ms)").pack()
# 		self.ARPInput = Entry(self.contentFrame)
# 		self.ARPInput.pack()
# 		self.PVARP = Label(self.contentFrame, text="Post Ventricular Atrial Refractory Period (ms)").pack()
# 		self.PVARPInput = Entry(self.contentFrame)
# 		self.PVARPInput.pack()
# 		self.AtrSensitivitiyLabel = Label(self.contentFrame, text="Atrial Sensitivity (V)").pack() 
# 		self.AtrSensitivityInput = Entry(self.contentFrame)
# 		self.AtrSensitivityInput.pack()
# 		# self.HysteresisLabel = Label(self.contentFrame, text="Hysteresis").pack()
# 		# self.HysteresisInput = Entry(self.contentFrame)
# 		# self.HysteresisInput.pack() 
# 		self.RateSmoothingLabel = Label(self.contentFrame, text="Rate Smoothing (%)").pack()
# 		self.RS = StringVar(self.contentFrame)
# 		self.RS.set("OFF") #Default
# 		self.RateSmoothingInput = OptionMenu(self.contentFrame,self.RS,"OFF","3","6","9","12","15","18","21","25")
# 		self.RateSmoothingInput.pack()
# 		self.ActivityThresholdLabel = Label(self.contentFrame, text="Activity Threshold").pack()
# 		self.ATI = StringVar(self.contentFrame) 
# 		self.ATI.set("Medium") #Default
# 		self.ActivityThresholdInput	= OptionMenu(self.contentFrame,self.ATI,"High","Medium","Low") 
# 		self.ActivityThresholdInput.pack()
# 		self.ReactionTimeLabel = Label(self.contentFrame, text="Reaction Time (ms)").pack()
# 		self.ReactionTimeInput = Entry(self.contentFrame)
# 		self.ReactionTimeInput.pack()
# 		self.ResponseFactorLabel = Label(self.contentFrame, text="Response Factor").pack()  ## this value should be from 1-16 (it's a factor, so no units)
# 		self.ResponseFactorInput = Entry(self.contentFrame)
# 		self.ResponseFactorInput.pack()
# 		self.RecoveryTimeLabel = Label(self.contentFrame, text="Recovery Time (min)").pack()
# 		self.RecoveryTimeInput = Entry(self.contentFrame)
# 		self.RecoveryTimeInput.pack()

# 		# Going to have to modify this button functions
# 		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeAAIR(self.LRLInput.get(),self.URLInput.get(),self.MaxSensorRateInput.get(),self.AtrAmplitudeInput.get(),self.AtrPulseWidthInput.get(),self.ARPInput.get(),self.PVARPInput.get(),self.AtrSensitivityInput.get(),self.RS.get(),self.ATI.get(),self.ReactionTimeInput.get(),self.ResponseFactorInput.get(),self.RecoveryTimeInput.get())).pack()  # Saves the parameters to the master file

# 		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
# 		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: readtosend.readparameters(7)).pack(side=LEFT)
# 		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
# 		self.addTxRxDisplay() # add the txrx setup

# 	def VOOR(self): 
# 		self.removeContent()
# 		self.VOORcontent = Label(self.contentFrame, text ="VOOR Programmable Variables").pack()
				
# 		# programmable parameters inputs
# 		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit (BPM)").pack()
# 		self.LRLInput = Entry(self.contentFrame)
# 		self.LRLInput.pack()
# 		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit (BPM)").pack()
# 		self.URLInput = Entry(self.contentFrame)
# 		self.URLInput.pack()
# 		self.MaxSensorRateLabel = Label(self.contentFrame, text="Maximum Sensor Rate (BPM)").pack()
# 		self.MaxSensorRateInput = Entry(self.contentFrame)
# 		self.MaxSensorRateInput.pack()
# 		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude (V)").pack()
# 		self.VentAmplitudeInput = Entry(self.contentFrame)
# 		self.VentAmplitudeInput.pack()
# 		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width (ms)").pack()
# 		self.VentPulseWidthInput = Entry(self.contentFrame)
# 		self.VentPulseWidthInput.pack()
# 		self.ActivityThresholdLabel = Label(self.contentFrame, text="Activity Threshold").pack()
# 		self.ATI = StringVar(self.contentFrame) 
# 		self.ATI.set("Medium") #Default
# 		self.ActivityThresholdInput	= OptionMenu(self.contentFrame,self.ATI,"High","Medium","Low") 
# 		self.ActivityThresholdInput.pack()
# 		self.ReactionTimeLabel = Label(self.contentFrame, text="Reaction Time (ms)").pack()
# 		self.ReactionTimeInput = Entry(self.contentFrame)
# 		self.ReactionTimeInput.pack()
# 		self.ResponseFactorLabel = Label(self.contentFrame, text="Response Factor").pack() #Factor so no units should be 1-16 range
# 		self.ResponseFactorInput = Entry(self.contentFrame)
# 		self.ResponseFactorInput.pack()
# 		self.RecoveryTimeLabel = Label(self.contentFrame, text="Recovery Time (min)").pack() 
# 		self.RecoveryTimeInput = Entry(self.contentFrame)
# 		self.RecoveryTimeInput.pack()


# 		# Going to have to modify this button function
# 		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeVOOR(self.LRLInput.get(),self.URLInput.get(),self.MaxSensorRateInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get(),self.ATI.get(),self.ReactionTimeInput.get(),self.ResponseFactorInput.get(),self.RecoveryTimeInput.get())).pack()  # Saves the parameters to the master file

# 		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
# 		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: readtosend.readparameters(8)).pack(side=LEFT)
# 		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
# 		self.addTxRxDisplay() # add the txrx setup

# 	def VVIR(self):
# 		self.removeContent()
# 		self.VIIRcontent = Label(self.contentFrame, text ="VVIR Programmable Variables").pack()
				
# 		# programmable parameters inputs
# 		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit (BPM)").pack()
# 		self.LRLInput = Entry(self.contentFrame)
# 		self.LRLInput.pack()
# 		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit (BPM)").pack()
# 		self.URLInput = Entry(self.contentFrame)
# 		self.URLInput.pack()
# 		self.MaxSensorRateLabel = Label(self.contentFrame, text="Maximum Sensor Rate (BPM)").pack()
# 		self.MaxSensorRateInput = Entry(self.contentFrame)
# 		self.MaxSensorRateInput.pack()
# 		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude (V)").pack()
# 		self.VentAmplitudeInput = Entry(self.contentFrame)
# 		self.VentAmplitudeInput.pack()
# 		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width (ms)").pack()
# 		self.VentPulseWidthInput = Entry(self.contentFrame)
# 		self.VentPulseWidthInput.pack()
# 		self.VRP = Label(self.contentFrame, text="Ventricular Refractory Period (ms)").pack()
# 		self.VRPInput = Entry(self.contentFrame)
# 		self.VRPInput.pack()
# 		self.VentSensitivitiyLabel = Label(self.contentFrame, text="Ventricular Sensitivity (V)").pack()  
# 		self.VentSensitivityInput = Entry(self.contentFrame)
# 		self.VentSensitivityInput.pack()
# 		# self.HysteresisLabel = Label(self.contentFrame, text="Hysteresis").pack()
# 		# self.HysteresisInput = Entry(self.contentFrame)
# 		# self.HysteresisInput.pack()
# 		self.RateSmoothingLabel = Label(self.contentFrame, text="Rate Smoothing (%)").pack()
# 		self.RS = StringVar(self.contentFrame)
# 		self.RS.set("OFF") #Default
# 		self.RateSmoothingInput = OptionMenu(self.contentFrame,self.RS,"OFF","3","6","9","12","15","18","21","25")
# 		self.RateSmoothingInput.pack()
# 		self.ActivityThresholdLabel = Label(self.contentFrame, text="Activity Threshold").pack()
# 		self.ATI = StringVar(self.contentFrame) 
# 		self.ATI.set("Medium") #Default
# 		self.ActivityThresholdInput	= OptionMenu(self.contentFrame,self.ATI,"High","Medium","Low") 
# 		self.ActivityThresholdInput.pack()
# 		self.ReactionTimeLabel = Label(self.contentFrame, text="Reaction Time (ms)").pack()
# 		self.ReactionTimeInput = Entry(self.contentFrame)
# 		self.ReactionTimeInput.pack()
# 		self.ResponseFactorLabel = Label(self.contentFrame, text="Response Factor").pack()
# 		self.ResponseFactorInput = Entry(self.contentFrame)
# 		self.ResponseFactorInput.pack()
# 		self.RecoveryTimeLabel = Label(self.contentFrame, text="Recovery Time (min)").pack()
# 		self.RecoveryTimeInput = Entry(self.contentFrame)
# 		self.RecoveryTimeInput.pack()

# 		# write inputs to file
# 		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeVVIR(self.LRLInput.get(),self.URLInput.get(),self.MaxSensorRateInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get(),self.VRPInput.get(),self.VentSensitivityInput.get(),self.RS.get(),self.ATI.get(),self.ReactionTimeInput.get(),self.ResponseFactorInput.get(),self.RecoveryTimeInput.get())).pack()  # Saves the parameters to the master file

# 		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
# 		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: readtosend.readparameters(9)).pack(side=LEFT)
# 		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
# 		self.addTxRxDisplay() # add the txrx setup

# 	def DOOR(self):
# 		self.removeContent()
# 		self.DOORcontent = Label(self.contentFrame, text ="DOOR Programmable Variables").pack()
				
# 		# programmable parameters inputs
# 		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit (BPM)").pack()
# 		self.LRLInput = Entry(self.contentFrame)
# 		self.LRLInput.pack()
# 		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit (BPM)").pack()
# 		self.URLInput = Entry(self.contentFrame)
# 		self.URLInput.pack()
# 		self.MaxSensorRateLabel = Label(self.contentFrame, text="Maximum Sensor Rate (BPM)").pack()
# 		self.MaxSensorRateInput = Entry(self.contentFrame)
# 		self.MaxSensorRateInput.pack()
# 		self.FixedAVDelayLabel = Label(self.contentFrame, text="Fixed AV Delay (V)").pack()
# 		self.FixedAVDelayInput = Entry(self.contentFrame)
# 		self.FixedAVDelayInput.pack()
# 		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude (V)").pack()
# 		self.AtrAmplitudeInput = Entry(self.contentFrame)
# 		self.AtrAmplitudeInput.pack()
# 		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width (ms)").pack()
# 		self.AtrPulseWidthInput = Entry(self.contentFrame)
# 		self.AtrPulseWidthInput.pack()
# 		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude (V)").pack()
# 		self.VentAmplitudeInput = Entry(self.contentFrame)
# 		self.VentAmplitudeInput.pack()
# 		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width (ms)").pack()
# 		self.VentPulseWidthInput = Entry(self.contentFrame)
# 		self.VentPulseWidthInput.pack()
# 		self.ActivityThresholdLabel = Label(self.contentFrame, text="Activity Threshold ").pack()
# 		self.ATI = StringVar(self.contentFrame) 
# 		self.ATI.set("Medium") #Default
# 		self.ActivityThresholdInput	= OptionMenu(self.contentFrame,self.ATI,"High","Medium","Low") 
# 		self.ActivityThresholdInput.pack()
# 		self.ReactionTimeLabel = Label(self.contentFrame, text="Reaction Time (ms)").pack()
# 		self.ReactionTimeInput = Entry(self.contentFrame)
# 		self.ReactionTimeInput.pack()
# 		self.ResponseFactorLabel = Label(self.contentFrame, text="Response Factor").pack()
# 		self.ResponseFactorInput = Entry(self.contentFrame)
# 		self.ResponseFactorInput.pack()
# 		self.RecoveryTimeLabel = Label(self.contentFrame, text="Recovery Time (min)").pack()
# 		self.RecoveryTimeInput = Entry(self.contentFrame)
# 		self.RecoveryTimeInput.pack()

# 		#save parameters button - will have to be updated
# 		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeDOOR(self.LRLInput.get(),self.URLInput.get(),self.MaxSensorRateInput.get(),self.FixedAVDelayInput.get(),self.AtrAmplitudeInput.get(),self.AtrPulseWidthInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get(),self.ATI.get(),self.ReactionTimeInput.get(),self.ResponseFactorInput.get(),self.RecoveryTimeInput.get())).pack()  # Saves the parameters to the master file

# 		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
# 		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: readtosend.readparameters(10)).pack(side=LEFT)
# 		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
# 		self.addTxRxDisplay() # add the txrx setup


# # Test case idea, go through every piece of text to check that the units make sense
# # Try to break the stuff 



# ## BONUS (Only do once all else is done)  
# # More functions exist beyond this one \/

# 	def DDDR(self):
# 		self.removeContent()
# 		self.DDDRcontent = Label(self.contentFrame, text ="DDDR Programmable Variables").pack()
				
# 		# programmable parameters inputs
# 		self.LRLLabel = Label(self.contentFrame, text = "Lower Rate Limit").pack()
# 		self.LRLInput = Entry(self.contentFrame)
# 		self.LRLInput.pack()
# 		self.URLLabel = Label(self.contentFrame, text="Upper Rate Limit").pack()
# 		self.URLInput = Entry(self.contentFrame)
# 		self.URLInput.pack()
# 		self.MaxSensorRateLabel = Label(self.contentFrame, text="Maximum Sensor Rate (ms?)").pack()
# 		self.MaxSensorRateInput = Entry(self.contentFrame)
# 		self.MaxSensorRateInput.pack()
# 		self.FixedAVDelayLabel = Label(self.contentFrame, text="Fixed AV Delay (ms)").pack()
# 		self.FixedAVDelayInput = Entry(self.contentFrame)
# 		self.FixedAVDelayInput.pack()
# 		self.DynamicAVDelayLabel = Label(self.contentFrame, text="Dynamic AV Delay (ms)").pack()
# 		self.DynamicAVDelayInput = Entry(self.contentFrame)
# 		self.DynamicAVDelayInput.pack()
# 		self.SensedAVDelayOffsetLabel = Label(self.contentFrame, text="Sensed AV Delay Offset (ms)").pack()
# 		self.SensedAVDelayOffsetInput = Entry(self.contentFrame)
# 		self.SensedAVDelayOffsetInput.pack()
# 		self.AtrAmplitudeLabel = Label(self.contentFrame, text="Atrial Amplitude").pack()
# 		self.AtrApmlitudeInput = Entry(self.contentFrame)
# 		self.AtrApmlitudeInput.pack()
# 		self.AtrPulseWidthLabel = Label(self.contentFrame, text="Atrial Pulse Width").pack()
# 		self.AtrPulseWidthInput = Entry(self.contentFrame)
# 		self.AtrPulseWidthInput.pack()
# 		self.VentAmplitudeLabel = Label(self.contentFrame, text="Ventricular Amplitude").pack()
# 		self.VentAmplitudeInput = Entry(self.contentFrame)
# 		self.VentAmplitudeInput.pack()
# 		self.VentPulseWidthLabel = Label(self.contentFrame, text="Ventricular Pulse Width").pack()
# 		self.VentPulseWidthInput = Entry(self.contentFrame)
# 		self.VentPulseWidthInput.pack()
# 		self.VRP = Label(self.contentFrame, text="Ventricular Refractory Period (VRP)").pack()
# 		self.VRPInput = Entry(self.contentFrame)
# 		self.VRPInput.pack()
# 		self.ARP = Label(self.contentFrame, text="Atrial Refractory Period (ARP)").pack()
# 		self.ARPInput = Entry(self.contentFrame)
# 		self.ARPInput.pack()
# 		self.HysteresisLabel = Label(self.contentFrame, text="Hysteresis").pack()
# 		self.HysteresisInput = Entry(self.contentFrame)
# 		self.HysteresisInput.pack()
# 		self.RateSmoothingLabel = Label(self.contentFrame, text="Rate Smoothing").pack()
# 		self.RateSmoothingInput = Entry(self.contentFrame)
# 		self.RateSmoothingInput.pack()
# 		## ATR Mode (on/off button?)
# 		# ATR Fallback - fallback to VVIR
# 		# ATR Duration - Atrial tachycardia happens, wait a programmed number of cariac cycles
# 		self.ATRDurationLabel = Label(self.contentFrame, text="ATR Duration").pack()
# 		self.ATRDurationInput = Entry(self.contentFrame)
# 		self.ATRDurationInput.pack()
# 		self.ActivityThresholdLabel = Label(self.contentFrame, text="Activity Threshold").pack()
# 		self.ATI = StringVar(self.contentFrame) #IDK why this works but it does (i think the variable just needed to be defined)
# 		self.ATI.set("Medium") #Default
# 		self.ActivityThresholdInput	= OptionMenu(self.contentFrame,self.ATI,"High","Medium","Low") 
# 		self.ReactionTimeLabel = Label(self.contentFrame, text="Reaction Time").pack()
# 		self.ReactionTimeInput = Entry(self.contentFrame)
# 		self.ReactionTimeInput.pack()
# 		self.ResponseFactorLabel = Label(self.contentFrame, text="Response Factor").pack()
# 		self.ResponseFactorInput = Entry(self.contentFrame)
# 		self.ResponseFactorInput.pack()
# 		self.RecoveryTimeLabel = Label(self.contentFrame, text="Recovery Time").pack()
# 		self.RecoveryTimeInput = Entry(self.contentFrame)
# 		self.RecoveryTimeInput.pack()

# 		#save parameters button - will have to be updated
# 		# self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:parameters.writeVVI(self.LRLInput.get(),self.URLInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get(),self.VRPInput.get())).pack()  # Saves the parameters to the master file

# 		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
# 		self.textbutton = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
# 		self.textbutton2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
# 		self.addTxRxDisplay() # add the txrx setup


		# add an indicator button at bottom of the screen that tells us if we are transmitting/receiving
	def addTxRxDisplay(self):

		self.txrx = Button(self.optionsFrame, text ="Transmitting/Receiving", bg="white", fg="black")
		self.txrx.grid()
		self.txrx.configure(state=DISABLED)
		
        # call colorTxRx(1) to turn indicator light on and (0) to turn it off
	def colorTxRx(self, type):
		if (type==1):
			self.txrx.configure(bg="lightgreen")
		else:
			self.txrx.configure(bg="white")

