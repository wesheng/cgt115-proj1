import pygame
import random
import json
import os
import enum

splash_text = [
    'Some text',
    'Hello world!',
    'Splishy splashy!',
    'much text wow',
]

config = {
    'title': 'graphic design is my passion',
    'window-width': 800,
    'window-height': 600,
    'background-color': (0, 255, 0),
    'font': 'Comic Sans MS',
    'text-color': (200, 0, 0)
}

config_file = 'config.json'
if os.path.isfile(config_file):
    with open(config_file) as f:
        data = f.read()
        config = json.loads(data)
        print(config)
else:
    with open(config_file, 'w') as f:
        contents = json.dumps(config, indent=4)
        print(contents)
        f.write(contents)

pygame.init()
dimensions = (config['window-width'], config['window-height'])
screen = pygame.display.set_mode(dimensions)
surface = pygame.display.get_surface()

class CenteredText:
    def __init__(self, font, position, text, color):
        self.text = font.render(text, True, color)
        self.rect = self.text.get_rect(center=position)

    def draw(self, screen):
        screen.blit(self.text, self.rect)

class GameState(enum.Enum):
    MAIN_MENU = 0
    GAME = 1
    SETTING = 2

current_state = GameState.GAME

pygame.font.init()
font = pygame.font.SysFont(config['font'], 20)
text_to_display = splash_text[random.randrange(len(splash_text))]
# text = font.render(text_to_display, True, config['text-color'])
screen_center = (dimensions[0] / 2, dimensions[1] / 2)
# text_rect = text.get_rect(center=screen_center)

main_menu_txt = CenteredText(font, screen_center, "Main Menu", config['text-color'])
game_txt = CenteredText(font, screen_center, "Game", config['text-color'])
settings_txt = CenteredText(font, screen_center, "Setting", config['text-color'])


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                current_state = GameState.MAIN_MENU
            if event.key == pygame.K_RETURN:
                current_state = GameState.SETTING
            if event.key == pygame.K_SPACE:
                current_state = GameState.GAME
    screen.fill(config['background-color'])
    # screen.blit(text, text_rect)
    if current_state == GameState.MAIN_MENU:
        main_menu_txt.draw(screen)
    if current_state == GameState.SETTING:
        settings_txt.draw(screen)
    if current_state == GameState.GAME:
        game_txt.draw(screen)
    pygame.display.flip()