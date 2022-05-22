## Making The Snake Move ##

To make the snake move we will have to use the `KEYDOWN` class of PyGame.
We will use `K_LEFT`, `K_RIGHT`, `K_UP` and `K_DOWN` to make the snake move left, right, up and down respectively.
We have also chnaged the default of the screen colour from black to white using the `fill()` method.

The variables `x1_change` and `y1_change` have been created in order to hold the updating values of the x and y coordinates.

**Code to move the snake and chnage the background colour:**
```
import pygame 

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake game by Akoto Tech')

game_over = False

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
```
What we are doing here is everytime the user moves the snake, we update the x & y coordinates.

Let's take a closer look at:
```
x1 += x1_change
y1 += y1_change
```
Because we have set the original `x1` and `y1` coordinates to `300`, to update them everytime the snake moves the `x1_change` & `y1_change` values are either added or subtracted to the `x1` & `y1` values.
So `x1 += x1_change` is basically saying **add or subtract** whatever the value `x1_change` is to/from the `x1` value.  The same principle at the line below for `y1`.
