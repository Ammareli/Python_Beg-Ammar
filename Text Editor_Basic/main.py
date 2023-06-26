import os
from tkinter import *
from tkinter import filedialog,colorchooser,font
from tkinter.messagebox import *
from tkinter.filedialog import *

DEFAULT_FONT = "Arial"

DEFAULT_FONT_SIZE = "16"

LABEL_COLOR = "#FFFAFA"



class TextEditor:
    def __init__(self) -> None:

        self.window = Tk()
        self.window.title("Text Editor")

        self.window_width,self.window_height,self.x,self.y=self.center_window()
        self.window.geometry(f"{self.window_width}x{self.window_height}+{self.x}+{self.y}")

        self.font_name,self.font_size =self.default_font()
        
        self.text_area=self.text_edititor(self.font_name.get(),self.font_size.get())
        self.create_scroll_bar()

        self.window.grid_rowconfigure(0,weight=1)
        self.window.grid_columnconfigure(0,weight=1)

        self.button_frame = self.create_buttons_frame()
        self.color_button=self.create_color_buttons()
        self.create_font_menu()
        self.size_box=self.create_size_menu()
        self.menu_bar=self.create_menu_bar()
        self.create_file_menu()
        self.create_edit_menu()
        self.create_help_menu()


    def center_window(self):
        window_width = 1024
        window_height = 600
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = int(screen_width/2 - window_width/2)
        y = int(screen_height/2 - window_height/2)

        return window_width,window_height,x,y

    def default_font(self):

        self.font_name = StringVar(self.window)
        self.font_name.set(DEFAULT_FONT)
        
        self.font_size = StringVar(self.window)
        self.font_size.set(DEFAULT_FONT_SIZE)
        
        
       

        return self.font_name,self.font_size
        

    def text_edititor(self,name,size):
        text = Text(self.window,font=(name,size))
        text.grid(row=0,column=0,sticky=NSEW)
        return text
    def create_scroll_bar(self):
        scroll_bar = Scrollbar(self.text_area)
        scroll_bar.pack(side=RIGHT,fill=Y)
        self.text_area.config(yscrollcommand=scroll_bar.set)
        
    def create_buttons_frame(self):
        frame = Frame(self.window,bg=LABEL_COLOR,height=50,borderwidth=2,highlightbackground="#778899")
        frame.grid()
        return frame
    
    def color(self):
        color = colorchooser.askcolor()
        self.text_area.config(fg=color[1])
        self.color_button.config(bg=color[1])
        
    
    def change_font(self,font):
        self.font_name.set(font)
        
        self.text_area.config(font=(font,int(self.font_size.get())))
    
    def change_font_size(self):
        self.text_area.config(font=(self.font_name,int(self.size_box.get())))

    def create_color_buttons(self):
        color_button = Button(self.button_frame,text="Color",font=(DEFAULT_FONT,14),borderwidth=0,padx=21,command=self.color)
        color_button.grid(row=0,column=0,sticky=NSEW)
        return color_button
    def create_font_menu(self):
        font_select = OptionMenu(self.button_frame,self.font_name,*font.families(),command=self.change_font)
        font_select.grid(row=0,column=1,sticky=NSEW)
    def create_size_menu(self):
        size_box = Spinbox(self.button_frame,from_=1,to=100,textvariable=self.font_size,command=self.change_font_size,insertbackground=LABEL_COLOR)
        size_box.grid(row=0,column=2,sticky=NSEW)
        return size_box
    

    def create_menu_bar(self):
        menu = Menu(self.window)
        self.window.config(menu=menu)
        return menu
    
    def create_file_menu(self):
        file_menu = Menu(self.menu_bar,tearoff=0)
        self.menu_bar.add_cascade(label="File",menu=file_menu)
        file_menu.add_command(label="New",command=self.new)
        file_menu.add_command(label="Open",command=self.open)
        file_menu.add_command(label="Save",command=self.save)
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=quit)


    def create_edit_menu(self):
        edit_menu = Menu(self.menu_bar,tearoff=0)
        self.menu_bar.add_cascade(label="Edit",menu=edit_menu)
        edit_menu.add_command(label="Cut",command=self.cut)
        edit_menu.add_command(label="Copy",command=self.copy)
        edit_menu.add_command(label="Paste",command=self.paste)

    def create_help_menu(self):
        help_menu = Menu(self.menu_bar,tearoff=0)
        self.menu_bar.add_cascade(label="Help",menu=help_menu)
        help_menu.add_command(label="About",command=self.about)

    def new(self):
        self.window.title('Untitled.')
        self.text_area.delete(1.0,END)

    def open(self):
        file = askopenfilename(defaultextension=".txt",file=
                               [("All Files","*.*"),
                                ("Txt Files","*.txt")])
        
        try:
            self.window.title(os.path.basename(file))

            file = open(file,"r")

            self.text_area.delete(1.0,END)
            data = file.read() 
            self.text_area.insert(1.0,data)
            
        except Exception as e:
            showerror("Error",f"Cannot Open File\n:{e}")

        finally:
            file.close()
        

    def save(self):
        file = asksaveasfilename(defaultextension=".txt",initialfile="Untitled.txt",filetypes=[("All Files","*.*"),
                                                                                               ("Text Files","*.txt")])
        
        if file is NONE:
            return
        else:
            try:
                self.window.title(f"{os.path.basename(file)}-Text Editor")
                file = open(file,"w")
                file.write(self.text_area.get(1.0,END))


            except Exception as e:
                showerror('Error',f"Cannot Save File\n :{e}")
            finally:
                file.close()
               
    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def about(self):
        message = """
                Text Editor Programme.
                This Programe is wrriten in python using Basic GUI.
                For more help mail.
                mail@gmail.com
        
        """
        showinfo("About",message)
        
    def run(self):
        self.window.mainloop()



if __name__ == "__main__":
    text_edit = TextEditor()
    text_edit.run()
