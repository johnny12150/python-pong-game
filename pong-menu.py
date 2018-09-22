import pygame
import pygameMenu  # This imports classes and other things
from pygameMenu.locals import *
from random import randrange
import os

### Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

### Constants
W = 600
H = 600
pygame.font.init()
comic = pygame.font.SysFont('Comic Sans MS', 30)

### Variables
wt = 10
mplay = False

p1x = W / 30
p1y = H / 2 - ((W / 60) ** 2) / 2

p2x = W - (W / 30)
p2y = H / 2 - ((W / 60) ** 2) / 2

p1score = 0
p2score = 0

w_p = False
s_p = False
wsr = False
u_p = False
d_p = False
udr = False

dm = H / 40

paddle_width = W / 60
paddle_height = paddle_width ** 2

bsd = 1

bx = W / 2
by = H / 2
bw = W / 65
bxv = H / 60
bxv = -bxv
byv = 0


### Functions
def drawpaddle(x, y, w, h):
    pygame.draw.rect(screen, WHITE, (x, y, w, h))


def drawball(x, y):
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), int(bw))


def uploc():
    global p1y
    global p2y
    if w_p:
        if p1y - (dm) < 0:
            p1y = 0
        else:
            p1y -= dm
    elif s_p:
        if p1y + (dm) + paddle_height > H:
            p1y = H - paddle_height
        else:
            p1y += dm
    if u_p:
        if p2y - (dm) < 0:
            p2y = 0
        else:
            p2y -= dm
    elif d_p:
        if p2y + (dm) + paddle_height > H:
            p2y = H - paddle_height
        else:
            p2y += dm


def upblnv():
    global bx
    global bxv
    global by
    global byv
    global p2score
    global p1score

    # 球碰到(left)球拍
    if (bx + bxv < p1x + paddle_width) and ((p1y < by + byv + bw) and (by + byv - bw < p1y + paddle_height)):
        # 碰撞後反方向
        bxv = -bxv
        # 反彈後的y座標
        byv = ((p1y + (p1y + paddle_height)) / 2) - by
        byv = -byv / ((5 * bw) / 7)
    elif bx + bxv < 0:
        p2score += 1
        bx = W / 2
        bxv = H / 60
        by = H / 2
        byv = 0
    if (bx + bxv > p2x) and ((p2y < by + byv + bw) and (by + byv - bw < p2y + paddle_height)):
        bxv = -bxv
        byv = ((p2y + (p2y + paddle_height)) / 2) - by
        byv = -byv / ((5 * bw) / 7)
    elif bx + bxv > W:
        p1score += 1
        bx = W / 2
        bxv = -H / 60
        by = H / 2
        byv = 0
    if by + byv > H or by + byv < 0:
        byv = -byv

    bx += bxv
    by += byv


def drawscore():
    score = comic.render(str(p1score) + " - " + str(p2score), False, WHITE)
    screen.blit(score, (W / 2, 30))


### Initialize
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
        'Press LEFT/RIGHT to move through Selectors']
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

def change_color_bg(c, **kwargs):
    """
    Change background color

    :param c: Color tuple
    """
    if c == (-1, -1, -1):  # If random color
        c = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
    if kwargs['write_on_console']:
        print('New background color: ({0},{1},{2})'.format(*c))
    COLOR_BACKGROUND[0] = c[0]
    COLOR_BACKGROUND[1] = c[1]
    COLOR_BACKGROUND[2] = c[2]


def start_multi_player_mode(RUNNING):
    # print(RUNNING[0])
    while (RUNNING):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    RUNNING = False
                    menu.enable()
                if event.key == pygame.K_w:
                    w_p = True
                    if s_p == True:
                        s_p = False
                        wsr = True
                if event.key == pygame.K_s:
                    s_p = True
                    if w_p == True:
                        w_p = False
                        wsr = True
                if event.key == pygame.K_UP:
                    u_p = True
                    if d_p == True:
                        d_p = False
                        udr = True
                if event.key == pygame.K_DOWN:
                    d_p = True
                    if u_p == True:
                        u_p = False
                        udr = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    w_p = False
                    if wsr == True:
                        s_p = True
                        wsr = False
                if event.key == pygame.K_s:
                    s_p = False
                    if wsr == True:
                        w_p = True
                        wsr = False
                if event.key == pygame.K_UP:
                    u_p = False
                    if udr == True:
                        d_p = True
                        udr = False
                if event.key == pygame.K_DOWN:
                    d_p = False
                    if udr == True:
                        u_p = True
                        udr = False

        screen.fill(BLACK)
        uploc()
        upblnv()
        drawscore()
        drawball(bx, by)
        drawpaddle(p1x, p1y, paddle_width, paddle_height)
        drawpaddle(p2x, p2y, paddle_width, paddle_height)
        pygame.display.flip()
        pygame.time.wait(wt)


