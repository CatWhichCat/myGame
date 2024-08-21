import pygame
import sys
import time

from bullet import Bullet
from ufo import UFO


def events(screen, gun, bullets):
    '''Обработка событий'''
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False
                
def update(bg_color, screen, stats, score, gun, ufo, bullets):
    '''Обновление экрана'''
    screen.fill(bg_color)
    score.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    ufo.draw(screen)
    pygame.display.flip()
    
def update_bullets(screen, stats, score, ufos, bullets):
    '''Обновляет позиции пуль'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets)) -> Проверка удаляется ли пуля доходя до гриницы экрана
    collisions = pygame.sprite.groupcollide(bullets, ufos, True, True)
    if collisions:
        for ufos in collisions.values():
            stats.score += 10 * len(ufos)
        score.image_score()
        check_high_score(stats, score)
        score.image_guns()
        
    if len(ufos) == 0:
        bullets.empty()
        create_army(screen, ufos)
        
def gun_kill(stats, screen, score, gun, ufos, bullets):
    '''Столкновение пушки и прищельцев'''
    if stats.guns_left > 0:
        stats.guns_left -= 1
        score.image_guns()
        ufos.empty()
        bullets.empty()
        create_army(screen, ufos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()
    
    
def update_ufo(stats, screen, score, gun, ufos, bullets):
    '''Обновляет позицию прищельцев'''
    ufos.update()
    if pygame.sprite.spritecollideany(gun, ufos):
        gun_kill(stats, screen, score, gun, ufos, bullets)
    ufos_check(stats, screen, score, gun, ufos, bullets)
        
def ufos_check(stats, screen, score, gun, ufos, bullets):
    '''Проверка на косание нижней границы прищельцев'''
    screen_rect = screen.get_rect()
    for ufo in ufos.sprites():
        if ufo.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, score, gun, ufos, bullets)
            break
        
def create_army(screen, ufos):
    '''Создание армии прищельцов'''
    ufo = UFO(screen)
    ufo_wight = ufo.rect.width
    number_ufo_x = int((800 - 2 * ufo_wight) / ufo_wight)
    ufo_height = ufo.rect.height
    number_ufo_y = int((700 - 100 - 2 * ufo_height) / ufo_height)
    
    for row_number in range(number_ufo_y - 4):
        for ufo_number in range(number_ufo_x):
            ufo = UFO(screen)
            ufo.x = ufo_wight + (ufo_wight * ufo_number)
            ufo.y = ufo_height + (ufo_height * row_number)
            ufo.rect.x = ufo.x
            ufo.rect.y = ufo.rect.height + (ufo.rect.height * row_number)
            ufos.add(ufo)
    
def check_high_score(stats, score):
    '''Проверка новых рекордов'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))