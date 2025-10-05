import pygame
import time
import random

controls = ['L','R','U','D']

def fake_function():
    while True:
        value = random.choice(controls)
        if value == 'L':
            chosen_key = pygame.K_LEFT
        elif value == 'R':
            chosen_key = pygame.K_RIGHT
        elif value == 'U':
            chosen_key = pygame.K_UP
        else:
            chosen_key = pygame.K_DOWN
        event = pygame.event.Event(pygame.KEYDOWN, key=chosen_key)
        pygame.event.post(event)  
        print(value)
        time.sleep(0.5)