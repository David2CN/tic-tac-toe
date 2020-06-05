import pygame
pygame.init()

#display variable
screen = pygame.display.set_mode()

#collision points
first = pygame.Rect(0, 250, 240, 300)
second = pygame.Rect(240, 250, 240, 300)
third =  pygame.Rect(480, 250, 240, 300)
fourth =  pygame.Rect(0, 550, 240, 300)
fifth =  pygame.Rect(240, 550, 240, 300)
sixth = pygame.Rect(480, 550, 240, 300)
seventh =  pygame.Rect(0, 850, 240, 300)
eighth =  pygame.Rect(240, 850, 240, 300)
ninth =  pygame.Rect(480, 850, 240, 300)

#win_line
win_dict2 = {(0, 1, 2) : [(0, 400), (720, 400)],
(3, 4, 5) : [(0, 700), (720, 700)],
(6, 7, 8) : [(0, 1000), (720, 1000)],
(0, 3, 6) : [(120, 250), (120, 1150)],
(1, 4, 7) : [(360, 250), (360, 1150)],
(2, 5, 8) : [(600, 250), (600, 1150)],
(0, 4, 8) : [(0, 250), (720, 1150)],
(2, 4, 6) : [(720, 250), (0, 1150)] }

#open spaces
first_open = True
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eighth_open = True
ninth_open = True

#helper sets, the clicked positions are added into the sets eX and eO respectively. The game_over function would check each set after each turn to see if any has a winning set of positions(e.g 0, 1, 2)
eX = set()
eO = set()


#assist 1
def initialize_board(screen):
    """
    To initialize the board.
    """
    screen.fill((210, 210, 210))
    pygame.display.set_caption("Tic-Tac-Toe")
    #vertical and horizontal lines
    pygame.draw.line(screen, (0, 0, 150), (0, 550), (720, 550), 5)
    pygame.draw.line(screen, (0, 0, 150), (0, 850), (720, 850), 5)
    pygame.draw.line(screen, (0, 0, 150), (240, 250), (240, 1150), 5)
    pygame.draw.line(screen, (0, 0, 150), (480, 250), (480, 1150), 5)
    #Border
    pygame.draw.line(screen, (0, 0, 150), (0, 0), (0, 1300), 2)
    pygame.draw.line(screen, (0, 0, 150), (720, 0), (720, 1300), 2)
    pygame.draw.line(screen, (0, 0, 150), (0, 0), (720, 0), 2)
    pygame.draw.line(screen, (0, 0, 150), (0, 1300), (720, 1300), 2)
    #additional stuffs
    myfont = pygame.font.SysFont("DejaVuSans", 48)
    titlefont = pygame.font.SysFont("DejaVuSans", 64)
    titlefont.set_bold(True)
    label1 = titlefont.render("Tic - Tac - Toe", 1, (0, 0, 0))
    label2 = myfont.render("Player 1 - X    Player 2 - O", 1, (0, 0, 0))
    screen.blit(label1, (120, 50))
    screen.blit(label2, (50, 150))    
    return screen

#assist 2
def draw_status(screen):
    """
    To display the player turns and who won the game.
    """
    color = (50, 150, 75)
    myfont = pygame.font.SysFont("DejaVuSans", 48)
    label3  = myfont.render(message, 1, (0, 0, 0), color)
    screen.blit(label3, (200, 1200))
    return screen

#assist 3
def show_board(screen):
    """
    To show the board with current status.
    """
    #To overlay the previous status
    myfont = pygame.font.SysFont("DejaVuSans", 48)    
    temp = myfont.render( message, 1, (210, 210, 210), (210, 210, 210))
    screen.blit(temp, (200, 1200))
    draw_status(screen)
    return screen

#assist 4
def board_position(screen):
    pos = pygame.mouse.get_pos()
    return pos


#assist 5
def game_over(screen):
    """
    To check for a winner.
    """
    bool = False
    winner, cord = False, False
    wins = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]
    for i in wins:
        if i - eX == set():
            bool = True
            winner = "Player 1"
            cord = list(i)
        elif i - eO == set():
            bool = True
            winner = "Player 2"
            cord = list(i)
    return bool, winner, cord
        

#shapes
def drawX(screen, top, left):
    """
    To draw X.
    """
    start = left + 10, top + 20
    end = left + 230, top + 280
    start2 = left + 230, top + 20
    end2 = left + 10, top + 280
    pygame.draw.line(screen, (50, 150, 75), start, end, 7)
    pygame.draw.line(screen, (50, 150, 75), start2, end2, 7)

