## Creating A Snake ##

We need to create colour variables for the snake and the food that the snake will eat. 
We will use the **RGB colour scheme** *(Red, Green, Blue)*.  If all the RGB values are set to 0 then the colour will be black.  If all the values are set to 255 then the colour will be set to white.
The shape of the snake will be a rectagle, so in order to create a rectangle with PyGame we will use the `draw.rect()` function.
With the `draw.rect()` we can assign the rectangle any colour we want. 
```
import pygame

pygame.init()

dis = pygame.display.set_mode((400,300))
pygame.display.set_caption('Snake game by Akoto Tech')

blue = (0,0,255)
red = (255,0,0)

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.draw.rect(dis,blue,[200,150,10,10])
    pygame.display.update()

pygame.quit()
quit()
```

#### RGB Colours ####
In case you would like to chnage the colour of your snake here are some more RGB colours to choose from:
- **Red:** (255, 0, 0)
- **Green:** (0, 128, 0)
- **Blue:** (0, 0, 255)
- **Yellow:** (255, 255, 0)
- **Purple:** (128, 0, 128)
- **Pink:** (255, 192, 203)
- **Orange:** (255, 165, 0)
- **Grey:** (128, 128, 128)
- **Brown:** (153, 102, 51)

***The next step after creating the snake is getting it to move.***
