import tkinter as tk

SMALL_FONT_STYLE = ("Arial",16)
LARGE_FONT_STYLE = ("Arial",30,"bold")
DIGIT_FONT_STYLE = ("Agency FB",24,"bold")
DEFAULT_FONT_STYLE = ("Arial",20)


LIGHT_GREY = "#F5F5F5"
LABEL_COLOR = "#25265E"
WHITE = "#FFFFFF"
OFF_WHITE = "#F8FAFF"
CORN_FLOWER_BLUE = "#6495ED"

class Calculator:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.current_expression = ""
        self.total_expression = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_dispaly_label()

        self.digits = {
            "7":(1,0), "8":(1,1), "9":(1,2),
            "4":(2,0), "5":(2,1), "6":(2,2),
            "1":(3,0), "2":(3,1), "3":(3,2),
            "0":(4,0), ".":(4,1)

        }  

        self.operations = {"/":"\u00F7","*":"\u00D7","-":"-","+":"+"}  
        


        self.buttons_frame = self.create_buttons_frame()
        self.create_buttons()
        self.create_operators_buttons()
        self.create_special_buttons()
        
        self.buttons_frame.rowconfigure(0,weight=1)
        self.buttons_frame.rowconfigure(0,weight=1)
        
        self.buttons_frame.rowconfigure(1,weight=1)
        self.buttons_frame.columnconfigure(1,weight=1)

        self.buttons_frame.rowconfigure(2,weight=1)
        self.buttons_frame.columnconfigure(2,weight=1)
        
        self.buttons_frame.rowconfigure(3,weight=1)
        self.buttons_frame.columnconfigure(3,weight=1)

        self.buttons_frame.rowconfigure(4,weight=1)

        self.bind_keys()

        

        
        


    def create_special_buttons(self):
        self.clear_button()
        self.equal_button()
        self.squre_button()
        self.sqrt_button()

    def squre_button(self):
        button = tk.Button(self.buttons_frame,text="x\u00b2",borderwidth=0,bg=OFF_WHITE,fg=LABEL_COLOR,font=DEFAULT_FONT_STYLE,command=self.squre)
        button.grid(row=0,column=1,sticky=tk.NSEW)

    def squre(self):
        try:
            self.current_expression = str(eval(f"{self.current_expression}**2"))
        except SyntaxError:
            self.current_expression = "Syntax Error"
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def sqrt_button(self):
        button = tk.Button(self.buttons_frame,text="\u221ax",borderwidth=0,bg=OFF_WHITE,fg=LABEL_COLOR,font=DEFAULT_FONT_STYLE,command=self.sqrt)
        button.grid(row=0,column=2,sticky=tk.NSEW)

    def sqrt(self):
        try:
            self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        except SyntaxError:
            self.current_expression = "Syntax Error"
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def evalulate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except ZeroDivisionError :
            self.current_expression = "Can't Divide 0"
        except SyntaxError:
            self.current_expression = "Syntax Error"
        except Exception as e :
            self.current_expression = "Error"
            
        finally:
            self.update_label()


    def create_dispaly_label(self):
        total_label = tk.Label(self.display_frame,text=self.total_expression,anchor=tk.E,font=SMALL_FONT_STYLE,bg=LIGHT_GREY,fg=LABEL_COLOR,padx=24)
        total_label.pack(expand=True,fill="both")

        label = tk.Label(self.display_frame,text=self.current_expression,anchor=tk.E,font=LARGE_FONT_STYLE,bg=LIGHT_GREY,fg=LABEL_COLOR,padx=24)
        label.pack(expand=True,fill="both")

        return total_label,label

    def create_display_frame(self):
        frame = tk.Frame(self.window,bg=LIGHT_GREY)
        frame.pack(expand=True,fill="both")
        return frame
    
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def add_to_expression(self,value):
        self.current_expression += str(value)
        self.update_label()

    def create_buttons(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame,text=digit,bg=WHITE,fg=LABEL_COLOR,font=DIGIT_FONT_STYLE,borderwidth=0,command=lambda x=digit:self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1],sticky=tk.NSEW)

    def create_operators_buttons(self):
        i=0
        for operator,sym in self.operations.items():
            button = tk.Button(self.buttons_frame,text=sym,borderwidth=0,bg=OFF_WHITE,fg=LABEL_COLOR,font=DEFAULT_FONT_STYLE,command=lambda x=operator : self.append_operator(x))
            button.grid(row=i,column=3,sticky=tk.NSEW)
            i+=1
    def clear_button(self):
        button = tk.Button(self.buttons_frame,text="C",borderwidth=0,bg=OFF_WHITE,fg=LABEL_COLOR,font=DEFAULT_FONT_STYLE,command=self.clear)
        button.grid(row=0,column=0,sticky=tk.NSEW)

    def equal_button(self):
        button = tk.Button(self.buttons_frame,text="=",borderwidth=0,bg=CORN_FLOWER_BLUE,fg=LABEL_COLOR,font=DEFAULT_FONT_STYLE,command=self.evalulate)
        button.grid(row=4,column=2,columnspan=2,sticky=tk.NSEW)

    

    def create_buttons_frame(self):
        frame= tk.Frame(self.window)
        frame.pack(expand=True,fill="both")
        return frame
    def update_total_label(self):
        expression = self.total_expression
        for operator,sym in self.operations.items():
            expression = expression.replace(operator,f' {sym} ')
        self.total_label.config(text=expression)
    
    def update_label(self):
        self.label.config(text=self.current_expression[:14])
    
    def bind_keys(self):
        self.window.bind("<Return>",lambda event:self.evalulate())
        self.window.bind("<Delete>",lambda event:self.clear())

        for key in self.digits:
            self.window.bind(str(key),lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.window.bind(key, lambda event , operator = key: self.append_operator(operator))
   

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()