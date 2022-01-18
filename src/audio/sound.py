import pygame
import paths

def play(audio_name:str, vol:float=0.6):
    sound = pygame.mixer.Sound(f"{paths.audio}/{audio_name}")
    sound.set_volume(vol)
    sound.play()
    return sound