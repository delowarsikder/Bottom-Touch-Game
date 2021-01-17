import os.path
import pygame
from pygame import *
from pygame.locals import *
from time import *
from random import *
from sys import exit
import math
from pygame.mixer import *
import unittest

# initiation the game
pygame.init()

# Initialize Basic constant
DISPLAY_HEIGHT = 480
DISPLAY_WIDTH = 640
DANGER_LINE = 0.04*DISPLAY_HEIGHT
SCREEN_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

'''
image and music load
'''
background_image_filename = 'assets/background.png'
bounce_ball_image_filename = 'assets/football.png'
bottom_bar_image_filename = 'assets/bar.png'
filepath = os.path.dirname(__file__)


def image_load(image):
    return pygame.image.load(os.path.join(filepath, image))


def music_load(music):
    return mixer.music.load(os.path.join(filepath, music))


def sound_load(sound):
    return pygame.mixer.Sound(os.path.join(filepath, sound))


# game image
background_img = image_load(background_image_filename).convert()
bounce_ball = image_load(bounce_ball_image_filename).convert_alpha()
bottom_bar = image_load(bottom_bar_image_filename).convert_alpha()

# caption & icon
pygame.display.set_caption('Bounce Ball')
pygame.display.set_icon(bounce_ball)

# Sound
background_music_file = 'assets/background.wav'
collision_sound_file = "assets/laser.wav"
over_sound_file = "assets/explosion.wav"
music_load(background_music_file)
mixer.music.play(-1)


# speed control
clock = pygame.time.Clock()
BALL_X, BALL_Y = randint(0, DISPLAY_WIDTH), 0
PLAYER_X, PLAYER_Y = (DISPLAY_WIDTH-bottom_bar.get_width()) / \
    2, (DISPLAY_HEIGHT-DANGER_LINE-bottom_bar.get_height())

speed_x, speed_y = DISPLAY_WIDTH/5., DISPLAY_HEIGHT/5.
#control game speed
game_speed_increase=5
# bar sprit controlling
move_bar_stepX = 0
# color
white_color = (255, 255, 255)
red_color = (255, 0, 0)
black_color = (0, 0, 0)
green_color = (0, 255, 0)
blue_color = (0, 0, 255)
yellow_color = (255, 255, 0)
cyan_color = (200, 100, 255)
random_color = (randint(0, 255), randint(0, 255), randint(0, 255))

# store score
score = 0
scorePosition = (10, 10)

# font
font = pygame.font.get_fonts()
score_font = pygame.font.SysFont(font[5], 32)
game_over_font = pygame.font.SysFont(font[1], 64)
developer_font = pygame.font.SysFont(font[20], 22)
pause_font = pygame.font.SysFont(font[12], 36)
small_font = pygame.font.SysFont("comicsansms", 20)
mid_font = pygame.font.SysFont("comicsansms", 30)
large_font = pygame.font.SysFont("comicsansms", 50)
myself_font = pygame.font.Font('freesansbold.ttf', 20)
message_font = pygame.font.SysFont(font[28], 32)

# display score


def display_score():
    score_text = score_font.render(
        'Score : '+str(score), True, (255, 255, 255), None)
    screen.blit(score_text, scorePosition)


"""# Game Over
def gameOver():
    over_text = game_over_font.render('GAME OVER', True, (200, 10, 90), None)
    screen.blit(over_text, (int(DISPLAY_WIDTH/5), int(DISPLAY_HEIGHT/3)))
"""
# show speed up text


def show_speed_up_text():
    global DISPLAY_HEIGHT, DISPLAY_WIDTH
    x, y = DISPLAY_WIDTH/3, DISPLAY_HEIGHT/3
    speed_text = game_over_font.render(
        'Speed Up !!!', True, (200, 10, 90), None)
    while(y != 0):
        screen.blit((background_img),(0,0))
        screen.blit(speed_text, (x, y))
        y = y-10

# check boundary


def check_boundary(x):
    if x < 0:
        x = 0
    elif(x > (DISPLAY_WIDTH-bottom_bar.get_width())):
        x = DISPLAY_WIDTH-bottom_bar.get_width()
    return x


# # #draw circle


