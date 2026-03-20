import pygame
import time
import random

# Game variables initializations 

#pygame init
pygame.init()
HAUTEUR = 600
LARGEUR = 600
SCREEN = pygame.display.set_mode((HAUTEUR, LARGEUR))
pygame.display.set_caption("snake_game_ai")
tile_size = 50

#colors init
APPLE_RED = (200, 0, 0)
TILE_GREEN = (0, 255, 0)
SNAKE_GREEN = (0, 100, 0)
WALL_BROWN = (150, 42, 42)
BLACK = (0, 0, 0)


background = TILE_GREEN

def draw_rect(x, y, color): #Draws a rectangle of a specific color
    rect = pygame.Rect(x, y, tile_size, tile_size)
    rect = rect.inflate(-2, -2)
    pygame.draw.rect(SCREEN, color, rect)

def draw_scene(): #Draws the static basic scene
    SCREEN.fill(BLACK)
    for x in range(0, LARGEUR, tile_size):
        for y in range(0, HAUTEUR, tile_size):
            if (y == 0 or y == (HAUTEUR - tile_size) or x == 0 or x == (LARGEUR - tile_size)):
                draw_rect(x, y, WALL_BROWN)
            else:
                draw_rect(x, y, TILE_GREEN)
    

class snake:
    score = 0
    body = []
    direction = []
    apple_pos = ()

    def __init__(self, direction):
        self.body = [[3*tile_size, 3*tile_size]]
        self.direction = direction
        self.apple_pos = (6*tile_size, 6*tile_size)
        self.handle_apple()

    def draw(self):
        for x in self.body:
            draw_rect(x[0], x[1], SNAKE_GREEN)

    def update(self, new_dir):
        self.handle_body(new_dir)
        if (self.body[0] == self.apple_pos):
            score += 1
            self.handle_apple()
        
        
    def handle_body(self, new_dir):
        if new_dir == None:
            new_dir = self.direction
        self.direction = new_dir
        # Calculate new head position
        new_head = [self.body[0][0] + new_dir[0] * tile_size, 
                    self.body[0][1] + new_dir[1] * tile_size]
        i = 0
        while i < len(self.body):
            if i == 0:
                self.body[i] = new_head
            else:
                self.body[i] = self.body[i - 1]
            i += 1
        print (self.body)
    
    def handle_apple(self):
        x = random.randrange(0, LARGEUR, tile_size)
        y = random.randrange(0, HAUTEUR, tile_size)
        if ((x, y) in self.body):
            self.handle_apple(self.body)
        else:
            draw_rect(x, y, APPLE_RED)
                


running = True

def key_hook(ev):
    if ev.type == pygame.KEYUP:
        if ev.key == pygame.K_LEFT:
            return [-1, 0]
        elif ev.key == pygame.K_RIGHT:
            return [1, 0]
        elif ev.key == pygame.K_UP:
            return [0, -1]
        elif ev.key == pygame.K_DOWN:
            return [0, 1]
        elif ev.key == pygame.K_ESCAPE:
            running = False


direction = [1, 0]
Snake = snake(direction)

# Main event loop
while (running):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: #safe exit
            running = False
        direction = key_hook(ev)
        Snake.update(direction)
        draw_scene()
        Snake.draw()
        pygame.display.update()





# Closing process
print("closing game..")
pygame.quit()