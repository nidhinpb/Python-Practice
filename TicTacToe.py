import os
def clear():
    os.system('clear')
ls=[]
def reset_g(ls):
    i=0
    for i in range(0,9):
        ls.append(" ")
reset_g(ls)
def func():
    def check(s,num):
        if((ls[0]==s and ls[1]==s and ls[2]==s)or(ls[0]==s and ls[3]==s and ls[6]==s)or(ls[0]==s and ls[4]==s and ls[8]==s)or(ls[1]==s and ls[4]==s and ls[7]==s)or(ls[6]==s and ls[7]==s and ls[8]==s)or(ls[8]==s and ls[5]==s and ls[2]==s)or(ls[4]==s and ls[6]==s and ls[2]==s)or(ls[3]==s and ls[4]==s and ls[5]==s)or(s=="TieCall" and num==1)):
            print("\n\n\t\t\tPlayer {} has Won, Congratulations!!!!!!!!".format(num))
            again=input("\n\nDo you want to Play Again:(Yes/No)")
            if again.lower()=="yes":
                clear()
                func()
            else:
                exit()
    print("\t\t\tWelcome to Tic Tac Toe")
    print("\t\t\t----------------------")
    print("Positions in Tic Tac Toe:")
    print("\t\t\t-------------\n\t\t\t| 7 | 8 | 9 |\n\t\t\t-------------")
    print("\t\t\t| 4 | 5 | 6 |\n\t\t\t-------------")
    print("\t\t\t| 1 | 2 | 3 |\n\t\t\t-------------")
    opi=input("To player 1-Do you want to start the game(Yes or No)? ")
    f=1
    if opi.lower()=="yes":
        print("\nPlayer {} can start".format(f))
    elif opi.lower()=="no":
        f=f+1
        print("\nPlayer {} can start".format(f))
    else:
        print("Invalid Command")
    if f==1:
        c=1
        while c!=10:
            if c%2==0:
                pos=int(input("Enter your desired position(1-9) according to sample given above:"))
                c=c+1
                ls[pos-1]="O"
                print("-------------\n| {} | {} | {} |\n-------------".format(ls[6],ls[7],ls[8]))
                print("| {} | {} | {} |\n-------------".format(ls[3],ls[4],ls[5]))
                print("| {} | {} | {} |\n-------------".format(ls[0],ls[1],ls[2]))
                check("O",f+1)
            elif c%2==1:
                pos=int(input("Enter your desired position(1-9) according to sample given above:"))
                c=c+1
                ls[pos-1]="X"
                print("-------------\n| {} | {} | {} |\n-------------".format(ls[6],ls[7],ls[8]))
                print("| {} | {} | {} |\n-------------".format(ls[3],ls[4],ls[5]))
                print("| {} | {} | {} |\n-------------".format(ls[0],ls[1],ls[2]))
                check("X",f)
        if c==10:
            print("\n\n\t\t\tGreat you both are Good, it's a TIE!!!!!!!!\n\n")
            check("TieCall",1)
    elif f==2:
        c=1
        while c!=10:
            if c%2==0:
                pos=int(input("Enter your desired position(1-9) according to sample given above:"))
                c=c+1
                ls[pos-1]="O"
                print("-------------\n| {} | {} | {} |\n-------------".format(ls[6],ls[7],ls[8]))
                print("| {} | {} | {} |\n-------------".format(ls[3],ls[4],ls[5]))
                print("| {} | {} | {} |\n-------------".format(ls[0],ls[1],ls[2]))
                check("O",f-1)
            elif c%2==1:
                pos=int(input("Enter your desired position(1-9) according to sample given above:"))
                c=c+1
                ls[pos-1]="X"
                print("-------------\n| {} | {} | {} |\n-------------".format(ls[6],ls[7],ls[8]))
                print("| {} | {} | {} |\n-------------".format(ls[3],ls[4],ls[5]))
                print("| {} | {} | {} |\n-------------".format(ls[0],ls[1],ls[2]))
                check("X",f)
        if c==10:
            print("\n\n\t\t\tGreat you both are Good, it's a TIE!!!!!!!!\n\n")
            check("TieCall",1)
func()
