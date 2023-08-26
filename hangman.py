import time
import random

print ("WELCOME TO THE GAME HANGMAN!!")
time.sleep(1)
print("-----------------------------------------")
print('1.Play\n2.Administrator')
print("-----------------------------------------")
def menu():
    # for choosing of interface
    choice1 = input('Enter 1 to Play & 2 for Administrator: ')
    # for user interface
    if choice1 == '1':
        name = input('ENTER YOUR NAME: ').upper()
        print("-----------------------------------------")

        def hangman():
            # for reading file of words
            with open("secret.txt") as f:
                a = f.read()
                spl = a.split()
            print('Loading word list from file...')
            print(len(spl), 'words loaded')
            print(name, 'Lets start the HANGMAN Game!')
            time.sleep(1)
            listOfWords = spl
            lives = 6
            letterpicked = []
            warnings = 3
            alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z']
            stralpha = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
            alpha = 'abcdefghijklmnopqrstuvwxyz'
            secret_word = random.choice(listOfWords)
            print('I am thinking of a word that is',len(secret_word),'letters long')
            print(len(secret_word) * "_ ")
            print()
            while True:
                print(lives, "LIVES LEFT")
                print(warnings, "WARNINGS LEFT")
                print("Available letters: ",stralpha,'\n')
                letter = input("Please guess a letter: ").lower()
                if letter not in alpha:  # for invalid input
                    print('OOPS! You enter a invalid character\nPlease enter an alphabet.\n')
                    continue
                if letter in letterpicked:
                    print("YOU HAVE TRIED THIS BEFORE!")
                    warnings -= 1
                    if warnings == 0:
                        lives -= 1
                    if warnings < 0:
                        warnings = 3
                    continue  # to restart the loop
                else:
                    letterpicked.append(letter)
                if letter in secret_word:
                    print("GOOD GUESS!\nYOU FOUND A LETTER")
                # for wrong guess
                else:
                    print("OOPS! THAT LETTER IS NOT IN THE WORD")
                    if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
                        lives -= 1
                    lives -= 1
                alphabet.remove(letter)
                # for changing list of alphabets into string
                stralpha = ''
                for i in alphabet:
                    stralpha +=(i+' ')
                allLetters = True
                # for good guess
                for i in secret_word:
                    if i in letterpicked:
                        print(i, end="")
                    else:
                        print("_ ", end="")
                        allLetters = False
                print('\n-----------------------------------------------------')
                print()
                if allLetters:
                    score = lives * len(set(secret_word))  # for calculating score
                    print(f"CONGRATULATIONS! YOU WON WITH {lives} LIVES LEFT ")
                    print(f'YOUR TOTAL SCORE FOR THIS GAME IS: {score}')
                    with open('score.txt','a+') as file:
                        file.write(' '+str(score))
                    # for calculating highscore
                    with open('score.txt') as file:
                        scr=file.read()
                        scr=scr.split()
                        count=0
                        for i in range(len(scr)):
                            if score>=int(scr[i]):
                                count+=1
                        # for writing highscore to the file
                        if count==len(scr):
                            print('CONGRATULATIONS! YOU ARE HANGMAN MASTER.\nYOU HAVE MADE HIGHSCORE!')
                            with open('highscore.txt','a') as f2:
                                f2.write(name+'     '+str(score)+'\n')

                    break
                # To display hangman
                if (lives == 5):
                    print("\n+---+")
                    print("|   |")
                    print("O   |")
                    print("    |")
                    print("    |")
                    print("   ===")
                elif (lives == 4):
                    print("\n+---+")
                    print("|   |")
                    print("O   |")
                    print("|   |")
                    print("    |")
                    print("   ===")
                elif (lives == 3):
                    print("\n +---+")
                    print(" |   |")
                    print(" O   |")
                    print("/|   |")
                    print("     |")
                    print("    ===")
                elif (lives == 2):
                    print("\n +---+")
                    print(" |   |")
                    print(" O   |")
                    print("/|\  |")
                    print("     |")
                    print("    ===")
                elif (lives == 1):
                    print("\n +---+")
                    print(" |   |")
                    print(" O   |")
                    print("/|\  |")
                    print("/    |")
                    print("    ===")
                elif (lives <= 0):
                    print("\n +---+")
                    print(" |   |")
                    print(" O   |")
                    print("/|\  |")
                    print("/ \  |")
                    print("    ===")
                if lives <= 0:
                    print("SORRY! YOU RAN OUT OF LIVES.\nTHE CORRECT ANSWER IS",secret_word,'\nYOUR SCORE IS 0\n')
                    break
            # to play again
            play_again=input('Do you want to play again[y/Y]? ')
            if play_again=='y' or play_again=='Y':
                hangman()
        hangman()
    # for administrator interface
    elif choice1 == '2':
        def administrator():
            print('\n1.View highscore\n2.Reset highscore\n3.Add words in file\n')
            choice2 = input('Enter 1 to view highscore 2 to reset highscore & 3 to add words in file: ')
            if choice2 == '1':
                # for displaying top three highscores
                with open('highscore.txt') as f2:
                    hscr=f2.readlines()
                    print()
                    print('***** HIGHSCORES *****')
                    print()
                    print('       NAME     SCORE')
                    count=0
                    for i in hscr[-1:-4:-1]:
                        count+=1
                        print(str(count)+'.     '+i,end='')
            if choice2 == '2':
                with open('highscore.txt','w+') as f3:
                   reset_hscr=f3.read()
                   print(reset_hscr)
                print('HIGHSCORES HAVE BEEN RESET!')


            if choice2 == '3':
                # for adding words
                with open("words.txt", 'a+') as f4:
                    add_wrds = input('Enter words you want to add separated by spaces: ')
                    spl_ = add_wrds.split()
                    for i in spl_:
                        f4.write(i + ' ')

        def account():
            acc = input('Do you have an account[y/n]: ')
            print()
            with open('myIds.txt') as f1:
                id_file = f1.read()
            if acc == 'y' or acc == 'Y':
                # for verifying existing account
                def id_():
                    id = input('Enter id: ')
                    if id in id_file:
                        pswrd = input('Enter password: ')
                        if pswrd in id_file:
                            administrator()
                        else:
                            print('Invalid password!\nPlease re-enter your id & password\n')
                            id_()
                    else:
                        print('Invalid id!\nPlease re-enter your id\n')
                        id_()
                id_()
            elif acc == 'n' or acc == 'N':
                # for making new account
                sign_up = input('Do you want to sign up[y/Y]: ')
                if sign_up == 'y' or sign_up == 'Y':
                    print()
                    with open('myIds.txt', 'a+') as f1:
                        id = input('Enter id:')
                        f1.write(id + '  ')
                        pswrd = input('Enter password: ')
                        f1.write(pswrd + ' ')
                        if pswrd in id_file:
                            print('Already Taken!')
                            pswrd = input('Enter a new password: ')
                            f1.write(pswrd + ' ')
                        administrator()
            else:
                print('Please enter a valid input!')
                account()

        account()
    else:
        print('Please enter valid input!')
        menu()

menu()



