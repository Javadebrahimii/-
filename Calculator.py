import tkinter as tk
import tkinter.ttk as ttk
import math




def open_calculator():
     

    color_Number= {'bd': 5, 'fg': '#000', 'bg': '#ccffcc','font': ('sans-serif', 17, 'bold')}

    g = {'bd': 5, 'fg': '#000', 'bg': '#ffe6ff', 'font': ('sans-serif', 17, 'bold')}

    c={'bd': 5, 'fg': '#000', 'bg': '#FF5C33', 'font': ('sans-serif', 16, 'bold')}

    e = {'bd': 5, 'fg': '#000', 'bg': '#5CD65C', 'font': ('sans-serif', 16, 'bold')}

    p= {'bd': 5, 'fg': '#000', 'bg': '#b3ffff', 'font': ('sans-serif', 16, 'bold')}

    off={'bd': 5, 'fg': '#000', 'bg': '#ff8080', 'font': ('sans-serif', 16, 'bold')}

    width=1
    height=1

    

    def button_click(number):
        current_text = E1.get()
        E1.delete(0, tk.END)
        E1.insert(tk.END, current_text + number)

    def close_window():
        window.destroy()

    def equals():
        x = E1.get()
        equal = eval(x)
        E1.delete(0, tk.END)
        E1.insert(tk.END, equal)

    def equal_pi():
            pi=3.14159
            E1.delete(0,tk.END)
            E1.insert(tk.END, pi)
            
    def equal_fact():
        x = E1.get()
        y="fact"+"("+x+")"+"="
        resultt = str(math.factorial(int(x)))
        E1.delete(0, tk.END)
        E1.insert(tk.END,y+resultt)

    def equal_neper():
        e=2.71828
        E1.delete(0,tk.END)
        E1.insert(tk.END,e)

    def equal_sin():
        x = E1.get()
        y="sin("+x+")"+"="
        result = str(math.sin(math.radians(int(x))))
        E1.delete(0, tk.END)
        E1.insert(tk.END,y+ result[:8])

    def equal_cos():
        x = E1.get()
        y="cos("+x+")"+"="
        result = str(math.cos(math.radians(int(x))))
        E1.delete(0, tk.END)
        E1.insert(tk.END, y+result[:8])

    def equal_tan():
        x = E1.get()
        y="tan("+x+")"+"="
        result = str(math.tan(math.radians(int(x))))
        E1.delete(0, tk.END)
        E1.insert(tk.END,y+ result[:8])

    def equal_cot():
        x = E1.get()
        y="cot("+x+")"+"="
        result = str(1 / math.tan(math.radians(int(x))))
        E1.delete(0, tk.END)
        E1.insert(tk.END,y+ result[:8])

    def equal_log():
        x = E1.get()
        y="log("+x+")"+"="
        result = str(math.log(int(x)))
        E1.delete(0, tk.END)
        E1.insert(tk.END, y+result[:7])

    def square_root():
        x = E1.get()
        y='\u00B2\u221A'+x+"="
        result = str(eval(x+'**(1/2)'))
        E1.delete(0, tk.END)
        E1.insert(tk.END, y+result[:7])

    def  third_root3():
    	x=E1.get()
    	y='\u00B3\u221A'+x+"="
    	result = str(eval(x+'**(1/3)'))
    	E1.delete(0,tk.END)
    	E1.insert(tk.END, y+result[:7])
	
	
	
	
    #window
    window = tk.Tk()
    window.configure(bg="#293C4A", bd=10)
    window.title("Calculator")
    window.geometry("490x580")



    # Entry

    E1 = tk.Entry( font=('sans-serif', 30, 'bold'), bd=9, bg='#BBB')
    E1.grid(row=0,column=0,columnspan=5, padx=5, pady=5, sticky="snew")

    # number_Buttons
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
    b1.grid(row=8, column=0,sticky="nsew")
    b2.grid(row=8, column=1,sticky="nsew")
    b3.grid(row=8, column=2,sticky="nsew")
    b4.grid(row=7, column=0,sticky="nsew")
    b5.grid(row=7, column=1,sticky="nsew")
    b6.grid(row=7, column=2,sticky="nsew")
    b7.grid(row=6, column=0,sticky="nsew")
    b8.grid(row=6, column=1,sticky="nsew")
    b9.grid(row=6, column=2,sticky="nsew")
    b0.grid(row=9, column=0,columnspan=2,sticky="nsew")


