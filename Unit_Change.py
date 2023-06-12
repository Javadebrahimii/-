import tkinter as tk
from tkinter import ttk

width=2
height=1
columnspan=5

color_Number= {'bd': 5, 'fg': '#000', 'bg': '#ccffcc','font': ('sans-serif', 17, 'bold')}

c={'bd': 5, 'fg': '#000', 'bg': '#FF5C33', 'font': ('sans-serif', 16, 'bold')}

e = {'bd': 5, 'fg': '#000', 'bg': '#5CD65C', 'font': ('sans-serif', 16, 'bold')}

style_label = {'bd': 5, 'font': ('sans-serif', 10, 'bold')}
style_equal = {'bd': 5,'font': ('sans-serif', 14, 'bold')}

def button_click(number):
        current_text = E1.get()
        E1.delete(0, tk.END)
        E1.insert(tk.END, current_text + number)

root = tk.Tk()
root.configure (bd=10)
root.title("Unit Change")
root.geometry("290x434")

#Number Buttons
b1 = tk.Button(text="1", **color_Number, command=lambda: button_click("1"),height=height,width=width)
b2 = tk.Button(text="2", **color_Number, command=lambda: button_click("2"),width=width,height=height)   
b3 = tk.Button(text="3", **color_Number, command=lambda: button_click("3"),width=width,height=height)
b4 = tk.Button(text="4", **color_Number, command=lambda: button_click("4"),height=height,width=width)
b5 = tk.Button(text="5", **color_Number, command=lambda: button_click("5"),width=width,height=height)
b6 = tk.Button(text="6", **color_Number, command=lambda: button_click("6"),width=width,height=height)
b7 = tk.Button(text="7", **color_Number, command=lambda: button_click("7"),width=width,height=height)
b8 = tk.Button(text="8", **color_Number, command=lambda: button_click("8"),width=width,height=height)
b9 = tk.Button(text="9", **color_Number, command=lambda: button_click("9"),width=width,height=height)
b0 = tk.Button(text="0", **color_Number, command=lambda: button_click("0"),width=width,height=height)

    
#run_number_Buttons
b1.grid(row=13, column=0,sticky="nsew")
b2.grid(row=13, column=1,sticky="nsew")
b3.grid(row=13, column=2,sticky="nsew")
b4.grid(row=13, column=3,sticky="nsew")
b5.grid(row=14, column=0,sticky="nsew")
b6.grid(row=14, column=1,sticky="nsew")
b7.grid(row=14, column=2,sticky="nsew")
b8.grid(row=14, column=3,sticky="nsew")
b9.grid(row=15, column=0,sticky="nsew")
b0.grid(row=15, column=1,columnspan=2,sticky="nsew")

#Button_equal
b_equal=tk.Button(text="=",**e)
b_equal.grid(row=14,column=4,rowspan=3,sticky="snew")

#Button_clear
b_clear = tk.Button(text="c", **c, command=lambda: E1.delete(0, tk.END),width=width,height=height)
b_clear.grid(row=13,column=4,sticky="nesw")

#Button pofloat
b_pofloat = tk.Button(text=".", **color_Number, command=lambda: button_click("."),width=width)
b_pofloat.grid(row=15,column=3,sticky="nesw")

# label
label_pleas_select_type_unit = tk.Label(text="Please select type unit :",**style_label)
label_pleas_select_type_unit.grid(row=1,column=0,columnspan=columnspan)

# create a combobox
box_unit= ttk.Combobox(width=40)

# get first 3 letters of every month name
box_unit['values'] = ["Length","Temperature","Time","Mass"]




# place the widget
box_unit.grid(row=2,column=0,columnspan=columnspan)
label_from = tk.Label(text="from :",**style_label)
label_from.grid(row=3,column=0,columnspan=columnspan)

box_select_from=ttk.Combobox(width=40)
		
box_select_from.grid(row=4,column=0,columnspan=columnspan)
label_enter_number = tk.Label(text="Enter Number:",**style_label)
label_enter_number.grid(row=5,column=0,columnspan=columnspan)

E1=tk.Entry(width=41)
E1.grid(row=7,column=0,columnspan=columnspan)
label_to = tk.Label(text="to :",**style_label)
label_to.grid(row=8,column=0,columnspan=columnspan)

box_select_to=ttk.Combobox(width=40)

box_select_to.grid(row=9,column=0,columnspan=columnspan)
label_answer = tk.Label(text="Answer :",**style_label)
label_answer.grid(row=10,column=0,columnspan=columnspan)

label_equal=tk.Label(**style_equal)
label_equal.grid(row=11,column=0,columnspan=columnspan)








