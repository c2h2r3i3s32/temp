import pygame
import random

clock = pygame.time.Clock()
height = 600
width = 800
blue = (200, 255, 255)
yellow = (255, 255, 150)
grey = (128, 128, 128)
white = (255, 255, 255)
purple = (255, 100, 255)
red = (255, 0, 0)
dark_blue = (0, 150, 255)
orange = (255, 165, 0)
pink = (255, 200, 255)
green = (130, 255, 0)
black = (0, 0, 0)
point = 0
pygame.init()
colour_list = ['red', 'orange', 'green', 'dark_blue', 'grey', 'black', 'pink', 'white', 'purple']
Text_colour_list = [red, orange, green, dark_blue, grey, black, pink, white, purple]
colour = random.choice(colour_list)
text_colour = random.choice(Text_colour_list)
chosen_colour = random.choice(Text_colour_list)
t1 = random.choice(Text_colour_list)
t2 = random.choice(Text_colour_list)
t3 = random.choice(Text_colour_list)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Click game')
screen.fill(blue)
pygame.display.flip()

def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)

def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))

def main_loop():
    global point
    global colour
    global text_colour
    global chosen_colour
    global t1
    global t2
    global t3
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                if 150 <= mopos[0] <= 250 and 250 <= mopos[1] <= 400:
                    if t1 == chosen_colour:
                        point = point + 1
                        t1 = random.choice(Text_colour_list)
                        t2 = random.choice(Text_colour_list)
                        t3 = random.choice(Text_colour_list)
                        chosen_colour = random.choice(Text_colour_list)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                if 350 <= mopos[0] <= 450 and 250 <= mopos[1] <= 400:
                    if t2 == chosen_colour:
                        t1 = random.choice(Text_colour_list)
                        t2 = random.choice(Text_colour_list)
                        t3 = random.choice(Text_colour_list)
                        chosen_colour = random.choice(Text_colour_list)
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                if 550 <= mopos[0] <= 650 and 250 <= mopos[1] <= 400:
                    if t3 == chosen_colour:
                        t1 = random.choice(Text_colour_list)
                        t2 = random.choice(Text_colour_list)
                        t3 = random.choice(Text_colour_list)
                        chosen_colour = random.choice(Text_colour_list)
                    

        if t1 == t2:
            t1 = random.choice(Text_colour_list)

        if t2 == t3:
            t2 = random.choice(Text_colour_list)

        if t3 == t1:
            t3 = random.choice(Text_colour_list)

        if chosen_colour != t1 and t2 and t3:
            t1 = random.choice(Text_colour_list)
            t2 = random.choice(Text_colour_list)
            t3 = random.choice(Text_colour_list)

        DrawText("Click", black, blue, 400, 100, 50)
        DrawText(colour, chosen_colour, blue, 400, 175, 50)
        DrawText("you have " + (f'{point:.2f}') + " point", black, blue, 100, 20, 20)
        rectangle(screen, t1, 150, 250, 100, 150)
        rectangle(screen, t2, 350, 250, 100, 150)
        rectangle(screen, t3, 550, 250, 100, 150)
        pygame.display.update()
        clock.tick(60)


main_loop()
pygame.quit()
quit()
