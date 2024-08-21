import pygame
from pygame.sprite import Group

class UFO(pygame.sprite.Sprite):
    '''Класс одного прищельца'''
    def __init__(self, screen):
        '''инициализируем и создаем начальную позицию'''
        super(UFO, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ufo.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def draw(self):
        '''Вывод прищельца на экран'''
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        '''Перемещает положение прищельцев'''
        self.y += 0.1
        self.rect.y = self.y