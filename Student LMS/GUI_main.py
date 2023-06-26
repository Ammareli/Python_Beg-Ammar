from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.messagebox import *
import pymongo as py
import pandas as pd
client = py.MongoClient("mongodb://localhost:27017")
db_1 = client["DemoStudents"]
collection = db_1["DemoStudentsData"]

BACKGROUNDCOLOUR = "#E0E0E0"

class StudentsLms:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.geometry("1000x600")
        self.window.config(background=BACKGROUNDCOLOUR)


        self.create_header_label()
        self.input_frm,self.output_frm = self.create_frames()
        self.tab_add_s,self.tab_search_s,self.tab_del_s = self.create_note_book()
        self.data = list(self.create_student_entry_form())
        self.create_submit_button()
        self.output_area=self.create_output_area()
        self.message_label=self.create_message_label()
        self.search_data=self.create_search_area()
        self.create_search_button()
        self.search_messgae=self.create_search_message_label()
        self.del_data = self.create_delete_form()
        self.create_delete_button()
        self.delete_message = self.create_delete_message_label()
        self.create_showall_students_button()
        self.create_clear_button()
        self.menu_bar=self.create_menu_bar()
        self.create_file_menu()


    def create_frames(self):
        frm_1 = ttk.Frame(self.window,padding=10,border=10)
        frm_1.pack(expand=True,fill="both")

        frm_2 = ttk.Frame(self.window,padding=10,border=10)
        frm_2.pack(expand=True,fill="both")

        return frm_1,frm_2
    
    def create_note_book(self):
        notebook = ttk.Notebook(self.input_frm)
        tab_1 = ttk.Frame(notebook)
        tab_2 = ttk.Frame(notebook)
        tab_3 = ttk.Frame(notebook)
        notebook.add(tab_1,text="Add Sudents")
        notebook.add(tab_2,text="Search")
        notebook.add(tab_3,text="Delete Students")

    
        notebook.pack(expand=True,fill="both")
        return tab_1,tab_2,tab_3
    
    def create_header_label(self):
        ttk.Label(self.window,text='LMS',font=("Arial",20),background="#FFFFFF").pack(expand=True,fill="both")

    def create_student_entry_form(self):
        self.label = {
            "Name":(0,0),
            "Father Name":(1,0),
            "Adress":(2,0),
            "Contact":(3,0)
                      }
        
        
        
        for value,grid_value in self.label.items():
            ttk.Label(self.tab_add_s,text=value,padding=10).grid(row=grid_value[0],column=grid_value[1])
            
        name = StringVar(self.tab_add_s)
        f_name = StringVar(self.tab_add_s)
        adress = StringVar(self.tab_add_s)
        contact = StringVar(self.tab_add_s)

        e1=ttk.Entry(self.tab_add_s,textvariable=name)
        e1.grid(row=0,column=1)
        e2=ttk.Entry(self.tab_add_s,textvariable=f_name)
        e2.grid(row=1,column=1)
        e3=ttk.Entry(self.tab_add_s,textvariable=adress)
        e3.grid(row=2,column=1)
        e4=ttk.Entry(self.tab_add_s,textvariable=contact)
        e4.grid(row=3,column=1)
        

        return name,f_name,adress,contact,e1,e2,e3,e4

    def create_submit_button(self):
        style = ttk.Style()
        style.map("C.TButton",
        foreground=[('pressed', 'red'), ('active', 'blue')],
        background=[('pressed', '!disabled', 'black'), ('active', 'white')]
        )
        
        ttk.Button(self.tab_add_s,text="Submit",style="C.TButton",command=self.submit).grid(row=4,column=0,columnspan=2)      


    def submit(self):
        global name 
        global f_name
        global adress
        global contact
        global message
        global command
        if self.data[0].get() != "" and self.data[0].get().isalpha():
            global name
            name= self.data[0].get().lower()
            command = True
        else:
            inval_name= self.data[0].get()
            message = f"Invalid Name\n Please Enter a Valid Name\n{inval_name} invalid Entry" 
            self.update_message_label(message)
            command = False
            self.clear()
        if self.data[1].get() != "" and self.data[1].get().isalpha():
            global f_name
            f_name = self.data[1].get().lower()
            command = True
        else:
            inval_f_name = self.data[1].get()
            message = f"Invalid Name\n Please Enter a Valid Father Name\n{inval_f_name} invalid Entry" 
            self.update_message_label(message)
            command = False
            self.clear()
        if self.data[2].get() != "":
            global adress
            adress = self.data[2].get().lower()
            command = True
        else:
            inval_adress = self.data[2].get()
            message = f"Invalid Adress\n Please Enter a Valid Name\n{inval_adress} invalid Entry" 
            self.update_message_label(message)
            command = False
            self.clear()
        if self.data[3].get() != ""and self.data[3].get().isnumeric():
            global contact
            contact = self.data[3].get()
            command = True
        else:
            inval_contact = self.data[3].get()
            message = f"Invalid contact\n Please Enter a Valid Name\n{inval_contact} invalid Entry" 
            self.update_message_label(message)
            command = False
            self.clear()
        
        if command:
            student = {"name":name,"father_name":f_name,"Adress":adress,"contact":contact}
            collection.insert_one(student)

            message = f"Name: {name}\nFather Name: {f_name}\nAdress: {adress}\nContact: {contact}\n Student Added"
            self.update_message_label(message)
            self.clear()

        
    def clear(self):
        for i in range(4,len(self.data)):
            self.data[i].delete(0,END)
        
    


    def create_output_area(self):
        ttk.Style().configure("Scolled Style")
        output_area = scrolledtext.ScrolledText(self.output_frm,spacing1=5,font = ("Arial",18))
        output_area.pack(expand=True)
        
        return output_area

    def create_clear_button(self):
        style = ttk.Style()
        style.map("C.TButton",
        foreground=[('pressed', 'red'), ('active', 'blue')],
        background=[('pressed', '!disabled', 'black'), ('active', 'white')]
        )
        
        button = ttk.Button(self.input_frm,text="Clear",state="C.TButton",command=self.clear_output_area,width=10)
        button.pack()
    def create_showall_students_button(self):
        style = ttk.Style()
        style.map("C.TButton",
        foreground=[('pressed', 'red'), ('active', 'blue')],
        background=[('pressed', '!disabled', 'black'), ('active', 'white')]
        )
        
        button = ttk.Button(self.input_frm,text="SHOW ALL",style="C.TButton",command=self.showall,width=30)
        button.pack()
    def showall(self):
        data=collection.find({},{"_id":0})
        df = pd.DataFrame(data)
        self.update_output_label(df)


    def clear_output_area(self):
        self.output_area.delete(1.0,END)
        
    def create_message_label(self):
        message = "DATA"
        
        message_l = ttk.Label(self.tab_add_s,text=message,padding=30,justify="left")  
        message_l.place(x=500,y=5)
        return message_l
    

    def update_message_label(self,message):
       self.message_label.config(text=message)
        
    def create_search_area(self):
        ttk.Label(self.tab_search_s,text="Name: ",font=("Arial",16,),padding=20).grid(row=0,column=0)

        ttk.Label(self.tab_search_s,text="Father Name: ",font=("Arial",16,),padding=20).grid(row=1,column=0)


        name_e = ttk.Entry(self.tab_search_s,width=20)
        name_e.grid(row=0,column=1,columnspan=2)

        f_name_e = ttk.Entry(self.tab_search_s,width=20)
        f_name_e.grid(row=1,column=1,columnspan=2)

        return name_e , f_name_e

        return search_e
    def create_search_button(self):
        style = ttk.Style()
        style.map("C.TButton",
        foreground=[('pressed', 'purple'), ('active', 'blue')],
        background=[('pressed', '!disabled', 'black'), ('active', 'white')]
        )
        
        ttk.Button(self.tab_search_s,text="Search",style="C.TButton",command=self.search).grid(row=2,column=1,columnspan=2)
        
    def search(self):
        global message
        name=self.search_data[0].get().lower()
        f_name = self.search_data[1].get().lower()
        global command
        if name != "" and name.isalpha():
            
            command = True
        else:
            message = f"Invalid name\n{name}"
            self.search_data[0].delete(0,END)
            self.search_data[1].delete(0,END)
            command = False
        if f_name != "" and f_name.isalpha():
            
            command = True

        else:
            message = f"Invalid name\n{name}"
            command = False
            self.search_data[0].delete(0,END)
            self.search_data[1].delete(0,END)
        
        if command:
            search = collection.find_one({"name":name,"father_name":f_name},{"_id":0})
            if search == None:
                message = "No student Found......"
                self.update_search_message_label(message)
                self.search_data[0].delete(0,END)
                self.search_data[1].delete(0,END)
            else:
                
                df=pd.DataFrame(search,index=["student"])
                self.update_output_label(df)
                self.search_data[0].delete(0,END)
                self.search_data[1].delete(0,END)

    def update_output_label(self,df):
        self.output_area.delete(1.0,END)
        self.output_area.insert(1.0,df)
    
    def create_search_message_label(self):
        message = "DATA"
        
        message_l = ttk.Label(self.tab_search_s,text=message,padding=30,justify="left")  
        message_l.place(x=500,y=5)
        return message_l

    def update_search_message_label(self,msg):
        self.search_messgae.config(text=message)

    def create_delete_form(self):
        ttk.Label(self.tab_del_s,text="Name: ",font=("Arial",16,),padding=20).grid(row=0,column=0)

        ttk.Label(self.tab_del_s,text="Father Name: ",font=("Arial",16,),padding=20).grid(row=1,column=0)


        name_e = ttk.Entry(self.tab_del_s,width=20)
        name_e.grid(row=0,column=1,columnspan=2)

        f_name_e = ttk.Entry(self.tab_del_s,width=20)
        f_name_e.grid(row=1,column=1,columnspan=2)

        return name_e , f_name_e
    
    def create_delete_button(self):
        style = ttk.Style()
        style.map("C.TButton",
        foreground=[('pressed', 'red'), ('active', 'blue')],
        background=[('pressed', '!disabled', 'black'), ('active', 'white')]
        )
        
        ttk.Button(self.tab_del_s,text="Delete",style="C.TButton",command=self.delete).grid(row=2,column=1,columnspan=2)
    def delete(self):
        name = self.del_data[0].get().lower()
        f_name = self.del_data[1].get().lower()
        global command

        if name != "" and name.isalpha():
            command=True
        else:
            message = f"Invalid name\n{name}"
            self.update_delete_message_label(message)
            command = False
            self.del_data[0].delete(0,END)
            self.del_data[1].delete(0,END)
        if f_name != "" and f_name.isalpha():
            command=True
        else:
            message = f"Invalid name{name}"
            self.update_delete_message_label(message)
            command = False
            self.del_data[0].delete(0,END)
            self.del_data[1].delete(0,END)
        if command:
            search = collection.find_one({"name":name,"father_name":f_name})
            if search == None:
                message = f"Student Not Found\n{name}\n{f_name}"
                self.update_delete_message_label(message)
                self.del_data[0].delete(0,END)
                self.del_data[1].delete(0,END)
            else:

                collection.delete_one({"name":name,"father_name":f_name})
                message = f"Name: {name}\nFather Name: {f_name}\nDeleted Sucessfully"
                self.update_delete_message_label(message)
                self.del_data[0].delete(0,END)
                self.del_data[1].delete(0,END)

    def create_delete_message_label(self):
        message = "DATA"
        
        message_l = ttk.Label(self.tab_del_s,text=message,padding=30,justify="left")  
        message_l.place(x=500,y=5)
        return message_l      

    def update_delete_message_label(self,msg):
        self.delete_message.config(text=msg)


    def create_menu_bar(self):
        menu = Menu(self.window,background="yellow")
        self.window.config(menu= menu)

        return menu
    
    def create_file_menu(self):
        file_menu = Menu(self.menu_bar,tearoff=0)
        self.menu_bar.add_cascade(label="file",menu=file_menu)
        file_menu.add_command(label="Add Student")
        file_menu.add_command(label="Delete Student")
        file_menu.add_command(label="Search Student")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command = quit)
        


    def run(self):
        self.window.mainloop()



if __name__ == "__main__":
    lms = StudentsLms()
    lms.run()