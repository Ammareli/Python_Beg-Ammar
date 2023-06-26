from tkinter import *
import random

LARGE_FONT = ("Arial",30)

BACK_GROUND = "#2F4F4F"
FONT_COLOR = "#F0F0F0"


STALE_GREY = "#708090"
DARK_BLUE = "#00008B"
INDEGO = "#4B0082"
WHITE = "#FFFFF0"
ALICE_BLUE = "#F0F8FF"
BRIGHT_RED = "#DC143C"


class TicTacGame:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.resizable(0,0)
        
        self.players = ["X","0"]
        self.player = random.choice(self.players)
        self.buttons = [[0,0,0],
                        [0,0,0],
                        [0,0,0]]
        self.turn_label = self.create_turn_label()
        self.create_reset_button()
        self.buttons_frame = self.create_buttons_frame()
        
        
        self.game_buttons = self.create_game_buttons()
        self.buttons_frame.rowconfigure(0,weight=1)
        self.buttons_frame.columnconfigure(0,weight=1)
        self.buttons_frame.rowconfigure(1,weight=0)
        self.buttons_frame.columnconfigure(1,weight=1)
        self.buttons_frame.rowconfigure(2,weight=1)
        self.buttons_frame.columnconfigure(2,weight=1)
        




#_______________________________________METHODS______________________________________________
    
    
    def create_turn_label(self):
        label = Label(self.window,text=f"{self.player} Turn",font=LARGE_FONT,bg=WHITE,fg=INDEGO)
        label.pack(side=TOP)

        return label
    def create_reset_button(self):
        button = Button(self.window,text="RESET",font=("Consolas",20),borderwidth=0,command=self.new_game)
        button.pack(side=TOP)

    def create_buttons_frame(self):
        frame = Frame(self.window)
        frame.pack(expand=True,fill=BOTH)
        return frame
    
    def create_game_buttons(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column] = Button(self.buttons_frame,text="",bg=STALE_GREY,fg=WHITE,font=LARGE_FONT,activebackground=ALICE_BLUE,activeforeground=DARK_BLUE,command=lambda row=row,column = column: self.next_turn(row,column),width=5,height=3)
                self.buttons[row][column].grid(row=row,column=column,sticky=NSEW)
            
        return self.buttons

            
        
    def next_turn(self,row,column):
        if (self.game_buttons[row][column]["text"] == "") and (self.cheak_winner() is False):
            if self.player == self.players[0]:
                self.game_buttons[row][column]["text"] = self.players[0]
                if self.cheak_winner() is False:
                    self.player = self.players[1]
                    self.turn_label.config(text=f"{self.player} Turn")
                elif self.cheak_winner() is True:
                    self.turn_label.config(text=f"{self.players[0]} Wins")
                elif self.cheak_winner() == "tie":
                    self.turn_label.config(text=f"Tie")
            else:
                
                self.game_buttons[row][column]["text"] = self.players[1]
                if self.cheak_winner() is False:
                    self.player = self.players[0]
                    self.turn_label.config(text=f"{self.player} Turn")
                elif self.cheak_winner() is True:
                    self.turn_label.config(text=f"{self.players[1]} Wins")
                elif self.cheak_winner() == "tie":
                    self.turn_label.config(text=f"Tie")


    def cheak_winner(self):
        for row in range(3):
            if self.game_buttons[row][0]["text"] == self.game_buttons[row][1]["text"] == self.game_buttons[row][2]["text"] != "":
                self.game_buttons[row][0].config(bg=BACK_GROUND,fg=FONT_COLOR)
                self.game_buttons[row][1].config(bg=BACK_GROUND,fg=FONT_COLOR)
                self.game_buttons[row][2].config(bg=BACK_GROUND,fg=FONT_COLOR)
                return True
            

        for column in range(3):
            if self.game_buttons[0][column]["text"] == self.game_buttons[1][column]["text"] == self.game_buttons[2][column]["text"] != "":
                self.game_buttons[0][column].config(bg=BACK_GROUND,fg=FONT_COLOR)
                self.game_buttons[1][column].config(bg=BACK_GROUND,fg=FONT_COLOR)
                self.game_buttons[2][column].config(bg=BACK_GROUND,fg=FONT_COLOR)
                return True
        
        if self.game_buttons[0][0]["text"] == self.game_buttons[1][1]["text"] == self.game_buttons[2][2]["text"] != "":
            self.game_buttons[0][0].config(bg=BACK_GROUND,fg=FONT_COLOR)
            self.game_buttons[1][1].config(bg=BACK_GROUND,fg=FONT_COLOR)
            self.game_buttons[2][2].config(bg=BACK_GROUND,fg=FONT_COLOR)
            return True
        elif self.game_buttons[0][2]["text"] == self.game_buttons[1][1]["text"] == self.game_buttons[2][0]["text"] != "":
            self.game_buttons[0][2].config(bg=BACK_GROUND,fg=FONT_COLOR)
            self.game_buttons[1][1].config(bg=BACK_GROUND,fg=FONT_COLOR)
            self.game_buttons[2][0].config(bg=BACK_GROUND,fg=FONT_COLOR)
            return True
        elif self.empty_spaces() is False:
            for row in range(3):
                for column in range(3):
                    self.game_buttons[row][column].config(bg=BRIGHT_RED,fg=FONT_COLOR)

            return "tie" 
        else:
            return False
    
    def empty_spaces(self):
        spaces = 9
        for row in range(3):
            for column in range(3):
                if self.game_buttons[row][column]["text"] != "":
                    spaces = spaces - 1
        
        if spaces == 0:
            return False
        else:
            return True
        

    def new_game(self):
        self.palyer = random.choice(self.players)

        self.turn_label.config(text=f"{self.player} Turn")

        for row in range(3):
            for column in range(3):
                self.game_buttons[row][column].config(text = "", bg=STALE_GREY)

    def run(self):
        self.window.mainloop()



if __name__ == "__main__":
    game = TicTacGame()
    game.run()


