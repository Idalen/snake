
import pygame, time
from pygame.locals import *
from random import randint

def drawGameWindow():
    screen.fill(BLACK) #limpa a tela
    screen.blit(apple, apple_pos)

    for pos in snake:
        screen.blit(snake_skin, pos)
        
    for pos in heart_pos:
        screen.blit(HEART, pos)
    
    pygame.display.update() 

def on_grid_random():
    x = randint(10, 580)//10*10
    y = randint(10, 580)//10*10
    return(x, y)

def collision_apple(c1, c2):
    return c1 == c2

def collision_snake(snake):
    for seg in snake[2:]:    
        if(seg == snake[0]):
            return True
    return False

   
BLOCK = (10,10)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

BLACK = 0, 0, 0
WHITE = 255, 255, 255
APPLE_RED = 212,17,17
SNAKE_GREEN = 112, 182, 84

HEART = pygame.image.load('pics/heart.png')
heart_number = 3
heart_pos = [(0,0), (10,0), (20,0)]
score_pos = (570, 590)
sound = 1

clock = pygame.time.Clock()

pygame.init() # inicia o pygame
screen = pygame.display.set_mode((600,600)) # define o tamanho da imagem
pygame.display.set_caption('fog snake')
pygame.mixer.init()

pygame.mixer.music.load("music/intro.wav")
pygame.mixer.music.play()


while heart_number:
    
    snake = [(200,200), (210,200), (220,200)] #posições da tela onde a cobra será plottada
    snake_skin = pygame.Surface(BLOCK)
    snake_skin.fill(SNAKE_GREEN)

    apple = pygame.Surface(BLOCK)      
    apple.fill(APPLE_RED)
    apple_pos= on_grid_random()  

    direction = LEFT
    paused = False
    walked = False
    score = 0

    while True:

        clock.tick(15 + score)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_UP and direction != DOWN:
                    direction = UP
                if event.key == K_RIGHT and direction != LEFT:
                    direction = RIGHT
                if event.key == K_DOWN and direction != UP:
                    direction = DOWN
                if event.key == K_LEFT and direction != RIGHT:
                    direction = LEFT
                if event.key == K_ESCAPE:
                    pygame.quit()
                if event.key == K_p:
                    paused = not paused
                if event.key == K_m:
                    sound = (sound+1)%2
                    pygame.mixer.music.set_volume(sound)
                
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("music/theme_song.wav")
            pygame.mixer.music.play(-1)
        
        if not paused:
            if collision_apple(snake[0], apple_pos):
                apple_pos = on_grid_random()
                snake.append((0,0))
                score+=1
        
            if collision_snake(snake):
                heart_pos.pop()
                heart_number = heart_number-1
                time.sleep(1)
                break
            

            for i in range(len(snake)-1, 0, -1):
                snake[i] = snake[i-1] 


            if direction == UP:
                snake[0] = (snake[0][0], snake[0][1] -10)
            elif direction == RIGHT:
                snake[0] = (snake[0][0] +10, snake[0][1])
            elif direction == DOWN:
                snake[0] = (snake[0][0], snake[0][1] +10)
            elif direction == LEFT:
                snake[0] = (snake[0][0] -10, snake[0][1])
            snake[0] = snake[0][0]%590, snake[0][1]%590

        drawGameWindow()

pygame.quit()    

        
      
