import pygame, time, random
from pygame.locals import *

#library pytmx imported
from pytmx.util_pygame import load_pygame

#user define function 
#tasks: to render the map in pygame window
def blit_my_map(window, tmxdata, world_offset):    
    
        #tile[0] -> x grid location
            #tile[1] -> y grid location
            #(x,y) -> position of the tile in the map
            #tile[2] -> image of the tile

    #render first layer has index of 0
    for tile in tmxdata.layers[0].tiles():
        img = pygame.transform.scale(tile[2], (35, 35))
        x_pixel = tile[0] * 35 + world_offset[0]
        y_pixel = tile[1] * 35 + world_offset[1]

        window.blit(img, (x_pixel, y_pixel) )



    # #render both layer
    # for layer in tmxdata:
    #     for tile in layer.tiles():
            
    

    #render both layer
    
            
def get_my_tiles_properties(tmxdata, x, y, world_offset):
    world_x = x - world_offset[0] #particular assets or tile
    world_y = y - world_offset[1]

    tile_x = world_x // 35
    tile_y = world_y // 35


    try:
        properties = tmxdata.get_tile_properties(tile_x, tile_y, 0)


    except ValueError:
        properties = {'id': -1, "climbable": False, "ground": False, "health": -999999, "points": 0,
        "provide": '', "require": "", "solid": False}


    #if player is not moving in the map (moving in a free space)
    if properties is None:
        properties = {'id': -1, "climbable": False, "ground": False, "health": 0, "points": 0,
        "provide": '', "require": "", "solid": False}


    #position of the tile
    properties['x'] = tile_x
    properties['y'] = tile_y
    return properties

