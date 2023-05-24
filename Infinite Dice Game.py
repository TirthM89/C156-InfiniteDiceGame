from tkinter import *
from PIL import ImageTk,Image
import random

root = Tk()
root.title("Endless Dice Game")
root.geometry("600x400")
root.configure(bg = 'lightblue')


player1 = Label(root, text = 'Player 1', bg = "purple", fg = "white")
player1.place(relx = 0.15, rely = 0.3, anchor = CENTER)
player2 = Label(root, text = 'Player 2', bg = "orange", fg = "black")
player2.place(relx = 0.85, rely = 0.3, anchor = CENTER)
p1s = Label(root, bg = "purple", fg = "white")
p1s.place(relx = 0.15, rely = 0.4, anchor = CENTER)
p2s = Label(root, bg = "orange", fg = "black")
p2s.place(relx = 0.85, rely = 0.4, anchor = CENTER)
random_dice = Label(root, bg = "black", fg = "white")
random_dice.place(relx = 0.5, rely = 0.5, anchor = CENTER)
img = Image.open("download.jfif")
resized_image= img.resize((100,100))
img1 = ImageTk.PhotoImage(resized_image)

player1score = 0

def p1():
    global player1score
    random_number = random.randint(1,6)
    random_dice["text"] = "Player 1 Score is "+str(random_number)
    player1score = player1score + random_number
    p1s["text"] = str(player1score)
    
btn1 = Button(root, image = img1, command = p1)
btn1.place(relx = 0.15, rely = 0.6, anchor = CENTER)


player2score = 0

def p2():
    global player2score
    random_number2 = random.randint(1,6)
    random_dice["text"] = "Player 2 Score is "+str(random_number2)
    player2score = player2score + random_number2
    p2s["text"] = str(player2score)
    
btn2 = Button(root, image = img1, command = p2)
btn2.place(relx = 0.85, rely = 0.6, anchor = CENTER)

root.mainloop()