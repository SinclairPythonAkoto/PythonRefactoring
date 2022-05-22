## Game Over When The Snake Hits The Boundaries ##

We want to creat a boundary for when the snake hits the end of the screen th euser looses.
To do this we will create an *if statement* that defines the limits of the x & y coordinates - so if the snake goes beyond this then the script will recognise ths and end the game.
We will also produce a message to the user telling them they have lost.

In this section we will also remove the *hardcodes* and used variables instead so that it will become easier to chnage some aspects if you choose to do so at any point in the future. 

**Code to create a game over:**
```
import pygame
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game by Akoto Tech')

game_over = False

x1 = dis_width / 2
y1 = dis_height / 2

snake_block = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2, dis_height / 2])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
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
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
    
    pygame.display.update()

    clock.tick(snake_speed)

message("You lost", red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()
```
To get the snake in the middle of the scren notice how we have divided the *display width* and the *display height* by `2`.
```
x1 = dis_width / 2
y1 = dis_height / 2
```
Also notice how we have created the variable `snake_block`. This enables us to chnage the size of the snake blocks as we please, and also control the movement of the snake when the direction keys are pressed.

***You can also adjust the speed of the snake with*** `snake_speed`.
***For my code I have slowed down the speed for the snake.***