def drawC(screen, top, left):
    """
    To draw O.
    """
    center = left + 120, top + 150
    pygame.draw.circle(screen, (200, 50, 150), center, 115, 20)
    
def win_line(screen, cord):
    """
    the winning line.
    """
    for j in win_dict2:
        if sorted(j) == sorted(cord):
            start, end = win_dict2.get(j)
    pygame.draw.line(screen, (175, 50, 50), start, end, 10)
        

initialize_board(screen)
message, player = "Turn - Player 1", "1"
#game loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = board_position(screen)
            
            if first.collidepoint(pos) and first_open:
                top, left = first.top, first.left
                if player == "1":
                    drawX(screen, top, left)
                    player, message = "2", "Turn - Player 2"
                    eX.add(0)
                elif player == "2":
                    drawC(screen, top, left)
                    player, message = "1", "Turn - Player 1"
                    eO.add(0)
                first_open = False            
            
            if second.collidepoint(pos) and second_open:
                top, left = second.top, second.left
                if player == "1":
                    drawX(screen, top, left)
                    player, message = "2", "Turn - Player 2"
                    eX.add(1)
                elif player == "2":
                    drawC(screen, top, left)
                    player, message = "1", "Turn - Player 1"
                    eO.add(1)
                second_open = False

            if third.collidepoint(pos) and third_open:
                top, left = third.top, third.left
                if player == "1":
                    drawX(screen, top, left)
                    player, message = "2", "Turn - Player 2"
                    eX.add(2)
                elif player == "2":
                    drawC(screen, top, left)
                    player, message = "1", "Turn - Player 1"
                    eO.add(2)
                third_open = False
                
            if fourth.collidepoint(pos) and fourth_open:
                top, left = fourth.top, fourth.left 
                if player == "1":
                    drawX(screen, top, left)
                    player, message = "2", "Turn - Player 2"
                    eX.add(3)
                elif player == "2":
                    drawC(screen, top, left)
                    player, message = "1", "Turn - Player 1"
                    eO.add(3)
                fourth_open = False
                
            if fifth.collidepoint(pos) and fifth_open:
                top, left = fifth.top, fifth.left
                if player == "1":
                    drawX(screen, top, left)
                    player, message = "2", "Turn - Player 2"
                    eX.add(4)
                elif player == "2":
                    drawC(screen, top, left)
                    player, message = "1", "Turn - Player 1"
                    eO.add(4)
                fifth_open = False

            if sixth.collidepoint(pos) and sixth_open:
                top, left = sixth.top, sixth.left
                if player == "1":
                    drawX(screen, top, left)
                    player, message = "2", "Turn - Player 2"
                    eX.add(5)
                elif player == "2":
                    drawC(screen, top, left)
                    player, message = "1", "Turn - Player 1"
                    eO.add(5)
                sixth_open = False                        

            if seventh.collidepoint(pos) and seventh_open:
                top, left = seventh.top, seventh.left  
                if player == "1":
                    drawX(screen, top, left)
                    player, message = "2", "Turn - Player 2"
                    eX.add(6)
                elif player == "2":
                    drawC(screen, top, left)
                    player, message = "1", "Turn - Player 1"
                    eO.add(6)
                seventh_open = False

            if eighth.collidepoint(pos) and eighth_open:
                top, left = eighth.top, eighth.left
                if player == "1":
                    drawX(screen, top, left)
                    player, message = "2", "Turn - Player 2"
                    eX.add(7)
                elif player == "2":
                    drawC(screen, top, left)
                    player, message = "1", "Turn - Player 1"
                    eO.add(7)
                eighth_open = False
                
            if ninth.collidepoint(pos) and ninth_open:
                top, left = ninth.top, ninth.left
                if player == "1":
                    drawX(screen, top, left)
                    player, message = "2", "Turn - Player 2"
                    eX.add(8)
                elif player == "2":
                    drawC(screen, top, left)
                    player, message = "1", "Turn - Player 1"
                    eO.add(8)
                ninth_open = False                    

            temp = [first_open, second_open, third_open, fourth_open, fifth_open, sixth_open, seventh_open, eighth_open, ninth_open]
            if all([i == False for i in temp]):
                message = "Game Over - Draw!"
        
            if game_over(screen)[0]:
                message = game_over(screen)[1] + " Won!!!"
                win_line(screen, game_over(screen)[2])
                first_open, second_open, third_open, fourth_open, fifth_open, sixth_open, seventh_open, eighth_open, ninth_open = False, False, False, False, False, False, False, False, False                
                                
    show_board(screen)
    pygame.display.flip()    
    
if __name__ == '__main__':
    main()