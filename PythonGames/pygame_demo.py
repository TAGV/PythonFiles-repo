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
start_pos_x = 500
start_pos_y = 0
end_pos_x = 500
end_pos_y = 500
linewidth = 5

jump_count = 10
# Start the main game loop
while True:
    # Create a game window of width * height
    game_window = pygame.display.set_mode((1000,500))
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
    width_screen = (pygame.display.get_window_size()[0])
    height_screen = (pygame.display.get_window_size()[1])

    if keys[pygame.K_LEFT]:
        print(x)
        if x > 0:
            x = x - velocity
        else:
            x = width_screen
            x = x - velocity
        #start_pos_x = start_pos_x + velocity
    if keys[pygame.K_RIGHT]:
        print(x)
        if x < (width_screen-20):
            x = x + velocity
        else:
            x = 0
            x = x + velocity
        #start_pos_x = start_pos_x - velocity
    if keys[pygame.K_UP]:
        print(y)
        if y > 0:
            y = y - velocity
        else:
            y = height_screen
            y = y - velocity
        #end_pos_y = end_pos_y + velocity
    if keys[pygame.K_DOWN]:
        print(y)
        if y < (height_screen-20):
            y = y + velocity
        else:
            y = 0
            y = y + velocity
        #end_pos_y = end_pos_y - velocity
    if keys[pygame.K_SPACE]:    #Jumping logic needs to be revised further
        if jump_count >= -10:
            negative_count = 1
            if jump_count < 0:
                negative_count = -1
            y = y - ((jump_count ** 2) * 0.5 * negative_count)
            jump_count = jump_count - 1
        else:
            jump_count = 10
    #game_window.fill((0,0,0))


    # Drawing rectangle on surface with the required parameters
    pygame.draw.rect(game_window,(0,255,0),(x,y,width,height))

    # Drawing Line on surface with the required parameters
    pygame.draw.line(game_window,(255,0,0),(start_pos_x,start_pos_y),(end_pos_x,end_pos_y),linewidth)

    # Refresh the surface display : IMP
    pygame.display.update()