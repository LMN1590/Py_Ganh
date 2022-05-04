import pygame

numKey=[pygame.K_0,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9,pygame.K_KP_0,pygame.K_KP_1,pygame.K_KP_2,pygame.K_KP_3,pygame.K_KP_4,pygame.K_KP_5,pygame.K_KP_6,pygame.K_KP_7,pygame.K_KP_8,pygame.K_KP_9]
def move(board2,screen,counter):
    screen.fill((131,238,255))
    
    #####################
    #Title
    title=[pygame.Rect(200,40,400,100),pygame.Rect(210,50,380,80)]
    pygame.draw.rect(screen,(139,69,19),title[0])
    pygame.draw.rect(screen,(255,222,173),title[1])
    fontTitle=pygame.font.Font("./font/Unicode/times.ttf",50)
    textTitle=fontTitle.render("Bước "+str(counter),True, (0,0,0))
    screen.blit(textTitle,(320,60))
    #####################

    #Board
    board=[pygame.Rect(255,160,290,290),pygame.Rect(260,165,280,280)]
    pygame.draw.rect(screen,(139,69,19),board[0])
    pygame.draw.rect(screen,(255,222,173),board[1])
    pygame.draw.line(screen,(0,0,0),(260,165),(540,445),5)
    pygame.draw.line(screen,(0,0,0),(260,445),(540,165),5)
    pygame.draw.line(screen,(0,0,0),(400,165+26),(540-26,305),5)
    pygame.draw.line(screen,(0,0,0),(400,165+26),(260+26,305),5)
    pygame.draw.line(screen,(0,0,0),(400,445-26),(260+26,305),5)
    pygame.draw.line(screen,(0,0,0),(400,445-26),(540-26,305),5)
    column=[pygame.Rect(260+(i+1)*52 + i*5,165,5,280) for i in range(4)]
    row=[pygame.Rect(260,165+(i+1)*52 + i*5,280,5) for i in range(4)]
    for i in range(4):
        pygame.draw.rect(screen,(0,0,0),column[i])
        pygame.draw.rect(screen,(0,0,0),row[i])
    for i in range(5):
        for j in range(5):
            startLeft=j*57+ 4 + 260
            startTop=i*57+ 4 + 165
            if(board2[i][j]==1):
                sq=pygame.Rect(startLeft,startTop,44,44)
                pygame.draw.rect(screen,(200,0,0),sq)
            elif (board2[i][j]==-1):
                sq=pygame.Rect(startLeft,startTop,44,44)
                pygame.draw.rect(screen,(0,0,200),sq)
    pygame.display.update()


def resDisOut(win,res,length,screen):
    font=pygame.font.Font("./font/Unicode/times.ttf",25)
    active=False
    user_text = ""
    counter=length
    running=True
    while running:
        screen.fill((131,238,255))
        
        #####################
        #Title
        title=[pygame.Rect(200,40,400,100),pygame.Rect(210,50,380,80)]
        pygame.draw.rect(screen,(139,69,19),title[0])
        pygame.draw.rect(screen,(255,222,173),title[1])
        fontTitle=pygame.font.Font("./font/Unicode/times.ttf",50)
        font=pygame.font.Font("./font/Unicode/times.ttf",25)
        textTitle=fontTitle.render("Bước "+str(counter),True, (0,0,0))
        screen.blit(textTitle,(320,60))
        #####################

        #Board
        board=[pygame.Rect(255,160,290,290),pygame.Rect(260,165,280,280)]
        pygame.draw.rect(screen,(139,69,19),board[0])
        pygame.draw.rect(screen,(255,222,173),board[1])
        pygame.draw.line(screen,(0,0,0),(260,165),(540,445),5)
        pygame.draw.line(screen,(0,0,0),(260,445),(540,165),5)
        pygame.draw.line(screen,(0,0,0),(400,165+26),(540-26,305),5)
        pygame.draw.line(screen,(0,0,0),(400,165+26),(260+26,305),5)
        pygame.draw.line(screen,(0,0,0),(400,445-26),(260+26,305),5)
        pygame.draw.line(screen,(0,0,0),(400,445-26),(540-26,305),5)
        column=[pygame.Rect(260+(i+1)*52 + i*5,165,5,280) for i in range(4)]
        row=[pygame.Rect(260,165+(i+1)*52 + i*5,280,5) for i in range(4)]
        for i in range(4):
            pygame.draw.rect(screen,(0,0,0),column[i])
            pygame.draw.rect(screen,(0,0,0),row[i])
        for i in range(5):
            for j in range(5):
                startLeft=j*57+ 4 + 260
                startTop=i*57+ 4 + 165
                if(res[counter-1][i][j]==1):
                    sq=pygame.Rect(startLeft,startTop,44,44)
                    pygame.draw.rect(screen,(200,0,0),sq)
                elif (res[counter-1][i][j]==-1):
                    sq=pygame.Rect(startLeft,startTop,44,44)
                    pygame.draw.rect(screen,(0,0,200),sq)
        if(win==0):
            textRes=font.render("Hòa",True,(220,0,0))
            screen.blit(textRes,(380,460))
        elif(win==1):
            textRes=font.render("Agent Random thắng",True,(220,0,0))
            screen.blit(textRes,(290,460))
        else:
            textRes=font.render("Bot thắng",True,(220,0,0))
            screen.blit(textRes,(350,460))
        textLen=font.render("/"+str(length),True,(0,0,0))
        screen.blit(textLen,(401,520))
        slideInput=pygame.Rect(340,520,60,30)
        pygame.draw.rect(screen,(0,0,0),slideInput)
        textInput=font.render(user_text,True,(200,200,200))
        screen.blit(textInput, (slideInput.x+2, slideInput.y+2))
        home=pygame.Rect(77,275,100,50)
        pygame.draw.rect(screen,(255,222,173),home)
        textHome=font.render("Quay lại",True,(0,0,0))
        screen.blit(textHome,(82,283))
        quit=pygame.Rect(622,275,100,50)
        textQuit=font.render("Thoát",True,(0,0,0))
        pygame.draw.rect(screen,(255,222,173),quit)
        screen.blit(textQuit,(640,283))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                return False
            if event.type==pygame.KEYDOWN:
                # Check for backspace
                if event.key==pygame.K_LEFT:
                    if(counter==1):
                        counter=1
                    else:
                        counter-=1
                elif event.key==pygame.K_RIGHT:
                    if(counter==length):
                        counter=length
                    else:
                        counter+=1
                elif active:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key in numKey:
                        if (len(user_text) < 4):
                            user_text += event.unicode
                    elif event.key==pygame.K_RETURN:
                        newer=int(user_text)
                        if(newer<1):newer=1
                        if(newer>length): newer=length
                        counter=newer
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if slideInput.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                if home.collidepoint(event.pos):
                    running=False
                    return True
                if quit.collidepoint(event.pos):
                    running=False
                    return False
        pygame.display.update()


