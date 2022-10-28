import pygame
import time
from pygame.sprite import Sprite

class Rocket:
    """Lets build a rocket!!"""
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('../images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Display our rocket!!"""
        self.screen.blit(self.image, self.rect)

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position!!"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct pos!!
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's pos as  a dec val!!
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet up!!"""
        # Update dec pos of bullet
        self.y -= self.settings.bullet_speed
        # Update rect pos
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet on screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

def run_game(self):
    """Start the main loop for the game."""
    while True:
        # Redraw screen during each pass through the loop.
        self._check_events()
        self.ship.update()
        self._update_bullets()
        self._update_screen()

def _check_events(self):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            self._check_keyup_events(event)

def _check_keydown_events(self, event):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        self._fire_bullet()

def _check_keyup_events(self, event):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = False

def _fire_bullet(self):
    """Create a new bullet and add it to bullets group!!"""
    if len(self.bullets) < self.settings.bullets_allowed:
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

#pygame.display.flip()
time.sleep(4)