from board import boards
import pygame
import math
pygame.init()
Width = 800
Height = 700
screen = pygame.display.set_mode([Width, Height])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
level = boards
color = 'blue'
PI = math.pi

player_imgs = []
for i in range(1, 5):
    player_imgs.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (30, 30)))

player_x = 400
player_y = 475
direction = 0
counter = 0
flicker = False
turns_allowed = [False, False, False, False]
def make_board():
    tile_height = ((Height - 50) // 32)
    tile_width = (Width // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * tile_width + (0.5 * tile_width), i * tile_height + (0.5 * tile_height)), 3)
            if level[i][j] == 2 and not flicker:
                pygame.draw.circle(screen, 'white', (j * tile_width + (0.5 * tile_width), i * tile_height + (0.5 * tile_height)), 7)
            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j * tile_width + (0.5 * tile_width), i * tile_height),
                                 (j * tile_width + (0.5 * tile_width), i * tile_height + tile_height), 2)
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * tile_width, i * tile_height + (0.5 * tile_height)),
                                 (j * tile_width + tile_width, i * tile_height + ( 0.5 * tile_height)), 2)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * tile_width - (tile_width * 0.4)) - 2, (i * tile_height + (0.5 * tile_height)), tile_width, tile_height], 0, PI/2, 2)
            if level[i][j] == 6:
                pygame.draw.arc(screen, color, [(j * tile_width + (tile_width * 0.5)), (i * tile_height + (0.5 * tile_height)), tile_width, tile_height], PI/2, PI, 2)
            if level[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * tile_width + (tile_width * 0.5)), (i * tile_height - (0.4 * tile_height)), tile_width, tile_height], PI, 3*PI/2, 2)
            if level[i][j] == 8:
                pygame.draw.arc(screen, color, [(j * tile_width - (tile_width * 0.4)) - 2, (i * tile_height - (0.4 * tile_height)), tile_width, tile_height], 3*PI/2, 2*PI, 2)
            if level[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * tile_width, i * tile_height + (0.5 * tile_height)),
                                 (j * tile_width + tile_width, i * tile_height + ( 0.5 * tile_height)), 2)

def make_player():
    if direction == 0:
        screen.blit(player_imgs[counter // 5], (player_x, player_y))
    elif direction == 1:
        screen.blit(pygame.transform.flip(player_imgs[counter // 5], True, False), (player_x, player_y))
    elif direction == 2:
        screen.blit(pygame.transform.rotate(player_imgs[counter // 5], 90), (player_x, player_y))
    elif direction == 3:
        screen.blit(pygame.transform.rotate(player_imgs[counter // 5], 270), (player_x, player_y))

def check_position(centerx, centery):

run = True
while run:
    timer.tick(fps)
    if counter < 19:
        counter += 1
        if counter > 3:
            flicker = False
    else:
        counter = 0
        flicker = True
    screen.fill('black')
    make_board()
    make_player()
    center_x = player_x + 16
    center_y = player_y + 16
    turns_allowed = check_position(center_x, center_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 0
            if event.key == pygame.K_LEFT:
                direction = 1
            if event.key == pygame.K_UP:
                direction = 2
            if event.key == pygame.K_DOWN:
                direction = 3

    pygame.display.flip()
pygame.quit()