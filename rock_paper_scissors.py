from tkinter import*
import random

gui = Tk()

gui.title("Rock Paper Scissors")

player_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

def player_wins():
    global player_score
    player_score += 1
    player_score_lable.config(text="Your score: " + str(player_score))
    winner_lable.config(text= "You won")
    
def computer_wins():
    global computer_score
    computer_score += 1
    computer_score_lable.config(text="computer score: " + str(computer_score))
    winner_lable.config(text= "computer won")


def game(player_choice):
    computer_choice = random.choice(options)
    player_lable.config(text= "you selected: " +  player_choice)
    computer_lable.config(text="computer selected: " + computer_choice)
    if player_choice == "rock":
        if computer_choice == "paper":
            computer_wins()
        if computer_choice == "scissors":
            player_wins()
            
    if player_choice == "paper":
        if computer_choice == "scissors":
            computer_wins()
        if computer_choice == "rock":
            player_wins()
            
    if player_choice == "scissors":
        if computer_choice == "rock":
            computer_wins()
        if computer_choice == "paper":
            player_wins()
            
    if player_choice == computer_choice:
        winner_lable.config(text= "Draw")
        
title_lable = Label(gui, text="Rock Paper Scissors", font=("times", 60))
title_lable.pack(pady=10)

winner_lable = Label(gui, text="lets start the game", font=("times", 30), fg="black")
winner_lable.pack(pady=10)

frame1 = Frame(gui)
frame1.pack(pady=10)

options_lable = Label(frame1, text="options: ", font=("times", 30))
options_lable.grid(row=0, column=0)

rock_button = Button(frame1, text="Rock", font=("times", 15), command=lambda: game(options[0]))
rock_button.grid(row=1, column=1, padx=8, pady=5)

paper_button = Button(frame1, text="Paper", font=("times", 15), command=lambda: game(options[1]))
paper_button.grid(row=1, column=2, padx=8, pady=5)

scissors_button = Button(frame1, text="Scissors", font=("times", 15), command=lambda: game(options[2]))
scissors_button.grid(row=1, column=3, padx=8, pady=5)

frame2 = Frame(gui)
frame2.pack(pady=10)

score_lable = Label(frame2, text="Score", font=("times", 15))
score_lable.grid(row=0, column=0)

player_lable = Label(frame2, text="You selected: ---", font=("times", 15))
player_lable.grid(row=1, column=1)

computer_lable = Label(frame2, text="Computer selected: ---", font=("times", 15))
computer_lable.grid(row=2, column=1)

player_score_lable = Label(frame2, text="Your score: ---", font=("times", 15))
player_score_lable.grid(row=1, column=2)

computer_score_lable = Label(frame2, text="computer score: ---", font=("times", 15))
computer_score_lable.grid(row=2, column=2)

gui.mainloop()
