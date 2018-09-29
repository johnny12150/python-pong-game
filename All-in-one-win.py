import pygame
import random
import time
from sys import exit
import pygameMenu  # This imports classes and other things
from pygameMenu.locals import *
import os

TimesCount = 0


def Solo(RUNNING):
    # while (RUNNING):
    # initialize pygame
    pygame.init()
    global TimesCount
    # color globals
    red = (255, 0, 0)
    orange = (255, 127, 0)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    violet = (127, 0, 255)
    brown = (102, 51, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)

    # screen globals
    screen_width = 800
    screen_height = 600
    game_screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tennis")
    font = pygame.font.SysFont("monospace", 50)

    # ball globals, xv, yv max is 20
    ball_x = int(screen_width / 2)
    ball_y = int(screen_height / 2)
    ball_xv = random.choice([5, -5])
    ball_yv = random.choice([5, -5])
    ball_r = 10
    rand1 = 50

    # pause
    pause = False
    TimesPause1 = 0
    TimesPause2 = 0

    # draw paddle 1
    paddle1_x = 10
    paddle1_y = int(screen_height / 2)
    paddle1_w = 10
    paddle1_h = 100
    paddle1_goal = 300

    # draw paddle 2
    paddle2_x = screen_width - 20
    paddle2_y = int(screen_height / 2)
    paddle2_w = 10
    paddle2_h = 100
    paddle2_goal = 300

    # initialize score
    player1_score = 0
    player2_score = 0

    # game loop
    pygame.mouse.set_visible(0)  # makes mouse invisible in game screen

    # while True:
    while (RUNNING):
        times = int(pygame.time.get_ticks() / 1000 - TimesCount)
        pressed = pygame.key.get_pressed()
        pygame.key.set_repeat()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            # if pressed[pygame.K_ESCAPE]:
            #     RUNNING = False
            #     menu.enable()
            #     print('menu')
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    RUNNING = False
                    menu.enable()
                if event.key == pygame.K_BACKSPACE and pause == False:
                    pause_xv = ball_xv
                    pause_yv = ball_yv
                    ball_xv = 0
                    ball_yv = 0
                    pause = True
                elif event.key == pygame.K_RETURN and pause == True:
                    ball_xv = pause_xv
                    ball_yv = pause_yv
                    pause = False
        if pressed[pygame.K_w] and pause == False:
            paddle1_y -= 15
        elif pressed[pygame.K_s] and pause == False:
            paddle1_y += 15

        # location of ball is updated
        ball_x += ball_xv
        ball_y += ball_yv

        # collision of ball with top/bottom of screen
        if ball_y - ball_r <= 5:
            ball_yv = abs(ball_yv)
        elif ball_y + ball_r >= 595:
            ball_yv = -abs(ball_yv)

        # collision of paddle with top/bottom of screen
        if paddle1_y < 10:
            paddle1_y = 10
        elif paddle1_y > 490:
            paddle1_y = 490

        # AI
        for num in range(0, 80):
            ball_esx = ball_x + num * ball_xv
            ball_esy = ball_y + num * ball_yv
            if ball_esx >= (screen_width - 20):
                if ball_esy <= 10:
                    paddle2_goal = 0 - ball_esy - rand1
                    break
                else:
                    paddle2_goal = ball_esy - rand1
                    break

        for count in range(0, 25):
            if paddle2_y < paddle2_goal and paddle2_y < 490:
                paddle2_y += 1
            elif paddle2_y > paddle2_goal and paddle2_y > 10:
                paddle2_y -= 1

        # collision of ball and paddles
        # left paddle
        if ball_x < paddle1_x + paddle1_w + ball_r and ball_y >= paddle1_y and ball_y <= paddle1_y + paddle1_h:
            rand1 = random.choice(
                [random.randint(10, 30), random.randint(70, 90)])
            ball_xv = abs(ball_xv)
            ball_yv = int(
                ((paddle1_y + (paddle1_y + paddle1_h)) / 2) - ball_y) * 2
            ball_yv = int(-ball_yv / ((5 * ball_r) / 7))

        # right paddle
        if ball_x > paddle2_x - ball_r and ball_y >= paddle2_y and ball_y <= paddle2_y + paddle2_h:
            rand1 = random.choice(
                [random.randint(10, 30), random.randint(70, 90)])
            ball_xv = -abs(ball_xv)
            ball_yv = int(
                ((paddle2_y + (paddle2_y + paddle2_h)) / 2) - ball_y) * 2
            ball_yv = int(-ball_yv / ((5 * ball_r) / 7))

        # player score
        if ball_x <= paddle1_x + paddle1_w / 2:
            player2_score += 1
            ball_xv = random.choice([5, -5])
            ball_yv = random.choice([5, -5])
            ball_x = int(screen_width / 2)
            ball_y = int(screen_height / 2)
        elif ball_x >= screen_width - 10 - paddle2_w / 2:
            player1_score += 1
            ball_xv = random.choice([5, -5])
            ball_yv = random.choice([5, -5])
            ball_x = int(screen_width / 2)
            ball_y = int(screen_height / 2)

        game_screen.fill(black)
        frame = pygame.draw.rect(game_screen, (255, 255, 255), (5, 5, 790, 590), 2)
        paddle_1 = pygame.draw.rect(
            game_screen, blue, (paddle1_x, paddle1_y, paddle1_w, paddle1_h), 0)
        paddle_2 = pygame.draw.rect(
            game_screen, red, (paddle2_x, paddle2_y, paddle2_w, paddle2_h), 0)
        net = pygame.draw.aaline = pygame.draw.line(game_screen, white, (int(
            screen_width / 2), 5), (int(screen_width / 2), 595))
        ball = pygame.draw.circle(
            game_screen, green, (ball_x, ball_y), ball_r, 0)
        score1 = font.render(str(player1_score), True, (255, 255, 255))
        score2 = font.render(str(player2_score), True, (255, 255, 255))
        game_screen.blit(score1, (320, 275))
        game_screen.blit(score2, (450, 275))

        pygame.display.update()

        time.sleep(0.016)


