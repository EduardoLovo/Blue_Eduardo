import os
import pygame

pygame.init()
if os.path.exists('./Users/Eduardo/Downloads/teste.mp3'):
    pygame.mixer.music.load('./Blue_T3C5_mod1/Aula24 - 8 Jul 2021/musicproj.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)

    clock = pygame.time.Clock()
    clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
else:
    print('O arquivo musica.mp3 não está no diretório do script Python')