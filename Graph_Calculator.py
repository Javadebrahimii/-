import tkinter as tk
from tkinter import ttk
from math import pow
from math import sin
from math import cos
from math import e
from math import pi
from math import log10
import matplotlib.pyplot as plt

def open_graph_calculator():
	
	Color_Button= {'bd': 8, 'fg': '#000', 'bg': '#ccffcc','font': ('sans-serif', 23, 'bold')}
	
	g = {'bd': 8, 'fg': '#000', 'bg': '#ffe6ff', 'font': ('sans-serif', 17, 'bold')}
	
	c={'bd': 8, 'fg': '#000', 'bg': '#FF5C33', 'font': ('sans-serif', 20, 'bold')}
	
	e = {'bd': 8, 'fg': '#000', 'bg': '#5CD65C', 'font': ('sans-serif', 20, 'bold')}
	
	p= {'bd': 8, 'fg': '#000', 'bg': '#b3ffff', 'font': ('sans-serif', 20, 'bold')}
	
	off={'bd': 5, 'fg': '#000', 'bg': '#ff8080', 'font': ('sans-serif', 16, 'bold')}
	
	#width=3
	#height=2
	
	def Accurate_draw():
		plt.close()
		plt.title("f(x)=" + E1.get(), color = "red")
		try:
			xpoints= [x*0.1 for x in range(-200,200) ]
			ypoints=[]
			for i in range(400):
				x=xpoints[i]
				formula=E1.get()
				g=eval(formula)	
				ypoints.append(g)
			plt.plot(xpoints, ypoints)
			plt.xlim(-19,19)
			plt.grid(linestyle = "dashed")
			
			plt.show()	
		except:
			xpoints= [x*0.1 for x in range(1,100) ]
			ypoints=[]
			for i in range(99):
				x=xpoints[i]
				formula=E1.get()
				g=eval(formula)	
				ypoints.append(g)
			plt.plot(xpoints, ypoints)
			plt.xlim(1,9)
			plt.grid(linestyle="dashed")
			plt.show()
								
													
														
																
	view_size = 20
	COMPUTATION_DISTANCE = 0.001
	ASYMPTOTE = 2.0
	
	
	def close_root():
	        root.destroy()
	        plt.close()
	
	
	def operator_click(operator):
		
		try:
			q=E1.get()
			t=q[-1]
			f=["1","2", "3","4","5","6" ,"7", "8", "9","0", "i","x","e"]
			if t in f:
				E1.insert(tk.END, "*" + operator)
			else:
				E1.insert(operator)
		except:
				E1.insert(tk.END, operator)
	
	'''simple operator= + , - , × , ÷ , ) , ( , ^ '''
	def simple_operator_click(simple_operator):
		E1.insert(tk.END, simple_operator)
	
	
	
	def equal_enter():
		draw_graph()
		
	
	
	def button_click(number):
		
		try:
		      q=E1.get()
		      t=q[-1]
		      f=["x","i"]
		      if t in f:
		      	E1.insert(tk.END, "*"+ number)
		      else:
	          	E1.insert(tk.END, number)
		except:
	     		 E1.insert(tk.END, number)
	       		
	     
	
	def translate(x_current, y_current):
	    tc = [0, 0]
	    x_mul = int(window_draw["width"]) / (view_size * 2)
	    y_mul = (int(window_draw["height"]) / (view_size * -2))
	    x_current = (x_current + view_size) * x_mul
	    y_current = (y_current + view_size) * y_mul + int(window_draw["height"])
	    tc[0] = x_current
	    tc[1] = y_current
	    return tc
	
	
	def draw_line(x_from, y_from, x_to, y_to):
	    from_coord = translate(x_from, y_from)
	    to_coord = translate(x_to, y_to)
	    if y_to - y_from > view_size * ASYMPTOTE or y_from - y_to > view_size * ASYMPTOTE:
	        from_coord = to_coord
	    window_draw.create_line(from_coord[0], from_coord[1], to_coord[0], to_coord[1])
	
	
	def draw_grid():
	    draw_line(view_size * -1, 0, view_size, 0 )
	    draw_line(0, view_size * -1, 0, view_size )
	
	
	def draw_graph(m):
	    window_draw.delete("all")
	    draw_grid()
	    y_previous = 0.0
	    x = view_size * -1
	    while x <= view_size:
	        try:
	            formula=E1.get()
	            y = eval(formula)
	            draw_line(x - COMPUTATION_DISTANCE * view_size, y_previous, x, y )
	        except NameError:
	        	E1.delete(0, tk.END)
	        	E1.insert(tk.END, "ERROR")
	        	break
	        except ValueError:
	        	E1.delete(0, tk.END)
	        	E1.insert(tk.END, "Click Accurate")
	        y_previous = y
	        x += COMPUTATION_DISTANCE * view_size
	
	
	
	
	
	root = tk.Tk()
	root.configure(bg="#293C4A", bd=10)
	root.title("grapg_Calculator")
	#root.geometry("490x580")
	
	
	
	
	window_draw= tk.Canvas()
	
	
	window_draw.grid(row=0, column=0, columnspan=6)
	
	# Entry
	E1= tk.Entry(font=('sans-serif', 20, 'bold'), 
	                     bd=9, bg='#BBB')
	E1.grid(row=1,column=0,columnspan=6,padx = 5, pady = 5,sticky="snew")
	
	
	# number_Buttons
	b1 = tk.Button(text="1", **Color_Button, command=lambda: button_click("1"),height=1,width=1)
	b2 = tk.Button(text="2", **Color_Button, command=lambda: button_click("2"),width=1,height=1)
	b3 = tk.Button(text="3", **Color_Button, command=lambda: button_click("3"),width=1,height=1)
	b4 = tk.Button(text="4", **Color_Button, command=lambda: button_click("4"),height=1,width=1)
	b5 = tk.Button(text="5", **Color_Button, command=lambda: button_click("5"),width=1,height=1)
	b6 = tk.Button(text="6", **Color_Button, command=lambda: button_click("6"),width=1,height=1)
	b7 = tk.Button(text="7", **Color_Button, command=lambda: button_click("7"),width=1,height=1)
	b8 = tk.Button(text="8", **Color_Button, command=lambda: button_click("8"),width=1,height=1)
	b9 = tk.Button(text="9", **Color_Button, command=lambda: button_click("9"),width=1,height=1)
	b0 = tk.Button(text="0", **Color_Button, command=lambda: button_click("0"),width=1,height=1)
	
	#run_number_Buttons
	b1.grid(row=4, column=0,sticky="nsew")
	b2.grid(row=4, column=1,sticky="nsew")
	b3.grid(row=4, column=2,sticky="nsew")
	b4.grid(row=4, column=3,sticky="nsew")
	b5.grid(row=5,column=0,sticky="nsew")
	b6.grid(row=5, column=1,sticky="nsew")
	b7.grid(row=5, column=2,sticky="nsew")
	b8.grid(row=5, column=3,sticky="nsew")
	b9.grid(row=6, column=0,sticky="nsew")
	b0.grid(row=6,column=1,sticky="nsew")
	
	
	
	#draw_grid()
	b_OFF=tk.Button(text="OFF",**off,width=1,height=1,command=close_root)
	b_enter_power=tk.Button(text="^",**g,width=1,height=1,command=lambda:simple_operator_click("**"))
	b_pi=tk.Button(text='π',**g,width=1,height=1,command=lambda:operator_click("pi"))
	b_par_r=tk.Button(text=")",**g,width=1,height=1,command=lambda: simple_operator_click(")"))
	b_par_l=tk.Button(text="(",**g,width=1,height=1,command=lambda: simple_operator_click("("))
	b_x=tk.Button(text="x",**g,width=1,height=1,command=lambda:operator_click("x"))
	b_add = tk.Button(text="+", **p,command=lambda: simple_operator_click("+"),width=1,height=1)
	b_subtraction = tk.Button(text="-", **p,command=lambda: simple_operator_click("-"),width=1,height=1)
	b_div = tk.Button(text="÷", **p, command=lambda: simple_operator_click("/"),width=1,height=1)
	b_multi = tk.Button(text="*", **p, command=lambda: simple_operator_click("*"),width=1,height=1)
	b_clear = tk.Button(text="c", **c, command=lambda: E1.delete(0, tk.END),width=1,height=1)
	b_eq = tk.Button(text="=", **e,width=1,height=1)
	b_point = tk.Button(text=".", **Color_Button
	,width=1,height=1,command=lambda: button_click("."))
	b_cosinos=tk.Button(text="cos",**g,width=1,height=1,command=lambda: operator_click("cos("))
	b_sinos=tk.Button(text="sin",**g,width=1,height=1,command=lambda: operator_click("sin("))
	b_neper=tk.Button(text="e",**g,width=1,height=1,command=lambda: operator_click("e"))
	b_log10=tk.Button(text="log",**g,width=1,height=1,command=lambda:operator_click("log10("))
	b_Accurate_draw=tk.Button(text="Accurate",**g,command=Accurate_draw)
	
	#Run_operator_Button
	b_OFF.grid(row=2,column=0,sticky="nsew")
	b_pi.grid(row=3,column=4,sticky="snew")
	b_div.grid(row=5, column=5,sticky="nsew")
	b_enter_power.grid(row=3,column=3,sticky="snew")
	b_par_l.grid(row=3, column=0,sticky="nsew")
	b_par_r.grid(row=3, column=1,sticky="nsew")
	b_x.grid(row=3, column=2,sticky="nsew")
	b_clear.grid(row=2, column=5,sticky="nsew",rowspan=2)
	b_add.grid(row=5, column=4,sticky="nsew")
	b_subtraction.grid(row=4, column=4,sticky="nsew")
	b_multi.grid(row=4, column=5,sticky="nsew")
	b_point.grid(row=6, column=2,sticky="nsew")
	b_cosinos.grid(row=2,column=2,sticky="snew")
	b_sinos.grid(row=2,column=1,sticky="snew")
	b_neper.grid(row=2,column=4,sticky="snew")
	b_log10.grid(row=2,column=3,sticky="snew")
	b_Accurate_draw.grid(row=6,column=3,sticky="nesw",columnspan=2)
	b_eq.bind('<Button-1>',draw_graph)
	b_eq.grid(row=6, column=5,sticky="nsew",columnspan=1)
	root.mainloop()
open_graph_calculator()