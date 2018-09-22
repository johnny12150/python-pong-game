import pygame
import random
import time
from sys import exit

TimesCount = 0


def home():
    # set the window size
    pygame.init()
    pygame.font.init()
    global TimesCount
    while True:
        BLACK = (0, 0, 0)
        window = pygame.display.set_mode((800, 600), 0, 24)
        window.fill(BLACK)
        myfont = pygame.font.SysFont("Tennis", 40)
        nlabel = myfont.render("Welcome to Tennis game", 1, (255, 0, 0))
        nlabel1 = myfont.render("Press 1 to Solo Mode", 1, (255, 0, 0))
        nlabel2 = myfont.render("Press 2 to Multi Mode", 1, (255, 0, 0))
        nlabel3 = myfont.render("Press 3 to AI Mode", 1, (255, 0, 0))
        nlabel4 = myfont.render("In game: Press Esc to Menu", 1, (255, 0, 0))
        nlabel5 = myfont.render("In game: Press Backspace to Pause", 1, (255, 0, 0))
        nlabel6 = myfont.render("In game: Press Enter to Continue", 1, (255, 0, 0))
        TimesCount = int(pygame.time.get_ticks() / 1000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Solo()
                elif event.key == pygame.K_2:
                    Multi()
                elif event.key == pygame.K_3:
                    AI()
        window.blit(nlabel, (200, 100))
        window.blit(nlabel1, (200, 250))
        window.blit(nlabel2, (200, 300))
        window.blit(nlabel3, (200, 350))
        window.blit(nlabel4, (200, 400))
        window.blit(nlabel5, (200, 450))
        window.blit(nlabel6, (200, 500))
        pygame.display.flip()


def Solo(RUNNING):
    while (RUNNING):
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

        while True:
            times = int(pygame.time.get_ticks() / 1000 - TimesCount)
            pressed = pygame.key.get_pressed()
            pygame.key.set_repeat()
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    exit()
                # if pressed[pygame.K_ESCAPE]:
                #     home()
                if event.type == pygame.KEYDOWN:
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


def Multi():
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

    while True:
        times = int(pygame.time.get_ticks() / 1000 - TimesCount)
        pressed = pygame.key.get_pressed()
        pygame.key.set_repeat()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        # if pressed[pygame.K_ESCAPE]:
        #     home()
        if event.type == pygame.KEYDOWN:
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


def AI():
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
    while True:
        times = int(pygame.time.get_ticks() / 1000 - TimesCount)
        pressed = pygame.key.get_pressed()
        pygame.key.set_repeat()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        # if pressed[pygame.K_ESCAPE]:
        #     home()
        if event.type == pygame.KEYDOWN:
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

# home()
