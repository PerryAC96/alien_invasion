import sys

import pygame

class AlienInvasion:
    """Over class to manage game assests and behavior"""

    def  _init_(self):
        """Initialize the game and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT():
                    sys.exit()

                # Make the most recently drawn screen visible.
            pygame.display.flip()
    if _name_ == '_main_':
        # Make a game instance, and run the game.
        ai = AlienInvasion()
        ai.run_game()
    def _init_self(self):
        
        pygame.display.set_caption("Alien Invasion")

        #Set the background color.
        self.bg_color = (230, 230, 230)
    def run_game(self):
        for event in pygame.event.get():
            sys.exit()
        #Redraw the most recnelty drawn screen visible.
        pygame.display.flip()    
        
