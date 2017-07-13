#Pygame
import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

#define colours (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    #sprite for player
    def __init__(self): #initializes sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45,45))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH/2)
        self.rect.bottom = HEIGHT - 15
        
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        elif keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,35))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(4,12)
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)
         
        
#initialize pygame and create our window
pygame.init()
pygame.mixer.init() #enalbles sound
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
mobs = pygame.sprite.Group()
for i in range(8):
    mob = Mob()
    all_sprites.add(mob)
    mobs.add(mob)

#Game loop
running = True
while running:
    #keep loop running at the right speed
    clock.tick(FPS)
    #process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #update
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False
    #draw/render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #after drawing everyting, flip the display
    pygame.display.flip()
pygame.quit()
    

