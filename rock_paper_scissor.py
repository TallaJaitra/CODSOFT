from tkinter import *
from PIL import Image,ImageTk
from random import randint
root=Tk()
root.title("Rock Paper Scissor")
root.configure(bg='green')
rock_img = ImageTk.PhotoImage(Image.open("C:\\Users\minnu&nani\Downloads\\rock_pic.png"))
paper_img = ImageTk.PhotoImage(Image.open("C:\\Users\minnu&nani\Downloads\\paper_pic.png"))
sci_img = ImageTk.PhotoImage(Image.open("C:\\Users\minnu&nani\Downloads\\sci_pic.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("C:\\Users\minnu&nani\Downloads\\rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("C:\\Users\minnu&nani\Downloads\\paper.png"))
sci_img_comp = ImageTk.PhotoImage(Image.open("C:\\Users\minnu&nani\Downloads\\scissor.png"))

user_label = Label(root,image=sci_img,bg='green')
comp_label = Label(root,image=sci_img_comp,bg='green')
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

playerscore = Label(root,text=0,font=100,bg='green',fg='white')
computerscore = Label(root,text=0,font=100,bg='green',fg='white')
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

user_indicator=Label(root,font=50,text='USER',bg='green',fg='white')
comp_indicator=Label(root,font=50,text='COMPUTER',bg='green',fg='white')
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

msg=Label(root,font=50,bg='green',fg='white')
msg.grid(row=3,column=2)

def updateMessage(x):
    msg['text'] = x

def updateUserScore():
    score =int(playerscore["text"])
    score+=1
    playerscore["text"]=str(score)

def updateCompScore():
    score =int(computerscore["text"])
    score+=1
    computerscore["text"]=str(score)


def checkwin(player,computer):
    if player == computer:
        updateMessage("Its a tie !!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("you loose !!!!")
            updateCompScore()
        else:
            updateMessage("you win !!!!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("you loose !!!!")
            updateCompScore()
        else:
            updateMessage("you win !!!!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("you loose !!!!")
            updateCompScore()
        else:
            updateMessage("you win !!!!")
            updateUserScore()
    else:
        pass

choices = ["rock","paper","scissor"]
def updateChoice(x):
#for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=sci_img_comp)



    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=sci_img)

    checkwin(x,compChoice)

rock = Button(root,width=20,height=2,text="ROCK",bg='red',fg='white',command=lambda : updateChoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg='yellow',fg='black',command=lambda : updateChoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg='blue',fg='white',command=lambda : updateChoice("scissor")).grid(row=2,column=3)


root.mainloop()