def Multi(RUNNING):
    # while (RUNNING):
    # initialize pygame
    pygame.init()
    global TimesCount

    # color globals
    red = (255, 0, 0)
    orange = (255, 127, 0)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    violet = (127, 0, 255)
    brown = (102, 51, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)

    # screen globals
    screen_width = 800
    screen_height = 600
    game_screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tennis")
    font = pygame.font.SysFont("monospace", 50)

    # ball globals
    ball_x = int(screen_width / 2)
    ball_y = int(screen_height / 2)
    ball_xv = random.choice([5, -5])
    ball_yv = random.choice([5, -5])
    ball_r = 10

    # pause
    pause = False

    # draw paddle 1
    paddle1_x = 10
    paddle1_y = int(screen_height / 2)
    paddle1_w = 10
    paddle1_h = 100

    # draw paddle 2
    paddle2_x = screen_width - 20
    paddle2_y = int(screen_height / 2)
    paddle2_w = 10
    paddle2_h = 100

    # initialize score
    player1_score = 0
    player2_score = 0

    # game loop
    pygame.mouse.set_visible(0)  # makes mouse invisible in game screen

    # while True:
    while (RUNNING):

        times = int(pygame.time.get_ticks() / 1000 - TimesCount)
        pressed = pygame.key.get_pressed()
        pygame.key.set_repeat()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        # if pressed[pygame.K_ESCAPE]:
        #     home()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUNNING = False
                menu.enable()
            if event.key == pygame.K_BACKSPACE and pause == False:
                pause_xv = ball_xv
                pause_yv = ball_yv
                ball_xv = 0
                ball_yv = 0
                pause = True
            elif event.key == pygame.K_RETURN and pause == True:
                ball_xv = pause_xv
                ball_yv = pause_yv
                pause = False
        if pressed[pygame.K_w] and pause == False:
            paddle1_y -= 15
        elif pressed[pygame.K_s] and pause == False:
            paddle1_y += 15

        if pressed[pygame.K_UP]:
            paddle2_y -= 15
        elif pressed[pygame.K_DOWN]:
            paddle2_y += 15

        # location of ball is updated
        ball_x += ball_xv
        ball_y += ball_yv

        # collision of ball with top/bottom of screen
        if ball_y - ball_r <= 5:
            ball_yv = abs(ball_yv)
        elif ball_y + ball_r >= 595:
            ball_yv = -abs(ball_yv)

        # collision of paddle with top/bottom of screen
        if paddle1_y < 10:
            paddle1_y = 10
        elif paddle1_y > 490:
            paddle1_y = 490

        if paddle2_y < 10:
            paddle2_y = 10
        elif paddle2_y > 490:
            paddle2_y = 490

        # collision of ball and paddles
        # left paddle
        if ball_x < paddle1_x + paddle1_w + ball_r and ball_y >= paddle1_y and ball_y <= paddle1_y + paddle1_h:
            ball_xv = abs(ball_xv)
            ball_yv = int(
                ((paddle1_y + (paddle1_y + paddle1_h)) / 2) - ball_y) * 2
            ball_yv = int(-ball_yv / ((5 * ball_r) / 7))

        # right paddle
        if ball_x > paddle2_x - ball_r and ball_y >= paddle2_y and ball_y <= paddle2_y + paddle2_h:
            ball_xv = -abs(ball_xv)
            ball_yv = int(
                ((paddle2_y + (paddle2_y + paddle2_h)) / 2) - ball_y) * 2
            ball_yv = int(-ball_yv / ((5 * ball_r) / 7))

        # player score
        if ball_x <= paddle1_x + paddle1_w / 2:
            player2_score += 1
            ball_xv = random.choice([5, -5])
            ball_yv = random.choice([5, -5])
            ball_x = int(screen_width / 2)
            ball_y = int(screen_height / 2)
        elif ball_x >= screen_width - 10 - paddle2_w / 2:
            player1_score += 1
            ball_xv = random.choice([5, -5])
            ball_yv = random.choice([5, -5])
            ball_x = int(screen_width / 2)
            ball_y = int(screen_height / 2)

        game_screen.fill(black)
        frame = pygame.draw.rect(game_screen, (255, 255, 255), (5, 5, 790, 590), 2)
        paddle_1 = pygame.draw.rect(
            game_screen, blue, (paddle1_x, paddle1_y, paddle1_w, paddle1_h), 0)
        paddle_2 = pygame.draw.rect(
            game_screen, red, (paddle2_x, paddle2_y, paddle2_w, paddle2_h), 0)
        net = pygame.draw.line(game_screen, white, (int(
            screen_width / 2), 5), (int(screen_width / 2), 595))
        ball = pygame.draw.circle(
            game_screen, green, (ball_x, ball_y), ball_r, 0)
        score1 = font.render(str(player1_score), True, (255, 255, 255))
        score2 = font.render(str(player2_score), True, (255, 255, 255))
        game_screen.blit(score1, (320, 275))
        game_screen.blit(score2, (450, 275))

        pygame.display.update()

        time.sleep(0.016)