#operator_Button

    b_OFF=tk.Button(text="OFF",**off,width=width,height=height,command=close_window)
    b_mod=tk.Button(text="mod",**g,command=lambda:button_click("%"),width=width,height=height)
    b_divint=tk.Button(text="div",**g,command=lambda:button_click("//"),width=width,height=height)
    b_fact=tk.Button(text="x!",**g,command=equal_fact,width=width,height=height)
    b_neper=tk.Button(text="e",**g,command=equal_neper,width=width,height=height)

    b_revers= tk.Button(text='x\u207b\xb9',**g,command=lambda:button_click("**(-1)"),width=width,height=height)
    b_second_power=tk.Button(text="x\u00B2",**g,width=width,height=height,command=lambda:button_click("**2"))
    b_third_power=tk.Button(text="x\u00B3",**g,width=width,height=height,command=lambda:button_click("**3"))
    b_enter_power=tk.Button(text="x^n",**g,width=width,height=height,command=lambda:button_click("**"))

    b_square_root = tk.Button(text='\u00B2\u221A',**g,width=width,height=height,command=square_root)
    b_third_root=tk.Button(text='\u00B3\u221A',**g,width=width,height=height,command=third_root3)
    b_pi=tk.Button(text='π',**g,width=width,height=height,command=equal_pi)
    b_ten_power=tk.Button(text="10^n",**g,command=lambda:button_click('10**'),width=width,height=height)

    b_log_base10 = tk.Button( text='log\u2081\u2080',**g,command=equal_log,width=width,height=height)
    b_par_r=tk.Button(text=")",**g,width=width,height=height)
    b_par_l=tk.Button(text="(",**g,width=width,height=height)
    b_add = tk.Button(text="+", **p,command=lambda: button_click("+"),width=width,height=height)
    b_subtraction = tk.Button(text="-", **p,command=lambda: button_click("-"),width=width,height=height)
    b_div = tk.Button(text="÷", **p, command=lambda: button_click("/"),width=width,height=height)
    b_multi = tk.Button(text="*", **p, command=lambda: button_click("*"),width=width,height=height)
    b_clear = tk.Button(text="c", **c, command=lambda: E1.delete(0, tk.END),width=width,height=height)
    b_eq = tk.Button(text="=", **e, command=equals,width=width,height=height)
    b_point = tk.Button(text=".", **color_Number, command=lambda: button_click("."),width=width)
    b_cosinos=tk.Button(text="cos",**g,command=equal_cos,width=width)
    b_sinos=tk.Button(text="sin",**g,command=equal_sin,width=width,height=height)
    b_tan=tk.Button(text="tan",**g,command=equal_tan,width=width,height=height)
    b_cot=tk.Button(text="cot",**g,command=equal_cot,width=width,height=height)

#Run_operator_Button
    b_OFF.grid(row=1,column=0,sticky="nsew")
    b_mod.grid(row=1,column=1,sticky="nsew")
    b_divint.grid(row=1,column=2,sticky="nsew")
    b_pi.grid(row=5,column=2,sticky="snew")
    b_neper.grid(row=5,column=3,sticky="nsew")
    b_div.grid(row=2, column=4,sticky="nsew")
    b_revers.grid(row=3, column=0,sticky="nsew")
    b_second_power.grid(row=3,column=1,sticky="nsew")
    b_third_power.grid(row=3,column=2,sticky="snew")
    b_enter_power.grid(row=3,column=3,sticky="snew")
    b_square_root.grid(row=4, column=0,sticky="nsew")
    b_third_root.grid(row=4,column=1,sticky="snew")
    b_fact.grid(row=4,column=2,sticky="nsew")
    b_ten_power.grid(row=4,column=3,sticky="snew")
    b_par_l.grid(row=5, column=0,sticky="nsew")
    b_par_r.grid(row=5, column=1,sticky="nsew")
    b_log_base10.grid(row=1, column=3,sticky="nsew")
    b_clear.grid(row=1, column=4,sticky="nsew")
    b_eq.grid(row=6, column=3,rowspan=10,sticky="nsew")
    b_add.grid(row=4, column=4,rowspan=10,sticky="nsew")
    b_subtraction.grid(row=4, column=4,sticky="nsew")
    b_multi.grid(row=3, column=4,sticky="nsew")
    b_point.grid(row=9, column=2,sticky="nsew")
    b_cosinos.grid(row=2,column=1,sticky="snew")
    b_sinos.grid(row=2,column=0,sticky="snew")
    b_tan.grid(row=2,column=2,sticky="snew")
    b_cot.grid(row=2,column=3,sticky="snew")




    #Runapp
    window.mainloop()
open_calculator()