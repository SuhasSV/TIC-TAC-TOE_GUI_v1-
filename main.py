from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Tic-Tac-Toe")
l1 = Label(root,text='player1:X', font="Helvetica")
l1.grid(row=0,column=0)
l2 = Label(root,text='player2:O', font="Helvetica")
l2.grid(row=0,column=1)

#check win status
winner = False
def disable_all_button():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)
def check_win():
    global winner
    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
        b1.config(bg = 'red')
        b2.config(bg = 'red')
        b3.config(bg = 'red')
        winner = True
        messagebox.showinfo(title="Tic-Tac-Toe: ", message="player1 wins!")
        disable_all_button()
    elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
        b4.config(bg = 'red')
        b5.config(bg = 'red')
        b6.config(bg = 'red')
        winner = True
        messagebox.showinfo(title="Tic-Tac-Toe: ", message="player1 wins!")
        disable_all_button()
    elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
        b1.config(bg = 'red')
        b2.config(bg = 'red')
        b3.config(bg = 'red')
        winner = True
        messagebox.showinfo(title="Tic-Tac-Toe: ", message="player1 wins!")
        disable_all_button()
    #checkwin player1 col
    elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        b1.config(bg = 'red')
        b4.config(bg = 'red')
        b7.config(bg = 'red')
        winner = True
        messagebox.showinfo(title="Tic-Tac-Toe: ", message="player1 wins!")
        disable_all_button()
    elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
        b2.config(bg = 'red')
        b5.config(bg = 'red')
        b8.config(bg = 'red')
        winner = True
        messagebox.showinfo(title="Tic-Tac-Toe: ", message="player1 wins!")
        disable_all_button()
    elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
        b3.config(bg = 'red')
        b6.config(bg = 'red')
        b9.config(bg = 'red')
        winner = True
        messagebox.showinfo(title="Tic-Tac-Toe: ", message="player1 wins!")
        disable_all_button()

    #check win for player2 rows
    elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        b1.config(bg = 'red')
        b2.config(bg = 'red')
        b3.config(bg = 'red')
        winner = True
        messagebox.showinfo(title="Tic-Tac-Toe: ", message="player2 wins!")
        disable_all_button()
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        b4.config(bg = 'red')
        b5.config(bg = 'red')
        b6.config(bg = 'red')
        winner = True
        messagebox.showinfo(title="Tic-Tac-Toe: ", message="player2 wins!")
        disable_all_button()
    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
        b7.config(bg = 'red')
        b8.config(bg = 'red')
        b9.config(bg = 'red')
        winner = True
        messagebox.showinfo(title="Tic-Tac-Toe: ", message="player2 wins!")
        disable_all_button()
    #checkwin player2 col
    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        b1.config(bg = 'red')
        b4.config(bg = 'red')
        b7.config(bg = 'red')
        winner = True
        messagebox.showinfo(title="Tic-Tac-Toe: ", message="player2 wins!")
        disable_all_button()
    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        b2.config(bg = 'red')
        b5.config(bg = 'red')
        b8.config(bg = 'red')
        winner = True
        messagebox.showinfo(title="Tic-Tac-Toe: ", message="player2 wins!")
        disable_all_button()
    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        b3.config(bg = 'red')
        b6.config(bg = 'red')
        b9.config(bg = 'red')
        winner = True
        messagebox.showinfo(title="Tic-Tac-Toe: ", message="player2 wins!")
        disable_all_button()
    #checkwin dia player1
    elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        b1.config(bg = 'red')
        b5.config(bg = 'red')
        b9.config(bg = 'red')
        winner = True
        messagebox.showinfo(title="Tic-Tac-Toe: ", message="player1 wins!")
        disable_all_button()
    elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
        b3.config(bg = 'red')
        b5.config(bg = 'red')
        b7.config(bg = 'red')
        winner = True
        messagebox.showinfo(title="Tic-Tac-Toe: ", message="player1 wins!")
        disable_all_button()
    #checkwin dia player2
    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        b1.config(bg = 'red')
        b5.config(bg = 'red')
        b9.config(bg = 'red')
        winner = True
        messagebox.showinfo(title="Tic-Tac-Toe: ", message="player2 wins!")
        disable_all_button()
    elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
        b3.config(bg = 'red')
        b5.config(bg = 'red')
        b7.config(bg = 'red')
        winner = True
        messagebox.showinfo(title="Tic-Tac-Toe: ", message="player1 wins!")
        disable_all_button()



#button functionality
clicked = True
count = 0
# "X" will be player 1, "O" will be player
def b_click(b):
    global clicked, count,dict_p1,dict_p2
    if b["text"] == " " and clicked == True:
        b['text'] = "X"
        clicked = False

        count+= 1
        check_win()
    elif b["text"] == " " and clicked == False:
        b['text'] = "O"
        clicked = True

        count+= 1
        check_win()
    else:
        messagebox.showerror(title="Tic-Tac-Toe", message="Box already selected\n pick another box")



#Building Buttons
b1 = Button(root, text=" ", font=("Helvetica",20),height = 3, width =6, bg="SystemButtonFace",command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica",20),height = 3, width =6, bg="SystemButtonFace",command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica",20),height = 3, width =6, bg="SystemButtonFace",command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica",20),height = 3, width =6, bg="SystemButtonFace",command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica",20),height = 3, width =6, bg="SystemButtonFace",command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica",20),height = 3, width =6, bg="SystemButtonFace",command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica",20),height = 3, width =6, bg="SystemButtonFace",command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica",20),height = 3, width =6, bg="SystemButtonFace",command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica",20),height = 3, width =6, bg="SystemButtonFace",command=lambda: b_click(b9))
# Grid buttons on the screen
b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3 , column=2)




root.mainloop()