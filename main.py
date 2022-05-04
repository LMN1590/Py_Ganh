import minmax as mm
import welcome
import random
import demo
import sys
import pygame

def main():
    pygame.init() 
    while True:
        #Setting up UI
        screen=pygame.display.set_mode((800,600))
        pygame.display.set_caption("Cờ gánh")
        icon = pygame.image.load("./img/logo.png")
        pygame.display.set_icon(icon)
        ###############
        goFirst,level=welcome.welcome(screen)
        #If user decided to escape
        if(goFirst==-1 and level==-1):
            print("Program exited.")
            sys.exit()
        ###############
        #Who get to go first
        if (goFirst==1): player=-1 
        else: player=1 
        ###############
        #Setting up board
        mm.board()
        ###############
        #Current board
        res=[mm.board.current_board]
        ###############
        counter=0
        demo.move(mm.board.current_board,screen,counter)
        win=0
        while True:
            previous_board=mm.board.copy_board(mm.board.current_board)

            if (player==-1): #Bot -1
                move=mm.board.select_move(player,level)
                if move==None: 
                    win=1
                    break
            else:            #Random Agent 1
                valid_move_temp=mm.board.get_valid_moves(mm.board.current_board, mm.board.previous_board, player)
                for i in valid_move_temp:
                    print("Start: "+str(i.pos_start.x)+" "+str(i.pos_start.y))
                    print("End: "+str(i.pos_end.x)+" "+str(i.pos_end.y))
                if(len(valid_move_temp)==0):
                    win=-1
                    break
                index=random.randint(0,len(valid_move_temp)-1)
                move=valid_move_temp[index]
            #Move
            mm.board.act_move(mm.board.current_board,move,player)
            mm.board.previous_board=mm.board.copy_board(previous_board)
            counter+=1

            #Update to UI
            demo.move(mm.board.current_board,screen,counter)

            #Print to terminal for Debugging
            for i in range(5): print(mm.board.current_board[i])
            print()
            res.append(mm.dupTable(mm.board.current_board))
            player=-player
            if(counter>=100):
                score=0
                for i in range(5):
                    for j in range(5):
                        if(mm.board.current_board[i][j]==1): score-=1
                        elif(mm.board.current_board[i][j]==-1): score+=1
                if(score>0):
                    win=-1
                elif(score<0):
                    win=1
                else:
                    win=0
                break
        restart=demo.resDisOut(win,res,len(res),screen)
        res=[]
        mm.board.current_board=[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        mm.board.previous_board=[[]]
        if(restart):pass
        else: break
clock = pygame.time.Clock()
clock.tick(60)
main()