def type_unit(m):
	z=box_unit.get()
	if z=="Length":
		box_select_from["values"]=("cm","m","km","inch")	
		box_select_to["values"]=("cm","m","km","inch")		
		
		def equal_Length():
			bs1=box_select_from.get()
			number=E1.get()
			bs2=box_select_to.get()
			
			if bs1 == "mm":
				if bs2 == "mm":
					label_equal["text"]=number
				elif bs2=="cm":
					label_equal["text"]=float(number)/10
				elif bs2=="m":
					label_equal["text"]=float(number)/1000	
				elif bs2=="km":
					label_equal["text"]=float(number)/1000000
				elif bs2 =="inch":
					label_equal["text"]=float(number)*0.0393700787
					
			elif bs1=="cm":
				if bs2== "mm":
					label_equal["text"]=float(number)*10
				elif bs2=="cm":
					label_equal["text"]=number
				elif bs2=="m":
					label_equal["text"]=float(number)/100
				elif bs2=="km":
					label_equal["text"]=float(number)/1000000
				elif bs2 =="inch":
					label_equal["text"]=float(number)*0.3937007874
					
			elif bs1=="m":
				if bs2== "mm":
					label_equal["text"]=float(number)*1000
				elif bs2=="cm":
					label_equal["text"]=float(number)/100
				elif bs2 == "m":
					label_equal["text"]=number
				elif bs2 =="km":
					label_equal["text"]=float(number)/1000
				elif bs2 =="inch":
					label_equal["text"]=float(number)*39.3700787402
					
			elif bs1 == "km":
				if bs2== "mm":
					label_equal["text"]=float(number)*1000000
				elif bs2 == "cm":
					label_equal["text"]=float(number)*100000
				elif bs2 == "m":
					label_equal["text"]=float(number)*1000
				elif bs2 =="km":
					label_equal["text"]=number
				elif bs2 =="inch":
					label_equal["text"]=float(number)*39370.078740157
					
			elif bs1 == "inch":
				if bs2== "mm":
					label_equal["text"]=float(number)*25.4
				elif bs2 == "cm":
					label_equal["text"]=float(number)*2.54
				elif bs2 == "m":
					label_equal["text"]=float(number)*0.0254
				elif bs2 == "km":
					label_equal["text"]=float(number)*0.0000254
				elif bs2 =="inch":
					label_equal["text"]=number	
				
				
		button_select_Length=tk.Button(text="=",command=equal_Length,**e)
		button_select_Length.grid(row=14,column=4,rowspan=3,sticky="nesw")

		
	elif z=="Time":
	
		box_select_from["values"]=("Second","Minutes","Hour")
	
		box_select_to["values"]=("Second","Minutes","Hour")
		
		
		def equal_Time():
			bs1=box_select_from.get()
			number=E1.get()
			bs2=box_select_to.get()
			if bs1 =="Second":
				if bs2 =="Second":
					label_equal["text"]=number
				elif bs2 =="Minutes":
					label_equal["text"]=float(number)/60
				elif bs2 =="Hour":
					label_equal["text"]=float(number)/3600
			elif bs1 == "Minutes":
				if bs2 == "Second":
					label_equal["text"]=float(number)*60
				elif bs2 =="Minutes":
					label_equal["text"]=number
				elif bs2 == "Hour":
					label_equal["text"]=float(number)/60
			elif bs1 == "Hour":
				if bs2 == "Second":
					label_equal["text"]=float(number)*3600
				elif bs2 == "Minutes":
					label_equal["text"]=float(number)*60
				elif bs2 == "Hour":
					label_equal["text"]=number																							
		button_select_T=tk.Button(text="=",command=equal_Time,**e)
		button_select_T.grid(row=14,column=4,rowspan=4,stick="nesw")		
				
						
	elif z == "Temperature":
		box_select_from["values"]=("C","F","K")	
		box_select_to["values"]=("C","F","K")
														
		def equal_T():
			bs1=box_select_from.get()
			number=E1.get()
			bs2=box_select_to.get()	
			
			if bs1 =="C":
				if bs2 =="C":
					label_equal["text"]=number
				elif bs2 =="F":
					label_equal["text"]=float(number) * 1.8+ 32
				elif bs2 =="K":
					label_equal["text"]=float(number)+273.15
						
			elif bs1 == "F":
				if bs2 == "C":
					label_equal["text"]=(float(number)-32)*(5/9)
				elif bs2 =="F":
					label_equal["text"]=number
				elif bs2 == "K":
					label_equal["text"]=(float(number)+459.67)*5/9
					
			elif bs1 == "K":
				if bs2 == "C":
					label_equal["text"]=float(number)-273.15
				elif bs2 == "F":
					label_equal["text"]=(float(number)*9/5)-459.67
				elif bs2 == "K":
					label_equal["text"]=number
		button_select_T=tk.Button(text="=",command=equal_T,**e)
		button_select_T.grid(row=14,column=4,rowspan=4,sticky="nesw")
		
	elif z== "Mass":
		box_select_from["values"]=("Gram","Kilogram","Ton")	
		box_select_to["values"]=("Gram","Kilogram","Ton")	
														
		def equal_Mass():
			bs1=box_select_from.get()
			number=E1.get()
			bs2=box_select_to.get()	
			
			if bs1 =="Gram":
				if bs2 =="Gram":
					label_equal["text"]=number
				elif bs2 =="Kilogram":
					label_equal["text"]=float(number) * 0.001
				elif bs2 =="Ton":
					label_equal["text"]=float(number)*0.000001
						
			elif bs1 == "Kilogram":
				if bs2 == "Gram":
					label_equal["text"]=(float(number))*1000
				elif bs2 =="Kilogram":
					label_equal["text"]=number
				elif bs2 == "Ton":
					label_equal["text"]=float(number)*0.001
					
			elif bs1 == "Ton":
				if bs2 == "Gram":
					label_equal["text"]=float(number)*1000000
				elif bs2 == "Kilogram":
					label_equal["text"]=float(number)*1000
				elif bs2 == "Ton":
					label_equal["text"]=number
		button_select_T=tk.Button(text="=",command=equal_Mass,**e)
		button_select_T.grid(row=14,column=4,rowspan=4,sticky="nesw")
		
		
box_unit.bind('<<ComboboxSelected>>', type_unit)



root.mainloop()