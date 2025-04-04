from tkinter import*
gui = Tk()

gui.title("Rock Paper Scissors")

player_score = 0
computer_score = 0
options = ["rock","paper","scissors"]
def player_wins():
    global player_score
    player_score +=1
    player_score_lable.config(text ="Your_score:" +str(player_score))
def game(player_choice):
    pass

title_lable = Label(gui, text = "Rock Paper Scissors",font=("times",60))
title_lable.pack(pady = 10)

winner_lable = Label(gui, text = "lets start the game",font=("times",30),fg="black")
winner_lable.pack(pady = 10)

frame1 = Frame(gui)
frame1.pack(pady = 10)

options_lable = Label(frame1, text = "options: ",font=("times",30))
options_lable.grid(row=0,column=0)

rock_button = Button(frame1, text = "Rock",font=("times",15),command=lambda: game(options[0]))
rock_button.grid(row=1,column=1 ,padx = 8, pady = 5)

paper_button = Button(frame1, text = "Paper",font=("times",15),command=lambda: game(options[1]))
paper_button.grid(row=1,column=2,padx = 8, pady = 5)

scissors_button = Button(frame1, text = "Scissors",font=("times",15),command=lambda: game(options[2]))
scissors_button.grid(row=1,column=3,padx = 8, pady = 5)

frame2 = Frame(gui)
frame2.pack(pady = 10)

score_lable = Label(frame2, text = "Score",font=("times",15))
score_lable.grid(row=0,column=0)

player_lable = Label(frame2, text = "You selected: ---",font=("times",15))
player_lable.grid(row=1,column=1)

computer_lable = Label(frame2, text = "Computer selected: ---",font=("times",15))
computer_lable.grid(row=2,column=1)

player_score_lable = Label(frame2, text = "Your score: ---",font=("times",15))
player_score_lable.grid(row=1,column=2)

computer_score_lable = Label(frame2, text = "computer score: ---",font=("times",15))
computer_score_lable.grid(row=2,column=2)


gui.mainloop()