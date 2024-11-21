import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        self.image = pygame.image.load('C:/Users/omolo/OneDrive/Desktop/CSC141/alien_invasion/images/zara_idle_1.png')

        # Scale the image by a factor of 3 using the current dimensions
        self.image = pygame.transform.scale(self.image, 
                                            (self.image.get_rect().width * 3, self.image.get_rect().height * 3))
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x



    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
