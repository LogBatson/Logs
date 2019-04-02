import random
import regex
import time

gameend = False
#create opening file message
ctrl = True
if ctrl == True:
    print(" Welcome to this probability game! \n This was built in Python, and designed by Logan Batson. \n Type 'play' to play the game \n Alternatively, type 'bot' for the game to play itself. \n Data will be shown at the end when you lose all credits/money")
    ctrl = False
while ctrl == False and gameend == False:
    x = input()

    #funcs
    def dice():
        x = random.randint(1,6)
        return x
    def spinner():
        x = random.randint(1,8)
        if x < 6:
            return "red"
        elif x >= 6 and x < 8:
            return "blue"
        else:
            return "yellow"
    def baggie():
        x = random.randint(1,10)
        if x < 6:
            return "red"
        elif x >= 6 and x < 9:
            return "blue"
        elif x == 9:
            return "yellow"
        else:
            return "green"
    def winmessage(a,b,c,d,e):
        total = c + d + e
        if (a == "red" and b == "red" and total > 7):
            x = "You won $5!"
            return x
        elif (a == "blue" and b == "blue" and total > 12):
            x = "You won $10!"
            return x
        elif (a == "yellow" and b == "yellow" and c == 1 and d == 1 and e == 1):
            x = "You won $1000!!!"
            return x
        elif (a == "yellow" and b == "yellow" and c == 2 and d == 2 and e == 2):
            x = "You won $20!"
            return x
        elif (a == "yellow" and b == "yellow" and c == 3 and d == 3 and e == 3):
            x = "You won $20!"
            return x
        elif (a == "yellow" and b == "yellow" and c == 4 and d == 4 and e == 4):
            x = "You won $20!"
            return x
        elif (a == "yellow" and b == "yellow" and c == 5 and d == 5 and e == 5):
            x = "You won $20!"
            return x
        elif (a == "yellow" and b == "yellow" and c == 6 and d == 6 and e == 6):
            x = "You won $20!"
            return x
        elif (a == "red" and b == "blue" and total > 12):
            x = "You won $3!"
            return x
        elif (a == "blue" and b == "red" and total > 12):
            x = "You won $3!"
            return x
        elif (a == "blue" and b == "red" and total < 6):
            x = "You won $25!"
            return x
        elif (a == "red" and b == "blue" and total < 6):
            x = "You won $25!"
            return x
        elif (a == "green"):
            x = "You lost! Green is an automatic loss!"
            return x
        else:
            x = "You lost!"
            return x
    def winamt(a,b,c,d,e):
        total = c + d + e
        if (a == "red" and b == "red" and total > 7):
            x = 5
            return x
        elif (a == "blue" and b == "blue" and total > 12):
            x = 10
            return x
        elif (a == "yellow" and b == "yellow" and c == 1 and d == 1 and e == 1):
            x = 1000
            return x
        elif (a == "yellow" and b == "yellow" and c == 2 and d == 2 and e == 2):
            x = 20
            return x
        elif (a == "yellow" and b == "yellow" and c == 3 and d == 3 and e == 3):
            x = 20
            return x
        elif (a == "yellow" and b == "yellow" and c == 4 and d == 4 and e == 4):
            x = 20
            return x
        elif (a == "yellow" and b == "yellow" and c == 5 and d == 5 and e == 5):
            x = 20
            return x
        elif (a == "yellow" and b == "yellow" and c == 6 and d == 6 and e == 6):
            x = 20
            return x
        elif (a == "red" and b == "blue" and total > 12):
            x = 3
            return x
        elif (a == "blue" and b == "red" and total > 12):
            x = 3
            return x
        elif (a == "blue" and b == "red" and total < 6):
            x = 25
            return x
        elif (a == "red" and b == "blue" and total < 6):
            x = 25
            return x
        else:
            x = 0
            return x
    def letterCheck(x):
        if regex.search('[a-zA-Z]', x) == True:
            return True
        else:
            return False
        
    #inputs
    if x == "bot":
        botcredits = input("Enter the amount of credits for the bot:")
        try:
            int(botcredits)
            if int(botcredits) < 5:
                print("Enter a value over 5!")
            else:
                botcredits = int(botcredits)
                wins = losses = greenloss = totalwon = totalspent = yellowoneswins = turns = 0
                rr7 = bb12 = yysame = rb12 = rb6 = 0
                while botcredits >= 5:
                    dice1 = dice()
                    dice2 = dice()
                    dice3 = dice()
                    dicesum = dice1 + dice2 + dice3
                    bag = baggie()
                    spin = spinner()
                    
                    botcredits -= 5
                    amt = winamt(bag, spin, dice1, dice2, dice3)
                    botcredits += amt
                    
                    print("Remaining Credits" ,botcredits,)
                    
                    turns += 1
                    totalwon += amt
                    totalspent += 5
                    if amt == 0:
                        losses += 1
                    if amt != 0:
                        wins += 1
                    if bag == "green":
                        greenloss += 1
                    if amt == 1000:
                        yellowoneswins += 1
                    if amt == 3:
                        rb12 += 1
                    if amt == 5:
                        rr7 += 1
                    if amt == 10:
                        bb12 += 1
                    if amt == 20:
                        yysame += 1
                    if amt == 25:
                        rb6 += 1
                    
                    if botcredits < 5:
                        greenlossratio = greenloss/losses
                        yellowwinratio = yellowoneswins/wins
                        winloss = wins/losses
                        
                        print("Game over!")
                        print("\n Stats for this game:")
                        print("Turns:" ,turns,)
                        print("Total won:" ,totalwon,)
                        print("Total spent:" ,totalspent,)
                        print("Wins:" ,wins,)
                        print("Losses:" ,losses,)
                        print("Win/Loss ratio:" ,winloss,)
                        print("Loss by Green:" ,greenloss,)
                        print("Winning with all red and total < 7:" ,rr7,)
                        print("Winning with all blue and total > 12:" ,bb12,)
                        print("Winning with red/blue and total > 12:" ,rb12,)
                        print("Winning with red/blue and total < 6:" ,rb6,)
                        print("Winning with all yellow and same dice:" ,yysame,)
                        print("Winning with all yellow and ones:" ,yellowoneswins,)
                        if greenlossratio > 0:
                            print("Loss by green ratio:" ,greenlossratio,)
                        if yellowwinratio > 0:
                            print("Winning with yellow and ones ratio:" ,yellowwinratio,)
                        time.sleep(60)
                        gameend = True
        except ValueError:
            print("Enter a number!")
    elif x == "play":
        c = 50
        start = True
        if start == True:
            print("Type 'play' to play one turn. Each turn is 5 credits, you have 50 to begin.")
            start = False
            wins = losses = greenloss = totalwon = totalspent = yellowoneswins = turns = 0
        while c >= 5:
            inp = input()
            if inp == "play":
                dice1 = dice()
                dice2 = dice()
                dice3 = dice()
                dicesum = dice1 + dice2 + dice3
                bag = baggie()
                spin = spinner()
                
                print("You have pulled a" ,bag, "item from the baggie")
                print("You have spun the colour" ,spin,)
                print("And your dice rolls are" ,dice1, "," ,dice2, "," ,dice3,", Totaling:" ,dicesum,)
                
                c -= 5
                mess = winmessage(bag, spin, dice1, dice2, dice3)
                amt = winamt(bag, spin, dice1, dice2, dice3)
                print(mess)
                c += amt
                
                print("Your remaining credits are:" ,c,)
                
                turns += 1
                totalwon += amt
                totalspent += 5
                if amt == 0:
                    losses += 1
                if amt != 0:
                    wins += 1
                if bag == "green":
                    greenloss += 1
                if bag == "yellow" and spin == "yellow" and dice1 == 1 and dice2 == 1 and dice3 == 1:
                    yellowoneswins += 1
                
                if c < 5:
                    greenlossratio = greenloss/losses
                    yellowwinratio = yellowoneswins/wins
                    
                    print("You do not have enough credits to play again! Game over!")
                    print("\n Your stats for this game:")
                    print("Turns:" ,turns,)
                    print("Total won:" ,totalwon,)
                    print("Total spent:" ,totalspent,)
                    print("Wins:" ,wins,)
                    print("Losses:" ,losses,)
                    print("Loss by Green:" ,greenloss,)
                    print("Winning with all yellow and ones:" ,yellowoneswins,)
                    if greenlossratio > 0:
                        print("Loss by green ratio:" ,greenlossratio,)
                    if yellowwinratio > 0:
                        print("Winning with yellow ratio:" ,yellowwinratio,)
                    time.sleep(60)
                    gameend = True
            else:
                print("Not a valid command")
                continue
    else:
        print("Not a valid command")
        continue