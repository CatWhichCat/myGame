import pygame

class Stats():
    '''Отслеживание статистики'''
    def __init__(self):
        '''Инициализирует статистику'''
        self.reset_start()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())
        
    def reset_start(self):
        '''статистика, изменяющаяся во время игры'''
        self.guns_left = 2
        self.score = 0
        