import pygame
import random

# initialize pygame modules
pygame.init()

# create screen display
screen = pygame.display.set_mode((500, 750))

# background image
backgroundImage = pygame.image.load('farmbackground.jpg')

# pig
pigImage = pygame.image.load('piggy.png')
# remove white background
pigImage.set_colorkey((255, 255, 255))
pig_x = 50
pig_y = 300
pig_width = 80
pig_height = 77
pig_y_change = 0

# function to display the pig
def displayPig(x, y):
    screen.blit(pigImage, (x, y))

# pipes
pipeWidth = 70
# gap between top and bottom pipes
pipeGap = 150  
pipe_x_change = -0.1
pipe_x = 500

# Function to generate random pipe heights
def generatePipeHeights():
    top_height = random.randint(150, 450)
    bottom_height = 750 - top_height - pipeGap
    return top_height, bottom_height

topPipeHeight, bottomPipeHeight = generatePipeHeights()

# function to display both top and bottom pipes
def displayPipes(top_height, bottom_height):
    pipeColor = (255,105,180)
    pygame.draw.rect(screen, pipeColor, (pipe_x, 0, pipeWidth, top_height))
    pygame.draw.rect(screen, pipeColor, (pipe_x, 750 - bottom_height, pipeWidth, bottom_height))

# function to detect if the pig touches the pipes
def pipeTouch(pipe_x, top_height, pig_x, pig_y, bottom_height):
    if (pipe_x <= pig_x + pig_width and pipe_x + pipeWidth >= pig_x) and \
            (pig_y <= top_height or pig_y + pig_height >= 750 - bottom_height):
        return True
    return False

# score
score = 0
scoreFont = pygame.font.SysFont('arial', 32)

def displayScore(score):
    scoreDisplay = scoreFont.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(scoreDisplay, (10, 10))

running = True
while running:
    # display farm background
    screen.blit(backgroundImage, (0, 0))

    for event in pygame.event.get():
        # if player pressed X button, quit pygame
        if event.type == pygame.QUIT:
            running = False

        # if space bar is pressed, the pig goes up
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pig_y_change = -0.2 

        # if space bar is released, the pig moves down
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                pig_y_change = 0.1

    # let pig move
    pig_y += pig_y_change

    # conditions so pig stays in the screen
    if pig_y <= 0:
        pig_y = 0
    if pig_y >= 670:
        pig_y = 670

    # let pipes move
    pipe_x += pipe_x_change

    # make a new pair of pipes when the current ones leave the screen
    if pipe_x <= -pipeWidth:
        pipe_x = 500
        topPipeHeight, bottomPipeHeight = generatePipeHeights()
        # increase score when pig goes through the gap between the pipes
        score += 1

    displayPipes(topPipeHeight, bottomPipeHeight)

    # if pig touches pipes, quit the game
    if (pipe_x <= pig_x + pig_width and pipe_x + pipeWidth >= pig_x) and \
            (pig_y <= topPipeHeight or pig_y >= 750 - bottomPipeHeight):
        running = False 

    displayPig(pig_x, pig_y)

    # display score
    displayScore(score)

    # update the display after each iteration
    pygame.display.update()

# quit pygame
pygame.quit()