def AI(RUNNING):
    # while (RUNNING):
    # initialize pygame
    pygame.init()
    global TimesCount

    # color globals
    red = (255, 0, 0)
    orange = (255, 127, 0)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    violet = (127, 0, 255)
    brown = (102, 51, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)

    # screen globals
    screen_width = 800
    screen_height = 600
    game_screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tennis")
    font = pygame.font.SysFont("monospace", 50)

    # ball globals, xv, yv max is 20
    ball_x = int(screen_width / 2)
    ball_y = int(screen_height / 2)
    ball_xv = random.choice([20, -20])
    ball_yv = random.choice([20, -20])
    ball_r = 10
    rand1 = 50

    # pause
    pause = False

    # draw paddle 1
    paddle1_x = 10
    paddle1_y = int(screen_height / 2)
    paddle1_w = 10
    paddle1_h = 100
    paddle1_goal = 300

    # draw paddle 2
    paddle2_x = screen_width - 20
    paddle2_y = int(screen_height / 2)
    paddle2_w = 10
    paddle2_h = 100
    paddle2_goal = 300

    # initialize score
    player1_score = 0
    player2_score = 0

    # game loop
    pygame.mouse.set_visible(0)  # makes mouse invisible in game screen
    # while True:
    while (RUNNING):
        times = int(pygame.time.get_ticks() / 1000 - TimesCount)
        pressed = pygame.key.get_pressed()
        pygame.key.set_repeat()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUNNING = False
                menu.enable()
            if event.key == pygame.K_BACKSPACE and pause == False:
                pause_xv = ball_xv
                pause_yv = ball_yv
                ball_xv = 0
                ball_yv = 0
                pause = True
            elif event.key == pygame.K_RETURN and pause == True:
                ball_xv = pause_xv
                ball_yv = pause_yv
                pause = False

        # location of ball is updated
        ball_x += ball_xv
        ball_y += ball_yv

        # collision of ball with top/bottom of screen
        if ball_y - ball_r <= 5:
            ball_yv = abs(ball_yv)
        elif ball_y + ball_r >= 595:
            ball_yv = -abs(ball_yv)

        # AI
        for num in range(0, 80):
            ball_esx = ball_x + num * ball_xv
            ball_esy = ball_y + num * ball_yv
            if ball_esx >= (screen_width - 20):
                if ball_esy <= 10:
                    paddle2_goal = 0 - ball_esy - rand1
                    break
                else:
                    paddle2_goal = ball_esy - rand1
                    break
            elif ball_esx <= 20:
                if ball_esy <= 10:
                    paddle1_goal = 0 - ball_esy - rand1
                    break
                else:
                    paddle1_goal = ball_esy - rand1
                    break

        for count in range(0, 25):
            if paddle2_y < paddle2_goal and paddle2_y < 490:
                paddle2_y += 1
            elif paddle2_y > paddle2_goal and paddle2_y > 10:
                paddle2_y -= 1
            if paddle1_y < paddle1_goal and paddle1_y < 490:
                paddle1_y += 1
            elif paddle1_y > paddle1_goal and paddle1_y > 10:
                paddle1_y -= 1

        # collision of ball and paddles
        # left paddle
        if ball_x < paddle1_x + paddle1_w + ball_r and ball_y >= paddle1_y and ball_y <= paddle1_y + paddle1_h:
            rand1 = random.choice(
                [random.randint(10, 30), random.randint(70, 90)])
            ball_xv = abs(ball_xv)
            ball_yv = int(
                ((paddle1_y + (paddle1_y + paddle1_h)) / 2) - ball_y) * 2
            ball_yv = int(-ball_yv / ((5 * ball_r) / 7))

        # right paddle
        if ball_x > paddle2_x - ball_r and ball_y >= paddle2_y and ball_y <= paddle2_y + paddle2_h:
            rand1 = random.choice(
                [random.randint(10, 30), random.randint(70, 90)])
            ball_xv = -abs(ball_xv)
            ball_yv = int(
                ((paddle2_y + (paddle2_y + paddle2_h)) / 2) - ball_y) * 2
            ball_yv = int(-ball_yv / ((5 * ball_r) / 7))

        # player score
        if ball_x <= paddle1_x + paddle1_w / 2:
            player2_score += 1
            ball_xv = random.choice([20, -20])
            ball_yv = random.choice([20, -20])
            ball_x = int(screen_width / 2)
            ball_y = int(screen_height / 2)
        elif ball_x >= screen_width - 10 - paddle2_w / 2:
            player1_score += 1
            ball_xv = random.choice([20, -20])
            ball_yv = random.choice([20, -20])
            ball_x = int(screen_width / 2)
            ball_y = int(screen_height / 2)

        game_screen.fill(black)
        frame = pygame.draw.rect(game_screen, (255, 255, 255), (5, 5, 790, 590), 2)
        paddle_1 = pygame.draw.rect(
            game_screen, blue, (paddle1_x, paddle1_y, paddle1_w, paddle1_h), 0)
        paddle_2 = pygame.draw.rect(
            game_screen, red, (paddle2_x, paddle2_y, paddle2_w, paddle2_h), 0)
        net = pygame.draw.line(game_screen, white, (int(
            screen_width / 2), 5), (int(screen_width / 2), 595))
        ball = pygame.draw.circle(
            game_screen, green, (ball_x, ball_y), ball_r, 0)
        score1 = font.render(str(player1_score), True, (255, 255, 255))
        score2 = font.render(str(player2_score), True, (255, 255, 255))
        game_screen.blit(score1, (320, 275))
        game_screen.blit(score2, (450, 275))

        pygame.display.update()

        time.sleep(0.016)