def draw_cicle(x, y):
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    radius = 20
    return pygame.draw.circle(screen, color, (x, y), radius)


# check collision
ball_radius = int(bounce_ball.get_height()/2)
bar_width = int(bottom_bar.get_width())


def check_collison(barX, barY, ballX, ballY):
    ballX = int(ballX+ball_radius)
    ballY = int(ballY+ball_radius)
    # math.isclose(barY,ballY):
    if ballX >= int(barX) and ballX <= int(barX+bar_width) and abs(barY-ballY) < ball_radius:
        return True
    else:
        return False


mySelf = 'Designed and Developed by : Delowar Sikder CSE 2K16 KUET'

# # # all message


def screen_message(message, x, y, txt_font, color=red_color):
    text = txt_font.render(message, True, color, None)
    screen.blit(text, (int(x), int(y)))


# How to play Game
welcome_txt = 'Protect the Ball from touching the Line'
instruction_txt = 'Game Instructions : '
start_txt = '1.Press S or s to start game'
pause_txt = '2.Press SPACE to pause & unpause game'
right_txt = '3.Press right arrow to move bar into right'
left_txt = '4.Press left arrow to move bar into left'
quit_txt = '5.Press q or Esc to quit game from any state'
point_txt = '6.When Ball Touch the White Bar increase point'
end_txt = '7.When Ball Touch the Red Line Game Over'
again_play_txt = '8.After Game over Press C or c to play agin'
speed_up_text = '9.Speed will increase after every '+str(game_speed_increase)+' points'

startText_X, startText_Y = 0, 0


def game_instruction():
    intro = True

    while intro:
       # show instruction in initial state
        # screen.fill(white_color)
        screen.blit((background_img), (0, 0))
        # message_show(txt,x,y,font,color)
        screen_message(welcome_txt,
                       startText_X+10, startText_Y+5, message_font, yellow_color)
        screen_message(instruction_txt,
                       startText_X+10, startText_Y+35, large_font, red_color)
        screen_message(start_txt,
                       startText_X+10, startText_Y+80, mid_font, white_color)
        screen_message(pause_txt,
                       startText_X+10, startText_Y+110, mid_font, yellow_color)
        screen_message(right_txt,
                       startText_X+10, startText_Y+140, mid_font, cyan_color)
        screen_message(left_txt,
                       startText_X+10, startText_Y+170, mid_font, white_color)
        screen_message(quit_txt,
                       startText_X+10, startText_Y+200, mid_font, red_color)
        screen_message(point_txt,
                       startText_X+10, startText_Y+230, mid_font, yellow_color)
        screen_message(end_txt,
                       startText_X+10, startText_Y+260, mid_font, red_color)
        screen_message(again_play_txt,
                       startText_X+10, startText_Y+290, mid_font, yellow_color)
        screen_message(speed_up_text,
                       startText_X+10, startText_Y+320, mid_font, cyan_color)
        screen_message(mySelf,
                       startText_X+10, DISPLAY_HEIGHT-50, myself_font, white_color)

        # handle event to start game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    intro = False
                if event.key == K_q:
                    pygame.quit()
                    exit()
                if event.key == K_s:
                    game_loop()

        pygame.display.flip()


# # control ball speed
ball_change_move = 12*1e-4

# # pause the game while running
pause = False

# control global variable

# start main game loop


