from tkinter import *
from time import *

BACK_GROUND = "#2F4F4F"
FONT_COLOR = "#F0F0F0"

def update():
    time_str = strftime("%H:%M:%S")
    time_label.config(text=time_str)

    day = strftime("%A")
    month = strftime("%B")
    day_number = strftime("%d")
    year = strftime("%Y")
   

    Day_date = f"{day}| {month} {day_number},{year}"
    label_Date_Day.config(text=Day_date)

    window.after(1000,update)

window = Tk()
window.title("Time Clock")
window.geometry("300x100")
window.resizable(0,0)
window.config(bg=BACK_GROUND)




time_label = Label(window,bg=BACK_GROUND,fg = FONT_COLOR, font=("Agency FB",36))
time_label.pack(fill="both" ,expand=True)

label_Date_Day = Label(window,bg=BACK_GROUND,fg="Black",font=("Bahnschrift Condensed",14))
label_Date_Day.pack(fill="both",expand=TRUE)





update()

window.mainloop()
