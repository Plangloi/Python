import pygame, sys, time
 
pygame.mixer.init()

sortir = 0



while sortir == 0:
    choix = input("1 = Wave\n2 = mp3\n3 = flac\n(Q)quit\n:")



    match choix:
        case "1":
            pygame.mixer.music.load("/Users/ipatmbp4/Downloads/10Fwave.wav")
            pygame.mixer.music.play()


        case "2":
            pygame.mixer.music.load("/Users/ipatmbp4/Downloads/10Fmp3.mp3")
            pygame.mixer.music.play()


        case "3":
            pygame.mixer.music.load("/Users/ipatmbp4/Downloads/10Fflac.flac")
            pygame.mixer.music.play()

        case "q":
            sortir = 1

        case _:
            print("Veuillez entrer un choix valide")

    