#main logic
def main():
    #********** Game variables **********

    font = pygame.font.SysFont("Arial", 20)

    world_offset = [0, 0] #which part of the map to show to the player

    collected_items = [] #to check what player has collected

   #this music is running continuously
    # pygame.mixer.music.load("sounds/intro game.wav")

    # pygame.mixer.music.play(-1) #tells us to loop continuously


    #coin, jump and injury is played conditionally
    coin_sfx = pygame.mixer.Sound("sounds/coin.wav")

    jump_sfx = pygame.mixer.Sound("sounds/jump.wav")
    injury_sfx = pygame.mixer.Sound("sounds/injury.wav")



    tmx_data = load_pygame("my_map.tmx")

    window.fill((0, 0, 0)) #reset my window screen back to black color
    

    y_ground = window.get_height() - 350

    quit = False
    x = 50
    y = y_ground

    #logistics for the game
    health = 10 #full health is given intially
    points = 0 


    #LOAD SINGLE IMAGE FOR STANDING STILL
    player_stand = pygame.image.load("assets/p1_stand.png").convert_alpha()

    player_stand = pygame.transform.scale(player_stand, (50, 70))


    #image loaded in player_right list
    player_right = [

            pygame.image.load("assets//p1_walk/PNG//p1_walk01.png").convert_alpha(),
            pygame.image.load("assets//p1_walk/PNG//p1_walk02.png").convert_alpha(),
            pygame.image.load("assets//p1_walk/PNG//p1_walk03.png").convert_alpha(),
            pygame.image.load("assets//p1_walk/PNG//p1_walk04.png").convert_alpha(),
            pygame.image.load("assets//p1_walk/PNG//p1_walk05.png").convert_alpha(),
            pygame.image.load("assets//p1_walk/PNG//p1_walk06.png").convert_alpha(),
            pygame.image.load("assets//p1_walk/PNG//p1_walk07.png").convert_alpha(),
            pygame.image.load("assets//p1_walk/PNG//p1_walk08.png").convert_alpha(),
            pygame.image.load("assets//p1_walk/PNG//p1_walk09.png").convert_alpha(),
            pygame.image.load("assets//p1_walk/PNG//p1_walk10.png").convert_alpha(),
            pygame.image.load("assets//p1_walk/PNG//p1_walk11.png").convert_alpha()

    ]

    #LC to scale images
    player_right = [ pygame.transform.scale(image, (50, 70)) 
    for image in player_right] #DRY 


    player_right_frame = 0 #index tracker of the list

    #logistic for player facing towards left
    
    player_left = [pygame.transform.flip(image, True, False)   
                   for image in player_right ]

    player_left_frame = 0



    #load image to jump
    player_jump = pygame.image.load("assets/p1_jump.png").convert_alpha()

    player_jump = pygame.transform.scale(player_jump, (50, 70))

    player_jump_frame = 0


    #player landing image
    player_land = pygame.image.load("assets/p1_duck.png").convert_alpha()
    player_land = pygame.transform.scale(player_land, (50, 70))


    direction = "stand" #current positionof player image

    #********** Start game loop ********** 
    while not quit:
        window.fill((0,0,0))                            # Reset screen to black
        #********** Process events **********

        blit_my_map(window, tmx_data, world_offset) #blit part of map

        points_image = font.render(f"Points: {points}", 1, (255, 255, 255))
        health_image = font.render(f"Health: {health}", 1, (255, 255, 255))

        window.blit(points_image, (50, 10) )
        window.blit(health_image, (50, 30))


        keyspressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True

        #when player moves from right to left
        if keyspressed[ord('a')]: 
            left_tile = get_my_tiles_properties(tmx_data, x-10, y + 35, world_offset)

            if not left_tile['solid']:
                #MOVE LEFT
                x = x - 10
                direction = "left"
           

        #when player moves from left to right
        if keyspressed[ord("d")]:

            right_tile = get_my_tiles_properties(tmx_data, x+50+10, y+35, world_offset)

            if not right_tile['solid']:
                #MOVE RIGHT
                x = x + 10
                direction = "right"

        #important 

        standing_on = get_my_tiles_properties(tmx_data, x + 25, y+ 70, world_offset )
        # print(standing_on)

        
        #collision handling
        touching =  get_my_tiles_properties(tmx_data, x+50, y, world_offset)

        health = health + touching['health']
        points = points + touching['points']

        if touching['health'] < 0:
            injury_sfx.play()




        tile_x = touching['x']
        tile_y = touching['y']
        #collect coin and reduce health 


        if health <= 0:
            quit = True


        #touching the coin
        if touching['id'] == 55:
            coin_sfx.play()
            #above is position of touched coin
            tmx_data.layers[0].data[tile_y][tile_x] = 0 #to remove coins after it is collected by the player


        #for lock and keys achievements
        touching_locks_keys = \
        get_my_tiles_properties(tmx_data, x + 25, y + 30, world_offset )

        #collect the items green key after touching it
        if touching_locks_keys['provide'] != "":
            collected_items.append(touching_locks_keys['provide'])

        #green lock is touched by player
        if touching_locks_keys['require'] != "":
            if touching_locks_keys['require'] in collected_items:
                #unlock of the door
                item = touching_locks_keys['require']
                if item == "green key":
                    #finally unlock the door
                    #override the door from tile layer 2 into tile layer 1

                    tmx_data.layers[0].data[33][66] = tmx_data.layers[1].data[33][66]
                    tmx_data.layers[0].data[34][66] = tmx_data.layers[1].data[34][66]


      #when player moves from down to up
        if keyspressed[ord("w")]:

            above_tile = get_my_tiles_properties(tmx_data, x+10, y - 7, world_offset )


            if standing_on['climbable'] == True:
                y = y - 10 #moving upward


            #we allow player to jump only when player is at ground
             #power of jump
            # y = y - 10
            # direction = "jump"
            if not above_tile['solid']:
                if standing_on['ground'] == True:
                    player_jump_frame = 10
                    y = y - 10
                    jump_sfx.play()
                    direction = "jump"
            
            else:
                player_jump_frame = 0
                #hit to the upper tile and fall completely down

        if keyspressed[ord("s")]:
            if standing_on['climbable']:
                y = y + 10


        #checking if no keys from keyboard is pressed
        if sum(keyspressed) == 0: 
            direction = "stand"

        #checking whether there is jump:

        #PROGRESS ON JUMPING
        if player_jump_frame > 0:
            y = y - 10
            direction = "jump"
            player_jump_frame = player_jump_frame - 1 #when player falls
            # player_jump_frame -= player_jump_frame


        #PROGRESS ON FALLING/LANDING
        elif standing_on['ground'] == False and standing_on['climbable'] == False: 
            direction = "landing"
            y = y + 10

 

        #check if my player is inside boundary
        if y < 210:
            y = 210
            world_offset[1] += 10


        if y > y_ground:
            y = y_ground
            world_offset[1] -= 10

        #to restrict player to not cross left and right boundary

        if x < 180:
            x = 180
            world_offset[0] += 10

        if x > window.get_width()-180 - 25:
            x = window.get_width()-180 - 25
            world_offset[0] -= 10

        #********** Your game logic here **********
        # player = Rect(x, y, 50, 50)
        # pygame.draw.rect(window, (204, 0, 255), player )

        #Draw player based on direction variable

        if (direction == "left"):

            window.blit(player_left[player_left_frame], (x,y))
            player_right_frame = (player_left_frame + 1) % len(player_left)
            

        elif direction == "right":
            window.blit(player_right[player_right_frame], (x,y))
            player_right_frame = (player_right_frame + 1) % len(player_right)

        elif direction == "jump":
            window.blit(player_jump, (x,y))

        elif direction == "landing":
            window.blit(player_land, (x,y))

        else: 
            window.blit(player_stand, (x,y))    
        
        #********** Update screen **********
        pygame.display.update()                        # Actually does the screen update
        clock.tick(15)                                 # run game at 30 frame per second
                            
#********** Initialise & run the game **********
if __name__ == "__main__":
    width, height = 800, 600                            # Set screen width,height
    pygame.init()                                       # Start graphics system
    pygame.mixer.init()                                 # Start audio system
    window = pygame.display.set_mode((width, height))   # Create window
    clock = pygame.time.Clock()                         # Create game clock
    main()
    pygame.quit()