if __name__ == "__main__":
    # 全域參數
    BLACK = (0, 0, 0)
    W = 600
    H = 600

    # 建立pygame window
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption('Snake ML v.1.0.0')
    screen.fill(BLACK)
    pygame.display.flip()
    # -----------------------------------------------------------------------------
    # Constants and global variables
    ABOUT = ['PygameMenu {0}'.format(pygameMenu.__version__),
             'Author: {0}'.format(pygameMenu.__author__),
             PYGAMEMENU_TEXT_NEWLINE,
             'Email: {0}'.format(pygameMenu.__email__)]
    COLOR_BLUE = (12, 12, 200)
    COLOR_BACKGROUND = [128, 0, 128]
    COLOR_WHITE = (255, 255, 255)
    FPS = 60
    H_SIZE = 600  # Height of window size
    HELP = ['Press ESC to enable/disable Menu',
            'Press ENTER to access a Sub-Menu or use an option',
            'Press UP/DOWN to move through Menu',
            'Press BackSpace to pause']
    W_SIZE = 800  # Width of window size

    # -----------------------------------------------------------------------------
    # Init pygame
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Write help message on console
    for m in HELP:
        print(m)

    # Create window
    surface = pygame.display.set_mode((W_SIZE, H_SIZE))
    pygame.display.set_caption('PygameMenu example')

    # Main timer and game clock
    clock = pygame.time.Clock()
    timer = [0.0]
    dt = 1.0 / FPS
    timer_font = pygame.font.Font(pygameMenu.fonts.FONT_NEVIS, 100)


    # -----------------------------------------------------------------------------
    def mainmenu_background():
        """
        Background color of the main menu, on this function user can plot
        images, play sounds, etc.
        """
        surface.fill((40, 0, 40))


    # -----------------------------------------------------------------------------
    # Timer menu
    timer_menu = pygameMenu.Menu(surface,
                                 dopause=False,
                                 font=pygameMenu.fonts.FONT_NEVIS,
                                 menu_alpha=85,
                                 menu_color=(0, 0, 0),  # Background color
                                 menu_color_title=(0, 0, 0),
                                 menu_height=int(H_SIZE / 2+70),
                                 menu_width=600,
                                 onclose=PYGAME_MENU_RESET,  # If this menu closes (press ESC) back to main
                                 title='Game Modes',
                                 title_offsety=5,  # Adds 5px to title vertical position
                                 window_height=H_SIZE,
                                 window_width=W_SIZE
                                 )

    timer_menu.add_selector('Mode',
                            [('Solo', True)],
                            onchange=None,  # Action when changing element with left/right
                            onreturn=Solo
                            )
    timer_menu.add_selector('Mode',
                            [('Duo', True)],
                            onchange=None,  # Action when changing element with left/right
                            onreturn=Multi
                            )
    timer_menu.add_selector('Mode',
                            [('AI', True)],
                            onchange=None,  # Action when changing element with left/right
                            onreturn=AI
                            )
    timer_menu.add_option('Return to Menu', PYGAME_MENU_BACK)
    timer_menu.add_option('Close Menu', PYGAME_MENU_CLOSE)

    # -----------------------------------------------------------------------------
    # About menu
    about_menu = pygameMenu.TextMenu(surface,
                                     dopause=False,
                                     font=pygameMenu.fonts.FONT_NEVIS,
                                     font_size_title=30,
                                     font_title=pygameMenu.fonts.FONT_8BIT,
                                     menu_color_title=COLOR_BLUE,
                                     onclose=PYGAME_MENU_DISABLE_CLOSE,  # Disable menu close (ESC button)
                                     text_fontsize=20,
                                     title='About',
                                     window_height=H_SIZE,
                                     window_width=W_SIZE
                                     )
    about_menu.add_option('Return to Menu', PYGAME_MENU_BACK)
    for m in ABOUT:
        about_menu.add_line(m)
    about_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)

    # -----------------------------------------------------------------------------
    # Main menu, pauses execution of the application
    menu = pygameMenu.Menu(surface,
                           bgfun=mainmenu_background,
                           enabled=False,
                           font=pygameMenu.fonts.FONT_NEVIS,
                           menu_alpha=90,
                           onclose=PYGAME_MENU_CLOSE,
                           title='Main Menu',
                           title_offsety=5,
                           window_height=H_SIZE,
                           window_width=W_SIZE
                           )
    menu.add_option(timer_menu.get_title(), timer_menu)  # Add timer submenu
    menu.add_option(about_menu.get_title(), about_menu)  # Add about submenu
    menu.add_option('Exit', PYGAME_MENU_EXIT)  # Add exit function

    # -----------------------------------------------------------------------------

    running = False
    while (running == False):
        # Paint background
        surface.fill(COLOR_BACKGROUND)
        menu.enable()

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # running = True
                    menu.enable()

        # Execute main from principal menu if is enabled
        menu.mainloop(events)

        # Flip surface
        pygame.display.flip()
