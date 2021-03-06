from tkinter import *  # imports all the needed code
import tkinter.messagebox
import pygame
click = True  # sets what click and tk start at
tk = None


def start():  # what goes on when the game is started
    global tk
    tk = Tk()
    tk.title("Tic Tac Toe")
    tk.update()
    file = 'Refreshing Elevator music.mp3'  # sets music to play every time the game starts
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.event.wait()

    def play(button):  # sets what happens when the play button is pressed
        global click, tk

        if button["text"] == " " and click:
            button["text"] = "X"
            click = False
        elif button["text"] == " ":
            button['text'] = "O"
            click = True

        if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or  # all of the if statement for x combinations to win
            button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
            button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
            button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
            button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
                button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
            answer = tkinter.messagebox.askquestion('X Player wins!!!', 'Do you want to play again')
            if answer == 'yes':  # the game will restart when yes is preesed which will only show up if the if's are true
                start()  # calls start
            try:  # if the answer is not yes then the game ends
                tk.destroy()
            except:
                pass

        elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or  # all of the if's for o to win
              button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
              button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
              button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
              button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
              button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
              button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
              button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
            answer = tkinter.messagebox.askquestion('O Player wins!!!', 'Do you want to play again')
            if answer == 'yes':
                start()
            try:
                tk.destroy()
            except:
                pass


# code to set how the buttons look, say, and interact
    button1 = Button(tk, text=" ", font=('Helvetica 10 bold italic'), height=4,
                     width=8, command=lambda: play(button1))
    button1.grid(row=1, column=0, sticky=S+N+E+W)

    button2 = Button(tk, text=" ", font=('Helvetica 10 bold italic'), height=4,
                     width=8, command=lambda: play(button2))
    button2.grid(row=1, column=1, sticky=S+N+E+W)

    button3 = Button(tk, text=" ", font=('Helvetica 10 bold italic'), height=4,
                     width=8, command=lambda: play(button3))
    button3.grid(row=1, column=2, sticky=S+N+E+W)

    button4 = Button(tk, text=" ", font=('Helvetica 10 bold italic'), height=4,
                     width=8, command=lambda: play(button4))
    button4.grid(row=2, column=0, sticky=S+N+E+W)

    button5 = Button(tk, text=" ", font=('Helvetica 10 bold italic'), height=4,
                     width=8, command=lambda: play(button5))
    button5.grid(row=2, column=1, sticky=S+N+E+W)

    button6 = Button(tk, text=" ", font=('Helvetica 10 bold italic'), height=4,
                     width=8, command=lambda: play(button6))
    button6.grid(row=2, column=2, sticky=S+N+E+W)

    button7 = Button(tk, text=" ", font=('Helvetica 10 bold italic'), height=4,
                     width=8, command=lambda: play(button7))
    button7.grid(row=3, column=0, sticky=S+N+E+W)

    button8 = Button(tk, text=" ", font=('Helvetica 10 bold italic'), height=4,
                     width=8, command=lambda: play(button8))
    button8.grid(row=3, column=1, sticky=S+N+E+W)

    button9 = Button(tk, text=" ", font=('Helvetica 10 bold italic'), height=4,
                     width=8, command=lambda: play(button9))
    button9.grid(row=3, column=2, sticky=S+N+E+W)

    tk.mainloop()


start()  # calls start
