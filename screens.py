# this file has the contents that will go into the main frame for one of the options we are doing
from tkinter import * 
import settings

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
		self.back = Button(self.optionsFrame, text ="Logout", command = lambda: self.mainDisplay()).pack()  # This will be the logout function, have to return to other screen
	
	def AOO(self):
		self.removeContent()
		self.AOOcontent = Label(self.contentFrame, text ="AOO Programmable Variables").pack()

		# Add programmable variables
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
		
		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:self.writeAOO(self.LRLInput.get(),self.URLInput.get(),self.AtrApmlitudeInput.get(),self.AtrPulseWidthInput.get(),self.ARPInput.get())).pack()  # Saves the parameters to the master file

		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbuttonremoveme = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbuttonremoveme2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup

	def writeAOO(self,LRL,URL,AtrAmp,AtrPW,APR):
		file = open("parameters.txt","r")
		lines = file.readlines()
		file.close()
		count = 0
		for i in lines:
			i = i.strip() #removes problematic whitespace  ## TEST CASE??
			count = count+1 # count up the number of lines till we reach the user
			if (i==settings.user):  #user is a global variable, this checks to see if the user exists in the parameters file.
				for j in lines:  # This will bug if there is more than one user in the parameters file
					j = j.strip() #remove whitespace 
					count = count + 1  # count the number of lines until AOO is reached + lines to the current user (from previous loop)
					if (j == "AOO"):
						print("user global works, @AOO too")
						yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
						if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
							#delete next 4 values
							del lines[count:count+5] #delete items from count to count+4
							
							lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
							lines.insert(count+1, "\n"+"URL"+"\t"+URL)
							lines.insert(count+2, "\n"+"AtrAmp"+"\t"+AtrAmp)
							lines.insert(count+3, "\n"+"AtrPW"+"\t"+AtrPW)
							lines.insert(count+4, "\n"+"APR"+"\t"+APR+"\n")

							file = open("parameters.txt","w")
							lines = "".join(lines) # join the new lines variable

							file.write(lines) #write to the file
							file.close()
							break
							
						else:
							# write only
							lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
							lines.insert(count+1, "\n"+"URL"+"\t"+URL)
							lines.insert(count+2, "\n"+"AtrAmp"+"\t"+AtrAmp)
							lines.insert(count+3, "\n"+"AtrPW"+"\t"+AtrPW)
							lines.insert(count+4, "\n"+"APR"+"\t"+APR+"\n")

							file = open("parameters.txt","w")
							lines = "".join(lines) # join the new lines variable

							file.write(lines) #write to the file
							file.close()
							break

	def AAI(self):
		self.removeContent()
		self.AAIcontent = Label(self.contentFrame, text ="AAI Programmable Variables").pack()
				
		# Add programmable variables
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

		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:self.writeAAI(self.LRLInput.get(),self.URLInput.get(),self.AtrApmlitudeInput.get(),self.AtrPulseWidthInput.get(),self.ARPInput.get())).pack()  # Saves the parameters to the master file

		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbuttonremoveme = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbuttonremoveme2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup

	def writeAAI(self,LRL,URL,AtrAmp,AtrPW,APR): ## Same variables a write AAI just different naming convention
		file = open("parameters.txt","r")
		lines = file.readlines()
		file.close()
		count = 0
		for i in lines:
			count = count+1 # count up the number of lines till we reach the user
			i = i.strip() #removes problematic whitespace  ## TEST CASE??
			if (i==settings.user):  #user is a global variable, oh lordy hope i haven't used it yet.
				for j in lines:
					j = j.strip() #remove whitespace 
					count = count + 1  #counts the current line
					if (j == "AAI"):
						yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
						if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
							#delete next 4 values
							del lines[count:count+5] #delete items from count-1 to count+3
							
							lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
							lines.insert(count+1, "\n"+"URL"+"\t"+URL)
							lines.insert(count+2, "\n"+"AtrAmp"+"\t"+AtrAmp)
							lines.insert(count+3, "\n"+"AtrPW"+"\t"+AtrPW)
							lines.insert(count+4, "\n"+"APR"+"\t"+APR+"\n")

							file = open("parameters.txt","w")
							lines = "".join(lines) # join the new lines variable

							file.write(lines) #write to the file
							file.close()
							break
							
						else:
							# write only
							lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
							lines.insert(count+1, "\n"+"URL"+"\t"+URL)
							lines.insert(count+2, "\n"+"AtrAmp"+"\t"+AtrAmp)
							lines.insert(count+3, "\n"+"AtrPW"+"\t"+AtrPW)
							lines.insert(count+4, "\n"+"APR"+"\t"+APR+"\n")

							file = open("parameters.txt","w")
							lines = "".join(lines) # join the new lines variable

							file.write(lines) #write to the file
							file.close()
							break

		
	def VOO(self):
		self.removeContent()
		self.VOOcontent = Label(self.contentFrame, text ="VOO Programmable Variables").pack()
				
		# Add programmable variables with box for input
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

		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:self.writeVOO(self.LRLInput.get(),self.URLInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get(),self.VRPInput.get())).pack()  # Saves the parameters to the master file

		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbuttonremoveme = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbuttonremoveme2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup

	def writeVOO(self,LRL,URL,VentAmp,VentPW,VRP):
		file = open("parameters.txt","r")
		lines = file.readlines()
		file.close()
		count = 0
		for i in lines:
			i = i.strip() #removes problematic whitespace  ## TEST CASE??
			count = count+1 # count up the number of lines till we reach the user
			if (i==settings.user):  #user is a global variable, this checks to see if the user exists in the parameters file.
				for j in lines:  # This will bug if there is more than one user in the parameters file
					j = j.strip() #remove whitespace 
					count = count + 1  # count the number of lines until AOO is reached + lines to the current user (from previous loop)
					if (j == "VOO"):
						print("user global works, @VOO too")
						yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
						if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
							#delete next 4 values
							del lines[count:count+5] #delete items from count-1 to count+3
							
							lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
							lines.insert(count+1, "\n"+"URL"+"\t"+URL)
							lines.insert(count+2, "\n"+"VentAmp"+"\t"+VentAmp)
							lines.insert(count+3, "\n"+"VentPW"+"\t"+VentPW)
							lines.insert(count+4, "\n"+"VRP"+"\t"+VRP+"\n")

							file = open("parameters.txt","w")
							lines = "".join(lines) # join the new lines variable

							file.write(lines) #write to the file
							file.close()
							break
							
						else:
							# write only
							lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
							lines.insert(count+1, "\n"+"URL"+"\t"+URL)
							lines.insert(count+2, "\n"+"VentAmp"+"\t"+VentAmp)
							lines.insert(count+3, "\n"+"VentPW"+"\t"+VentPW)
							lines.insert(count+4, "\n"+"VRP"+"\t"+VRP+"\n")

							file = open("parameters.txt","w")
							lines = "".join(lines) # join the new lines variable

							file.write(lines) #write to the file
							file.close()
							break



	def VVI(self):
		self.removeContent()
		self.VIIcontent = Label(self.contentFrame, text ="VVI Programmable Variables").pack()
				
		# Add programmable variables
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

		self.write = Button(self.optionsFrame,text="Save Parameters",command=lambda:self.writeVVI(self.LRLInput.get(),self.URLInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get(),self.VRPInput.get())).pack()  # Saves the parameters to the master file

		self.back = Button(self.optionsFrame, text ="Back To Main Screen", command = lambda: self.mainScreen()).pack()
		self.textbuttonremoveme = Button(self.optionsFrame, text="Turn TxRx ON", command = lambda: self.colorTxRx(1)).pack(side=LEFT)
		self.textbuttonremoveme2=Button(self.optionsFrame, text="Turn TxRx OFF", command = lambda: self.colorTxRx(0)).pack(side=RIGHT)
		self.addTxRxDisplay() # add the txrx setup

	def writeVVI(self,LRL,URL,VentAmp,VentPW,VRP):  ## This is an edge test case wrt this being at the end of the file, it doesn't work the same. Ghetto solution is to Write LRL during registration, works now
		file = open("parameters.txt","r")
		lines = file.readlines()
		file.close()
		count = 0
		for i in lines:
			i = i.strip() #removes problematic whitespace  ## TEST CASE??
			count = count+1 # count up the number of lines till we reach the user
			if (i==settings.user):  #user is a global variable, this checks to see if the user exists in the parameters file.
				for j in lines:  # This will bug if there is more than one user in the parameters file
					j = j.strip() #remove whitespace 
					count = count + 1  # count the number of lines until AOO is reached + lines to the current user (from previous loop)
					if (j == "VVI"):
						print("user global works, @VVI too")
						print(count)
						yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
						print(yesLRL)
						if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
							#delete next 4 values
							del lines[count:count+5] #delete items from count-1 to count+3
							
							lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
							lines.insert(count+1, "\n"+"URL"+"\t"+URL)
							lines.insert(count+2, "\n"+"VentAmp"+"\t"+VentAmp)
							lines.insert(count+3, "\n"+"VentPW"+"\t"+VentPW)
							lines.insert(count+4, "\n"+"VRP"+"\t"+VRP+"\n")

							file = open("parameters.txt","w")
							lines = "".join(lines) # join the new lines variable

							file.write(lines) #write to the file
							file.close()
							break
							
						else:
							# write only
							lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
							lines.insert(count+1, "\n"+"URL"+"\t"+URL)
							lines.insert(count+2, "\n"+"VentAmp"+"\t"+VentAmp)
							lines.insert(count+3, "\n"+"VentPW"+"\t"+VentPW)
							lines.insert(count+4, "\n"+"VRP"+"\t"+VRP+"\n")

							file = open("parameters.txt","w")
							lines = "".join(lines) # join the new lines variable

							file.write(lines) #write to the file
							file.close()
							break

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

