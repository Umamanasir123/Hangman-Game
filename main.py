import random
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import time
score = 0
run = True
def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, tick)
def Stop():
    clock.destroy()
# main loop
while run:
    root = Tk()
    root.geometry('905x700')
    root.title('HANG MAN GAME')
    root.config(bg='#E7FFFF')
    count = 0
    win_count = 0
    clock = Label(root, bg="Yellow", font=("Algerian", 25))
    clock.place(x=1100, y=10, width=200, height=50)
    tick()
    bg = PhotoImage(file="hangmanimg.png")
    bg_label = Label(root, image=bg,width=480,height=420,bg="#E7FFFF")
    bg_label.place(x=840, y=100)
    # choosing wordwith open("secret.txt")as f:
    with open("secret.txt") as f:
      a=f.read()
      spl=a.split()
      listOfWords = spl
      lives = 6
      letterpicked = []
      word = random.choice(listOfWords)
      # creation of word dashes variables
      x = 220
      for i in range(len(word)):
          x += 50
          exec('d{}=Label(root,text="_",bg="#E7FFFF",font=("arial",40))'.format(i))
          exec('d{}.place(x={},y={})'.format(i, x, 450))

      # letters icon
      al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
      for let in al:
          exec('{}=PhotoImage(file="{}.png")'.format(let, let))
      # letters placement
      button = [['b1', 'a', 0+50, 595], ['b2', 'b', 70+50, 595], ['b3', 'c', 140+50, 595], ['b4', 'd', 210+50, 595],
                ['b5', 'e', 280+50, 595], ['b6', 'f', 350+50, 595], ['b7', 'g', 420+50, 595], ['b8', 'h', 490+50, 595],
                ['b9', 'i', 560+50, 595], ['b10', 'j', 630+50, 595], ['b11', 'k', 700+50, 595], ['b12', 'l', 770+50, 595],
                ['b13', 'm', 840+50, 595], ['b14', 'n', 0+50, 645], ['b15', 'o', 70+50, 645], ['b16', 'p', 140+50, 645],
                ['b17', 'q', 210+50, 645], ['b18', 'r', 280+50, 645], ['b19', 's', 350+50, 645], ['b20', 't', 420+50, 645],
                ['b21', 'u', 490+50, 645], ['b22', 'v', 560+50, 645], ['b23', 'w', 630+50, 645], ['b24', 'x', 700+50, 645],
                ['b25', 'y', 770+50, 645], ['b26', 'z', 840+50, 645]]

      # hangman images
      h123 = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7']
      for hangman in h123:
          exec('{}=PhotoImage(file="{}.png")'.format(hangman, hangman))

       # hangman placement
      han = [['c1', 'h1'], ['c2', 'h2'], ['c3', 'h3'], ['c4', 'h4'], ['c5', 'h5'], ['c6', 'h6'], ['c7', 'h7']]
      for p1 in han:
        exec('{}=Label(root,bg="#E7FFFF",image={})'.format(p1[0], p1[1]))
      # placement of first hangman image
      c1.place(x=300, y=- 50)

      lv1 = 'AVAILABLE LETTERS: '
      lv2 = Label(root, text=lv1, bg="pink",fg="purple", font=("algerian", 25))
      lv2.place(x=206, y=540)

      for q1 in button:
          exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(
                  q1[0], q1[1], q1[0], q1[1]))
          exec('{}.place(x={},y={})'.format(q1[0], q1[2], q1[3]))

      # exit buton
      def close():
          global run
          answer = messagebox.askyesno('ALERT', 'YOU WANT TO EXIT THE GAME?')
          if answer == True:
              run = False
              root.destroy()


      e1 = PhotoImage(file='exit.png')
      ex = Button(root, bd=0, command=close, bg="#E7FFFF", activebackground="#E7FFFF", font=10, image=e1)
      ex.place(x=770, y=10)
      s2 = 'SCORE:0'
      s1 = Label(root, text=s2, bg="#E7FFFF", font=("algerian", 25))
      s1.place(x=10, y=10)
      lv2 = 'LIVES:' + str(lives)
      lv1 = Label(root, text=lv2, bg="#E7FFFF", font=("algerian", 25))
      lv1.place(x=10, y=60)

      # button press check function
      def check(letter, button):
          global count, win_count, run, score, lives,warnings
          exec('{}.destroy()'.format(button))
          lv2 = 'LIVES:' + str(lives)
          if letter in word:
              for i in range(0, len(word)):
                  if word[i] == letter:
                      win_count += 1
                      s2 = 'SCORE:' + str(win_count)
                      s1 = Label(root, text=s2, bg="#E7FFFF", font=("algerian", 25))
                      s1.place(x=10, y=10)
                      exec('d{}.config(text="{}")'.format(i, letter.upper()))
              if win_count == len(word):
                  answer = messagebox.askyesno('Congratulations', 'YOU WON!\nWANT TO PLAY AGAIN?')
                  if answer == True:
                      run = True
                      root.destroy()
                  else:
                      run = False
                      root.destroy()
          else:
              if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):

                  lives = lives - 2
                  if (lives == -1):
                      lives = 0
                  han = [['c1', 'h1'], ['c2', 'h2'], ['c3', 'h3'], ['c4', 'h4'], ['c5', 'h5'], ['c6', 'h6'],
                         ['c7', 'h7']]
                  if(lives==4):
                     c3.place(x=300, y=- 50)
                  elif(lives==3):
                     c4.place(x=300, y=- 50)
                  elif (lives==2):
                     c5.place(x=300, y=- 50)
                  elif (lives==1):
                     c6.place(x=300, y=- 50)
                  elif (lives==0):
                     c7.place(x=300, y=- 50)
              else:
                  lives=lives-1
                  if(lives==5):
                      c2.place(x=300, y=- 50)
                  elif (lives == 4):
                      c3.place(x=300, y=- 50)
                  elif (lives == 3):
                      c4.place(x=300, y=- 50)
                  elif (lives == 2):
                      c5.place(x=300, y=- 50)
                  elif (lives == 1):
                      c6.place(x=300, y=- 50)
                  elif (lives == 0):
                      c7.place(x=300, y=- 50)
              lv2 = 'LIVES:' + str(lives)
              lv1 = Label(root, text=lv2, bg="#E7FFFF", font=("algerian", 25))
              lv1.place(x=10, y=60)
              count += 1
              exec('c{}.destroy()'.format(count))
              exec('c{}.place(x={},y={})'.format(count + 1, 300, -50))
              if (count == 6 or lives==0):
                   Stop()
                   s2 = 'YOU RAN OUT OF LIVES.\nCORRECT ANSWER:' + str(word)
                   s1 = Label(root, text=s2, bg="#E7FFFF", font=("algerian", 17))
                   s1.place(x=10, y=120)
                   answer = messagebox.askyesno('GAME OVER', 'YOU LOST!\nWANT TO PLAY AGAIN?')
                   if answer == True:
                      run = True
                      score = 0
                      root.destroy()
                   else:
                      run = False
                      root.destroy()


      root.mainloop()


