import pygame
import pygame_menu
#import pong

#MENU_BACKGROUND_IMAGE = pygame_menu.baseimage.BaseImage(
#    image_path='menu_image.png',
#    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,)

#COLOR_BACKGROUND = (0, 0, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (255, 255, 255, 45)
#MENU_BACKGROUND_COLOR = MENU_BACKGROUND_IMAGE
MENU_TITLE_COLOR = (51, 51, 255)
WINDOW_SCALE = 0.75

#MENU_FONT = pygame_menu.font.FONT_MUNRO
MENU_FONT = pygame_menu.font.FONT_NEVIS

TITLE_STYLE = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL
#TITLE_STYLE = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY	
#TITLE_STYLE = pygame_menu.widgets.MENUBAR_STYLE_NONE
#TITLE_STYLE = pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE
#TITLE_STYLE = pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE_TITLE
#TITLE_STYLE = pygame_menu.widgets.MENUBAR_STYLE_ADAPTIVE	

pygame.display.init()
INFO = pygame.display.Info()
TILE_SIZE = int(INFO.current_h * 0.035)
WINDOW_SIZE = (13 * TILE_SIZE, 13 * TILE_SIZE)

clock = None
show_path = True
surface = pygame.display.set_mode(WINDOW_SIZE)


def main_background():
    global surface
    #surface.fill(COLOR_BACKGROUND)
    BACKGROUND_IMAGE = pygame.image.load('menu_image.png').convert()
    surface.blit(BACKGROUND_IMAGE, (0,0))


def menu_loop():
    pygame.init()

    pygame.display.set_caption('Pupil Pong')
    clock = pygame.time.Clock()

    menu_theme = pygame_menu.Theme(
        selection_color=COLOR_WHITE,
        widget_font=MENU_FONT,
        title_font_size=TILE_SIZE,
        title_font_color=COLOR_BLACK,
        title_font=MENU_FONT,
        title_bar_style=TITLE_STYLE,
        widget_font_color=COLOR_BLACK,
        widget_font_size=int(TILE_SIZE*0.75),
        background_color=MENU_BACKGROUND_COLOR,
        title_background_color=MENU_TITLE_COLOR,
    )

    other_menu_theme = pygame_menu.themes.Theme(
        selection_color=COLOR_WHITE,
        widget_font=MENU_FONT,
        title_font_size=TILE_SIZE,
        title_font_color=COLOR_BLACK,
        title_font=MENU_FONT,
        title_bar_style=TITLE_STYLE,
        widget_font_color=COLOR_BLACK,
        widget_font_size=int(TILE_SIZE*0.5),
        background_color=MENU_BACKGROUND_COLOR,
        title_background_color=MENU_TITLE_COLOR
    )

    about_menu = pygame_menu.Menu(
        theme=other_menu_theme,
        height=int(WINDOW_SIZE[1] * WINDOW_SCALE),
        width=int(WINDOW_SIZE[0] * WINDOW_SCALE),
        overflow=False,
        title='About'
    )

    about_menu.add.label("Movement:")
    about_menu.add.label("\nCreators:") 
    about_menu.add.label("Will Whitehead \nJoshua Lee \nSabastian Maciorowski", wordwrap=True)
    about_menu.add.vertical_margin(25)
    about_menu.add.button('Return to main menu', pygame_menu.events.BACK)

    main_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * WINDOW_SCALE),
        width=int(WINDOW_SIZE[0] * WINDOW_SCALE),
        onclose=pygame_menu.events.EXIT,
        title='Pupil Pong'
    )

    main_menu.add.button('Start Game')
    main_menu.add.button('Help Menu', about_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)

    running = True
    while running:

        clock.tick(FPS)

        main_background()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        if main_menu.is_enabled():
            main_menu.mainloop(surface, main_background)

        pygame.display.flip()

    exit()


if __name__ == "__main__":
    menu_loop()
