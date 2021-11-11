import sys
import pygame

# Initialize the game
pygame.init()

# Define parameters for rectangle
x=250
y=250
width=20
height=30
velocity = 3

# Define parameters for Line
start_pos_x = 250
start_pos_y = 100
end_pos_x = 250
end_pos_y = 450
linewidth = 5

# Start the main game loop
while True:
    # Create a game window of width * height
    game_window = pygame.display.set_mode((500,500))
    # print(game_window)

    # Game Window header
    pygame.display.set_caption(" First Game ")

    # To quit game on clicking close 'x' sign
    for event in pygame.event.get():
        # print(event.type)
        if event.type == pygame.QUIT:
            print("Inside....")
            sys.exit()

    # Configuring the movement of the object on screen
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x = x - velocity
        start_pos_x = start_pos_x + velocity
    if keys[pygame.K_RIGHT]:
        x = x + velocity
        start_pos_x = start_pos_x - velocity
    if keys[pygame.K_UP]:
        y = y - velocity
        end_pos_y = end_pos_y + velocity
    if keys[pygame.K_DOWN]:
        y = y + velocity
        end_pos_y = end_pos_y - velocity

    #game_window.fill((0,0,0))


    # Drawing rectangle on surface with the required parameters
    pygame.draw.rect(game_window,(0,255,0),(x,y,width,height))

    # Drawing Line on surface with the required parameters
    pygame.draw.line(game_window,(255,0,0),(start_pos_x,start_pos_y),(end_pos_x,end_pos_y),linewidth)

    # Refresh the surface display : IMP
    pygame.display.update()