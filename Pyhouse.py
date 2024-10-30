import pip
pip.main(['install', 'pygame'])
import pygame

# initialise pygame mixer
pygame.init()

check = True

# Associating function with song emotion
while check:
    request=input("Enter how you feel out of the following: angry, sad, happy, chill | ").lower()
    if request=='angry':
        pygame.mixer.music.load('angry.mp3')
        pygame.mixer.music.play()
    elif request=='sad':
        pygame.mixer.music.load('sad.mp3')
        pygame.mixer.music.play()
    elif request=='happy':
        pygame.mixer.music.load('happy.mp3')
        pygame.mixer.music.play()
    elif request=='chill':
        pygame.mixer.music.load('chill.mp3')
        pygame.mixer.music.play()
    else:
        print("No song available for this emotion.")




    



        
