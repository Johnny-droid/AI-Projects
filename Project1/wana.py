from game import *
from menu import *
from ai import *


STATE_MENU = 0
STATE_GAME = 1
STATE_PAUSE = 2
STATE_GAMEOVER = 3
STATE_EXIT = 4

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

class Wana:
    def __init__(self):
        pygame.init()
        self.state = STATE_MENU
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game = None
        self.menu = Menu()


    def run(self):
        
        pygame.display.set_caption("Wana Game")

        while True:
            self.screen.fill((0, 0, 0))

            events = pygame.event.get()

            # for event in pygame.event.get():
            #     if event.type == QUIT:
            #         exit()
                
            #     if event.type == KEYDOWN:
            #         # Press P to pause
            #         if event.key == K_p and self.state == STATE_GAME:
            #             self.prev_state = self.state
            #             self.state = STATE_PAUSE
            #         elif event.key == K_p and self.state == STATE_PAUSE:
            #             self.state = self.prev_state


            if self.state == STATE_MENU:
                self.menu.run(self.screen)
                if self.menu.ready:
                    self.game = Game(self.menu.player1, self.menu.player2, self.menu.board_number)
                    self.state = STATE_GAME
                
                
                
            elif self.state == STATE_GAME:
                
                self.game.player_move()
                if self.game.get_winner() != -1:
                    print("Player", self.game.get_winner(), "wins!")
                    break

                self.game.draw(self.screen)
                
            
            pygame.display.update()
            # Wait for 1 second
            # self.clock.tick(1)

            


wana = Wana()
wana.run()