#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 20:11:03 2020

@author: matt
"""
#DEFINITIONS
import tkinter as tk
from tkinter import Tk
window = tk.Tk()
window.title('TIC-TAC-TOE')
window.geometry("300x300")
button = tk.StringVar()
click = True
flag = 0

#GET PLAYER 1 TO CHOOSE X'S OR O'S
def player_input():
    marker = ''
    global click
    #get user X or O selection
    while marker != 'X' and marker != 'O':
        marker = input('Decide who goes first then Player 1 choose X or O: ')
    player1 = marker
    #assign player 2 opposite
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print('Player 1 is: ' + player1)
    print('Player 2 is: ' + player2)
    if player1 =='X': #sets up the counter for player1 and their selection
        click = True
    else:
        click = False
    return (player1, player2)
player_input()

#DETERMINES WHAT HAPPENS WHEN EACH BUTTON IS CLICKED
def game(button):
    global click, flag, player1, player2, player2_name, player1_name, playerb, pa
    if button["text"] == "-" and click == True:
        button["text"] = "X"
        click = False
        win_check()
        flag += 1

    elif button["text"] == "-" and click == False:
        button["text"] = "O"
        click = True
        win_check()
        flag += 1
    else:
        tk.messagebox.showinfo("Tic-Tac-Toe", "Button has already been Clicked!")
    pass

#CHECKS TO SEE IF ANYONE HAS WON YET OR IF A TIE OCCURS
def win_check():
    if ((Button1["text"] == 'X' and Button2["text"] == 'X' and Button3["text"] == 'X') or # across the top
        (Button4["text"] == 'X' and Button5["text"] == 'X' and Button6["text"] == 'X') or # across the middle
        (Button7["text"] == 'X' and Button8["text"] == 'X' and Button9["text"] == 'X') or # across the bottom
        (Button1["text"] == 'X' and Button4["text"] == 'X' and Button7["text"] == 'X') or # across the left
        (Button2["text"] == 'X' and Button5["text"] == 'X' and Button8["text"] == 'X') or # across the middle
        (Button3["text"] == 'X' and Button6["text"] == 'X' and Button9["text"] == 'X') or # across the right
        (Button1["text"] == 'X' and Button5["text"] == 'X' and Button9["text"] == 'X') or # diagnol 1
        (Button7["text"] == 'X' and Button5["text"] == 'X' and Button3["text"] == 'X')):# diagnol 2
        tk.messagebox.showinfo("Tic-Tac-Toe!! X WINS", "X's WIN!!!!!!")
        
    elif ((Button1["text"] == 'O' and Button2["text"] == 'O' and Button3["text"] == 'O') or # across the top
        (Button4["text"] == 'O' and Button5["text"] == 'O' and Button6["text"] == 'O') or # across the middle
        (Button7["text"] == 'O' and Button8["text"] == 'O' and Button9["text"] == 'O') or # across the bottom
        (Button1["text"] == 'O' and Button4["text"] == 'O' and Button7["text"] == 'O') or # across the left
        (Button2["text"] == 'O' and Button5["text"] == 'O' and Button8["text"] == 'O') or # across the middle
        (Button3["text"] == 'O' and Button6["text"] == 'O' and Button9["text"] == 'O') or # across the right
        (Button1["text"] == 'O' and Button5["text"] == 'O' and Button9["text"] == 'O') or # diagnol 1
        (Button7["text"] == 'O' and Button5["text"] == 'O' and Button3["text"] == 'O')):# diagnol 2
        tk.messagebox.showinfo("Tic-Tac-Toe!! O WINS", "O's WIN!!!!!")
    elif(flag == 8):
            tk.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

#BUILD GUI AND ASSIGN BUTTON LOCATIONS AND SIZES. ALSO ASSIGNS WHAT HAPPENS WHEN BUTTON CLICKED
frame = tk.Frame(master=window, borderwidth=1)
frame.pack()
Button1 = tk.Button(master=frame, text='-', height = 2, width = 2, command=lambda: game(Button1))
Button1.grid(row=0, column=0)
Button2 = tk.Button(master=frame, text='-', height = 2, width = 2, command=lambda: game(Button2))
Button2.grid(row=0, column=1)
Button3 = tk.Button(master=frame, text='-', height = 2, width = 2, command=lambda: game(Button3))
Button3.grid(row=0, column=2)
Button4 = tk.Button(master=frame, text='-', height = 2, width = 2, command=lambda: game(Button4))
Button4.grid(row=1, column=0)
Button5 = tk.Button(master=frame, text='-', height = 2, width = 2, command=lambda: game(Button5))
Button5.grid(row=1, column=1)
Button6 = tk.Button(master=frame, text='-', height = 2, width = 2, command=lambda: game(Button6))
Button6.grid(row=1, column=2)
Button7 = tk.Button(master=frame, text='-', height = 2, width = 2, command=lambda: game(Button7))
Button7.grid(row=2, column=0)
Button8 = tk.Button(master=frame, text='-', height = 2, width = 2, command=lambda: game(Button8))
Button8.grid(row=2, column=1)
Button9 = tk.Button(master=frame, text='-', height = 2, width = 2, command=lambda: game(Button9))
Button9.grid(row=2, column=2)
window.call('wm', 'attributes', '.', '-topmost', '1')
window.mainloop()
