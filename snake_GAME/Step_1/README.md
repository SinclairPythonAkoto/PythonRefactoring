## Creating A Screen ##

We will create a screen in order for the user to be able to play the game.

**Code to create a screen:**
```
import pygame

pygame.init()

dis = pygame.display.set_mode((400,300))
pygame.display.update()

pygame.quit()
quit()
```

In order to keep the window screen open, we have to create a while loop otherwise the screen will close immediately after it opens.
***We place the while loop just above*** `pygame.quit()`.

As you can see, in the terminal, the x & y coordinates along with the mouse buttons are printed everytime the mouse is moved.
You will also notice that you cannot close the screen when you press the **X** at the top of the right corner of the screen.  So if you are at this stage and would liek to close, you would have to press `ctrl` + `C` in the terminal.

**Code to display screen, prevent it from closing and display a screen title:**
```
import pygame

pygame.init()

dis = pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Snake game by Akoto Tech')

game_over = False

while not game_over:
    for event in pygame.event.get():
        print(event)

pygame.quit()
quit()
```
**To quit the game in the termianl press:** `cntrl` + `C`

For the screen to close when we click on the `X` at the top right hand side of the screen, we will need to specify that the screen should exit when the button is pressed.  To do this we have to specify the PyGame event to `QUIT`.

**Code to display screen, display the game title and allow the screen to close once exit button is pressed:**
```
import pygame

pygame.init()

dis = pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Snake game by Akoto Tech')

game_over = False

While not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()
quit()
```

Once we have done this, we have built a screen with a title of the game, and will allow the user to exit the screen once the `X` button has been pressed.
