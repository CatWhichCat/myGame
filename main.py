import pygame, controls

from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scorse import Scorse



def run():
    
    pygame.init()
    screen = pygame.display.set_mode((800, 700))
    pygame.display.set_caption('Космические войны')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    ufos = Group()
    controls.create_army(screen, ufos)
    stats = Stats()
    score = Scorse(screen, stats)
    
    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, score, gun, ufos, bullets)
            controls.update_bullets(screen, stats, score, ufos, bullets)
            controls.update_ufo(stats, screen, score, gun, ufos, bullets)

run()