def game_loop():
    # # # Initialize the global variable
    global BALL_X, BALL_Y, PLAYER_X, PLAYER_Y, move_bar_stepX, ball_change_move, score, speed_x, speed_y, pause,game_speed_increase
    # back all globar variable to initial state
    BALL_X, BALL_Y = randint(0, DISPLAY_WIDTH), 0
    PLAYER_X, PLAYER_Y = (DISPLAY_WIDTH-bottom_bar.get_width()) / \
        2, (DISPLAY_HEIGHT-DANGER_LINE-bottom_bar.get_height())
    score = 0
    ball_change_move = 12*1e-4
    # again play game
    game_over_state = False  # this variable for continue game after game over
    startGame = True
    running = True
    mixer.music.play(-1)
    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                    # # use for pause
                if event.key == K_SPACE:
                    if BALL_Y > (DISPLAY_HEIGHT-(DANGER_LINE+bounce_ball.get_height())):
                        startGame = False
                    else:
                        startGame = True
                        pause = False
                        mixer.music.play(-1)
        while startGame:
            screen.fill((black_color))
            screen.blit(background_img, (0, 0))
            # # control script move left or right
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        move_bar_stepX = -(8*DISPLAY_WIDTH)/1e4
                    elif event.key == K_RIGHT:
                        move_bar_stepX = (8*DISPLAY_WIDTH)/1e4
                        # pause the game
                    elif event.key == K_SPACE:
                        if not pause:
                            startGame = False
                            pause = not pause
                            mixer.music.pause()
                            screen_message('Press Space To Continue again !', DISPLAY_WIDTH/8,
                                           DISPLAY_HEIGHT/3, pause_font, yellow_color)

                elif event.type == KEYUP:
                    if event.key == K_LEFT:
                        move_bar_stepX = 0
                    elif event.key == K_RIGHT:
                        move_bar_stepX = 0

            # # load image in screen
            screen.blit(bounce_ball, (BALL_X, BALL_Y))
            # draw_cicle(int(BALL_X),int(BALL_Y))

            # # controlling game sprit
            PLAYER_X = PLAYER_X+move_bar_stepX
            PLAYER_X = check_boundary(PLAYER_X)
            screen.blit(bottom_bar, (PLAYER_X, PLAYER_Y))

            # # draw a red zone in bottom
            start_pos = (0, DISPLAY_HEIGHT-DANGER_LINE)
            rect_size = (DISPLAY_WIDTH, DANGER_LINE)
            pygame.draw.rect(screen, (red_color), Rect(start_pos, rect_size))

            # # # time_passed = clock.tick()
            # # # time_passed_seconds = time_passed / 1000.0
            # # # BALL_X += speed_x * time_passed_seconds
            # # # BALL_Y += speed_y * time_passed_seconds
            """speed up of ball movement"""
            if int(score) >= game_speed_increase:
                if int(score) % game_speed_increase == 0:
                    ball_change_move = ball_change_move+1e-7
                    # show_speed_up_text()

            BALL_X += speed_x * ball_change_move
            BALL_Y += speed_y * ball_change_move

            # # If the bounce_ball goes off the edge of the screen,
            # # make it move in the opposite direction
            if BALL_X > (DISPLAY_WIDTH - bounce_ball.get_width()):
                speed_x = speed_x/-1.
                BALL_X = DISPLAY_WIDTH - bounce_ball.get_width()
            elif BALL_X < 0:
                speed_x = speed_x/-1.
                BALL_X = 0.

            # control move according to collision
            # # check collision
            if check_collison(PLAYER_X, PLAYER_Y, BALL_X, BALL_Y):
                speed_y = speed_y/-1.
                BALL_Y = DISPLAY_HEIGHT - \
                    (DANGER_LINE+bottom_bar.get_height() + bounce_ball.get_height())
                score = score+1
                collision_sound = sound_load(collision_sound_file)
                collision_sound.play()

            else:
                if BALL_Y > (DISPLAY_HEIGHT-(DANGER_LINE+bounce_ball.get_height())):
                    overSound = sound_load(over_sound_file)
                    overSound.play()
                    mixer.music.pause()
                    # Game Over
                    startGame = False
                    game_over_state = True
                elif BALL_Y < 0:
                    speed_y = speed_y/-1.
                    BALL_Y = 0

            display_score()
            pygame.display.flip()

    # # # show this text after game over
        if game_over_state:
            screen.blit(background_img, (0, 0))
            screen_message('GAME OVER !!!', DISPLAY_WIDTH//6,
                           DISPLAY_HEIGHT//6, game_over_font, (200, 10, 90))

            screen_message('Score : '+str(score), 200,
                           160, score_font, white_color)

            screen_message('Do You want to play again !!!', 200,
                           200, developer_font, yellow_color)
            screen_message('Press C or c to Continue ...', 200,
                           230, developer_font, yellow_color)

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()

                    if event.key == K_c:
                        game_over_state = False
                        # # game_instruction() ##start from initial
                        game_loop()  # start from game state
        pygame.display.flip()


#game start here
game_instruction()
# # game_loop()
