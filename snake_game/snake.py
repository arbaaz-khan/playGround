import pygame
from random import randint

SCORE = 0
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
UNIT = 40
SPEED = 5
DIRECTION = 0
MOVEMENT = 0
SNAKE_COLOR = (0, 0, 0)
APPLE_COLOR = (255, 0, 0)
# Initialize pygame.
pygame.init()
# Initialize screen.
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_WIDTH))
# Load grass background image.
grassImage = pygame.image.load(r'C:\Users\Arbaaz\PycharmProjects\test\resources\grass.jpg')
grassImage = pygame.transform.scale(grassImage, (800, 800))
# Load apple image.
appleImage = pygame.image.load(r'C:\Users\Arbaaz\PycharmProjects\test\resources\apple.png')
appleImage = pygame.transform.scale(appleImage, (UNIT, UNIT))
# Load snake image.
snakeImage = pygame.image.load(r'C:\Users\Arbaaz\PycharmProjects\test\resources\snake_body.png')
snakeImage = pygame.transform.scale(snakeImage, (UNIT, UNIT))
# gameOver tracks the status of the game.
gameOver = False
# clock ensures that the frame rate of our game is controller and independent of system, & it's used for speeding up snake.
clock = pygame.time.Clock()

# Snake class contains all the members and functions related to the snake.
class Snake:

    def __init__(self):
        self.body = [[0, 0]]

    # Updates of position of the snake when it moves.
    def move(self, direction):
        if direction == 1: # UP
            self.body[0][1] -= UNIT
        elif direction == 2: # DOWN
            self.body[0][1] += UNIT
        elif direction == 3: # LEFT
            self.body[0][0] -= UNIT
        elif direction == 4: # RIGHT
            self.body[0][0] += UNIT

    # Updates the size of the snake when it eats apple.
    # TODO: currently the new body part is added in the tail and it's position is decided according to direction where the snake is headed.
    def grow(self):
        if DIRECTION == 1:
            self.body.append([self.body[-1][0], self.body[-1][1] + UNIT])
        elif DIRECTION == 2:
            self.body.append([self.body[-1][0], self.body[-1][1] - UNIT])
        elif DIRECTION == 3:
            self.body.append([self.body[-1][0] + UNIT, self.body[-1][1]])
        elif DIRECTION == 4:
            self.body.append([self.body[-1][0] - UNIT, self.body[-1][1]])

    # Draws the snake on the canvas.
    def drawSnake(self):
        for part in range(len(self.body)):
            screen.blit(snakeImage, (self.body[part][0], self.body[part][1]))

# Apple holds all the properties of the apple.
class Apple:
    def __init__(self):
        self.x = randint(0,SCREEN_WIDTH/UNIT) * UNIT
        self.y = randint(0,SCREEN_HEIGHT/UNIT) * UNIT
        self.alive = False

    # appear makes the apple appear on the canvas.
    def appear(self):
        if not self.alive:
            self.x = randint(1,SCREEN_WIDTH/UNIT) * UNIT - UNIT
            self.y = randint(1,SCREEN_HEIGHT/UNIT) * UNIT - UNIT
            #pygame.draw.rect(screen, APPLE_COLOR, pygame.Rect(self.x, self.y, UNIT, UNIT))
            screen.blit(appleImage, (self.x, self.y))
            self.alive = True
        else:
            #pygame.draw.rect(screen, APPLE_COLOR, pygame.Rect(self.x, self.y, UNIT, UNIT))
            screen.blit(appleImage, (self.x, self.y))

# snake object created.
snake = Snake()
# apple object created.
apple = Apple()
# The game runs until the snake collides with the wall.
# TODO: Need to add game over screen and all rules of game over that a normal snake game has.
while not gameOver:
    # display grass on the canvas.
    screen.blit(grassImage, (0, 0))
    # display apple if eaten.
    apple.appear()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                DIRECTION = 1 #UP
                MOVEMENT = -UNIT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                DIRECTION = 2 #DOWN
                MOVEMENT = UNIT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                DIRECTION = 3 #LEFT
                MOVEMENT = -UNIT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                DIRECTION = 4 #RIGHT
                MOVEMENT = UNIT
    if DIRECTION == 1 or DIRECTION == 2:
        L = [snake.body[0][0], snake.body[0][1] + MOVEMENT]
        snake.body.insert(0,L)
        snake.body = snake.body[:-1]
    elif DIRECTION == 3 or DIRECTION == 4:
        L = [snake.body[0][0] + MOVEMENT, snake.body[0][1]]
        snake.body.insert(0, L)
        snake.body = snake.body[:-1]
    if snake.body[0][0] == apple.x and snake.body[0][1] == apple.y:
        SCORE += 10
        snake.grow()
        apple.alive = False
    # Speed is increased with the score.
    SPEED = (SCORE//50)*5 + 5
    # Check game over conditions.
    if snake.body[0][0] < 0 or snake.body[0][0] > SCREEN_WIDTH-UNIT or snake.body[0][1] < 0 or snake.body[0][1] > SCREEN_WIDTH-UNIT:
        gameOver = True
    # Draw the snake.
    snake.drawSnake()
    # Update canvas.
    pygame.display.flip()
    # Update speed(Frame speed).
    clock.tick(SPEED)

# Once game is over, print score.
print("YOUR SCORE: ", SCORE)