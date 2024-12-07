import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Load the bullet image and set its rect attribute
        self.image = pygame.image.load('alien_invasion/images/star.png').convert_alpha() 
        # Scale the image using the current dimensions
        self.image = pygame.transform.scale(self.image, 
                                            (self.image.get_rect().width * 0.2, self.image.get_rect().height * 0.2))
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Store the bullet's position as a float
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet image to the screen."""
        self.screen.blit(self.image, self.rect)