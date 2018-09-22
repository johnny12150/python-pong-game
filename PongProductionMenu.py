import pygame
import pygameMenu  # This imports classes and other things
from pygameMenu.locals import *
from random import randrange
import os
import PongProductionModes

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
                                 title='Game Modes',
                                 title_offsety=5,  # Adds 5px to title vertical position
                                 window_height=H_SIZE,
                                 window_width=W_SIZE
                                 )

    # timer_menu.add_selector('Solo Mode', PongProductionModes.Solo(), onchange=None, onreturn=None)
    timer_menu.add_selector('Mode',
                            [('Solo', True)],
                            onchange=None,  # Action when changing element with left/right
                            onreturn=PongProductionModes.Solo,  # Action when pressing return on a element
                            default=1  # Optional parameter that sets default item of selector
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
    # menu.add_option('Multi', PongProductionModes.home())

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