# -----------------------------------------------------------------------------
# Timer menu
timer_menu = pygameMenu.Menu(surface,
                             dopause=False,
                             font=pygameMenu.fonts.FONT_NEVIS,
                             menu_alpha=85,
                             menu_color=(0, 0, 0),  # Background color
                             menu_color_title=(0, 0, 0),
                             menu_height=int(H_SIZE / 2),
                             menu_width=600,
                             onclose=PYGAME_MENU_RESET,  # If this menu closes (press ESC) back to main
                             title='Timer Menu',
                             title_offsety=5,  # Adds 5px to title vertical position
                             window_height=H_SIZE,
                             window_width=W_SIZE
                             )

# Adds a selector (element that can handle functions)
# timer_menu.add_selector('Change bgcolor',
#                         # Values of selector, call to change_color_bg
#                         [('Random', (-1, -1, -1)),
#                          ('Default', (128, 0, 128)),
#                          ('Black', (0, 0, 0)),
#                          ('Blue', COLOR_BLUE)],
#                         onchange=None,  # Action when changing element with left/right
#                         onreturn=change_color_bg,  # Action when pressing return on a element
#                         default=1,  # Optional parameter that sets default item of selector
#                         write_on_console=True  # Optional parametrs to change_color_bg function
#                         )

# pass value to function
timer_menu.add_selector('Multi player mode',
                        [('RUNNING', True)],
                        onchange=None,  # Action when changing element with left/right
                        onreturn=start_multi_player_mode,  # Action when pressing return on a element
                        default=1  # Optional parameter that sets default item of selector
                        )
timer_menu.add_option('Return to Menu', PYGAME_MENU_BACK)
timer_menu.add_option('Close Menu', PYGAME_MENU_CLOSE)

# -----------------------------------------------------------------------------
# Help menu
help_menu = pygameMenu.TextMenu(surface,
                                dopause=False,
                                font=pygameMenu.fonts.FONT_FRANCHISE,
                                menu_color=(30, 50, 107),  # Background color
                                menu_color_title=(120, 45, 30),
                                onclose=PYGAME_MENU_DISABLE_CLOSE,  # Pressing ESC button does nothing
                                title='Help',
                                window_height=H_SIZE,
                                window_width=W_SIZE
                                )
help_menu.add_option('Return to Menu', PYGAME_MENU_BACK)
for m in HELP:
    help_menu.add_line(m)

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
menu.add_option(help_menu.get_title(), help_menu)  # Add help submenu
menu.add_option(about_menu.get_title(), about_menu)  # Add about submenu
menu.add_option('Exit', PYGAME_MENU_EXIT)  # Add exit function
# add a tab for multi player
menu.add_option('Multi Player Mode', start_multi_player_mode)

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

# while running loop
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w:
                w_p = True
                if s_p == True:
                    s_p = False
                    wsr = True
            if event.key == pygame.K_s:
                s_p = True
                if w_p == True:
                    w_p = False
                    wsr = True
            if event.key == pygame.K_UP:
                u_p = True
                if d_p == True:
                    d_p = False
                    udr = True
            if event.key == pygame.K_DOWN:
                d_p = True
                if u_p == True:
                    u_p = False
                    udr = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                w_p = False
                if wsr == True:
                    s_p = True
                    wsr = False
            if event.key == pygame.K_s:
                s_p = False
                if wsr == True:
                    w_p = True
                    wsr = False
            if event.key == pygame.K_UP:
                u_p = False
                if udr == True:
                    d_p = True
                    udr = False
            if event.key == pygame.K_DOWN:
                d_p = False
                if udr == True:
                    u_p = True
                    udr = False

    screen.fill(BLACK)
    uploc()
    upblnv()
    drawscore()
    drawball(bx, by)
    drawpaddle(p1x, p1y, paddle_width, paddle_height)
    drawpaddle(p2x, p2y, paddle_width, paddle_height)
    pygame.display.flip()
    pygame.time.wait(wt)
