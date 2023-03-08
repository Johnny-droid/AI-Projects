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
        self.state = STATE_MENU
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game = Game(execute_random_move, execute_random_move)
        self.menu = Menu()


    def run(self):
        pygame.init()
        pygame.display.set_caption("Wana Game")

        while True:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                
                if event.type == KEYDOWN:
                    # Press P to pause
                    if event.key == K_p and self.state == STATE_GAME:
                        self.prev_state = self.state
                        self.state = STATE_PAUSE
                    elif event.key == K_p and self.state == STATE_PAUSE:
                        self.state = self.prev_state


            if self.state == STATE_MENU:
                self.menu.draw(self.screen)

            elif self.state == STATE_GAME:
                
                self.game.player_move()
                if self.game.exists_winner() != -1:
                    print("Player", self.game.exists_winner(), "wins!")
                    break

                self.game.draw(self.screen)
                
            
            pygame.display.update()
            # Wait for 1 second
            # self.clock.tick(1)

            


wana = Wana()
wana.run()