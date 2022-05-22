## Adding The Food ##
In this section we will add the food that the snake will eat onto the screen.  You will notice that the length of the snake does not extend when teh snake passes over the food; instead we will print out a message onto the termianl!
For our example the message will be `Yummy!!` but it can be anything - it is just to show that the script has acknowledged the food has been eaten by the snake.

**Code for the snake's food:**
```
import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

dis_width = 800
dis_length = 600

dis = pygame.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game ny Akoto Tech')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 30

font_style = pygame.font.SysFont(None, 30)

def messages m(sg, color):
    mesg = font_style.remdr_style(msg.True, color)
    dis.blit(mesg, [dis_width /  3, dis_height_ / 3])

def gamLoop:    
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_heihgt / 2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    while not game_over:
    
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q (to QUIT) or C (to PLAY AGAIN)", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                if event.key == pygame.K_c:
                    gameLoop()

         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 game_over = True
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_LEFT:
                     x1_change = -snake_block
                     y1_change = 0
                 elif event.key == pygame.K_RIGHT:
                     x1_change = snake_block
                     y1_change = 0
                 elif event.key == pygame.K_UP:
                     y1_change = -snake_block
                     x1_change = 0
                 elif event.key == pygame.K_DOWN:
                     y1_change = snake_block
                     x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [foodx, foody, snake_block, snake_block])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
```

When you test this code you will find that the snake's food will stay at the same place even after your snake has eaten it *(travelled across the square)*.  In the next session we will look at how we can extend the the snake and move it to a different part of the screen.
