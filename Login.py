import tkinter as tk



color_Button= {'bd': 5, 'fg': '#000', 'bg': '#ccffff','font': ('sans-serif', 17, 'bold')}

'''Function open caculator '''
def click_open_calculator():
    login.destroy()
    import Calculator
    
   
def click_open_graph_calculator():
	login.destroy()
	import Graph_Calculator
	
def click_open_unit_change():
	login.destroy()
	import Unit_Change
	
	
#window
login=tk.Tk()
login.configure(bg="#293C4A", bd=10)
login.title("login")
login.geometry("250x420")

'''Button open calculator'''
b_calculator=tk.Button(text="Calculator",width=15,height=4,command=click_open_calculator,**color_Button)
b_calculator.grid(row=0,column=2)

b_graph_calculator=tk.Button(text="Graph Calculator",width=15,height=4,command=click_open_graph_calculator,**color_Button)
b_graph_calculator.grid(row=1,column=2)

b_graph_calculator=tk.Button(text="Unit Change",width=15,height=4,command=click_open_unit_change,**color_Button)
b_graph_calculator.grid(row=2,column=2)




login.mainloop()