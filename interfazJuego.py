import pygame, sys, random
import RandomBinario as rb

def main():
    pygame.init()
    difficulty = 10
    red = 255, 0, 0
    black = 0, 0, 0
    white = 255, 255, 255
    yellow = 255, 255, 0
    size = width, height = 600, 550
    font = pygame.font.SysFont(None, 23)
    font_2 = pygame.font.SysFont(None, 40)
    listaOponentes = ['Samurai Fuego', 'Samurai Agua', 'Samurai Tierra', 'Samurai Aire', 'Samurai Rayo',
                    'Guerrero Fuego', 'Guerrero Agua', 'Guerrero Tierra', 'Guerrero Aire', 'Guerrero Rayo',
                    'KOer Fuego', 'KOer Agua', 'KOer Tierra', 'KOer Aire', 'KOer Rayo',
                    'Asesino Fuego', 'Asesino Agua', 'Asesino Tierra', 'Asesino Aire', 'Asesino Rayo']

    def message_to_screen(msg, color, x, y):#Funcion que imprime texto en la pantalla
        screen_text = font.render(msg, True, color)
        screen.blit(screen_text, [x, y])

    def message_perdiste(msg, color, x, y):#Funcion que imprime texto en la pantalla
        screen_text = font_2.render(msg, True, color)
        screen.blit(screen_text, [x, y])

    x = round((225/difficulty))*difficulty
    y = round((200/difficulty))*difficulty
    p1 = round(random.randint(1, width-difficulty)/difficulty)*difficulty
    p2 = round(random.randint(1, height-difficulty)/difficulty)*difficulty
    opo = random.randint(0, 20)
    #print(p1, p2)
    change_x = 0
    change_y = 0
    a = 0
    pantalla = 0
    personaje_actual = 'Huo'
    perso = 0
    battle = 0
    timer = 0
    timer_1 = 0
    ataque_actual = 'GolpeFuego'
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Juegochido')
    #outZone = pygame.event.Event(pygame.QUIT, {'motivo':'Out of zone'})
    #outBattle = pygame.event.Event(pygame.QUIT, {'motivo':'5 batallas'})
    COLITION = pygame.USEREVENT
    pointReached = pygame.event.Event(COLITION, {'object': 'point','p1': p1, 'p2': p2})
    battleReached = pygame.event.Event(COLITION, {'object': 'enemy', 'x': x, 'y': y})
    pointCounter = 0
    while True:
        while(pantalla == 1):
            #check for quit events
            for event in pygame.event.get():
                #print(event)
                if(event.type == pygame.QUIT):
                    sys.exit()
                if(event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_LEFT:
                        change_x = 0-difficulty
                        change_y = 0
                    elif event.key == pygame.K_RIGHT:
                        change_x = difficulty
                        change_y = 0
                    elif event.key == pygame.K_UP:
                        change_y = 0-difficulty
                        change_x = 0
                    elif event.key == pygame.K_DOWN:
                        change_y = difficulty
                        change_x = 0

                if(event.type == COLITION):
                    if(event.object == 'point'):
                        p1 = round(random.randint(1, width-difficulty)/difficulty)*difficulty
                        p2 = round(random.randint(1, height-difficulty)/difficulty)*difficulty
                        pointCounter += 1
                        #print(p1, p2)
                    if(event.object == 'enemy'):
                        mr = rb.main_recomendacion_interfaz(listaOponentes[perso], listaOponentes[opo])
                        if(battle == 9):
                            pantalla = 3
                        else:
                            timer_1 = 0
                            pantalla = 2
                        change_x = 0
                        change_y = 0
                        for i in range(limite):
                            w[i] = 0
                            z[i] = 0
                        a = 20
                        battle += 1

            #frames per second
            msElapsed = clock.tick(30)

            x += change_x
            y += change_y

            if(x > width):
                pantalla = 3
            elif(x < 0):
                pantalla = 3
            elif(y > height):
                pantalla = 3
            elif(y < 0):
                #pygame.event.post(pointReached)
                pantalla = 3

            #erase the screen
            screen.fill(black)

            message_to_screen('Puntaje: '+str(pointCounter), yellow, 0, 0)

            point = pygame.draw.circle(screen, yellow, [p1, p2], 5)

            if(a % 50 == 0):
                a = 0
                limite = random.randint(5, 20)
                w = []
                z = []
                enemy = []
                for i in range(limite):
                    w.append(round(random.randint(1, width-difficulty)/difficulty)*difficulty)
                    z.append(round(random.randint(1, height-difficulty)/difficulty)*difficulty)
                    enemy.append(pygame.draw.circle(screen, red, [w[i], z[i]], 5))
            else:
                for j in range(limite):
                    enemy.append(pygame.draw.circle(screen, red, [w[j], z[j]], 5))
            a += 1

            #drawing
            player = pygame.draw.circle(screen, white, [x, y], 5)

            if((x == p1-difficulty or x == p1+difficulty or x == p1) and (y == p2-difficulty or y == p2+difficulty or y == p2)):
                pygame.event.post(pointReached)

            for i in range(limite):
                if((x == w[i] or x == w[i]-difficulty or x == w[i]+difficulty) and (y == z[i] or y == z[i]-difficulty or y == z[i]+difficulty)):
                    pygame.event.post(battleReached)

            #update the screen
            pygame.display.update()

        while(pantalla == 0):
            for event in pygame.event.get():
                #print(event)
                if(event.type == pygame.QUIT):
                    sys.exit()
                if(event.type == pygame.KEYDOWN):
                    if(event.unicode == '0'):
                        personaje_actual = 'Huo'
                        perso = 0
                    if(event.unicode == '1'):
                        personaje_actual = 'Shui'
                        perso = 1
                    if(event.unicode == '2'):
                        personaje_actual = 'Tu'
                        perso = 2
                    if(event.unicode == '3'):
                        personaje_actual = 'Fei'
                        perso = 3
                    if(event.unicode == '4'):
                        personaje_actual = 'Kyon'
                        perso = 4
                    if(event.unicode == '5'):
                        personaje_actual = 'Lena'
                        perso = 5
                    if(event.unicode == '6'):
                        personaje_actual = 'Ondina'
                        perso = 6
                    if(event.unicode == '7'):
                        personaje_actual = 'Jorgen'
                        perso = 7
                    if(event.unicode == '8'):
                        personaje_actual = 'Aren'
                        perso = 8
                    if(event.unicode == '9'):
                        personaje_actual = 'Thor'
                        perso = 9
                    if(event.unicode == 'a'):
                        personaje_actual = 'Arthit'
                        perso = 10
                    if(event.unicode == 'b'):
                        personaje_actual = 'Sasithorn'
                        perso = 11
                    if(event.unicode == 'c'):
                        personaje_actual = 'Ubon'
                        perso = 12
                    if(event.unicode == 'd'):
                        personaje_actual = 'Sukhon'
                        perso = 13
                    if(event.unicode == 'e'):
                        personaje_actual = 'Pakpao'
                        perso = 14
                    if(event.unicode == 'f'):
                        personaje_actual = 'Ryu'
                        perso = 15
                    if(event.unicode == 'g'):
                        personaje_actual = 'Yoko'
                        perso = 16
                    if(event.unicode == 'h'):
                        personaje_actual = 'Riku'
                        perso = 17
                    if(event.unicode == 'i'):
                        personaje_actual = 'Sayaka'
                        perso = 18
                    if(event.unicode == 'j'):
                        personaje_actual = 'Toshio'
                        perso = 19
                    if(event.key == 32):
                        pantalla = 1


            msElapsed = clock.tick(30)

            screen.fill(black)

            message_to_screen('Seleccione un personaje:', yellow, 0, 0)
            message_to_screen('0.- Huo - Samurai Fuego', yellow, 0, 20)
            message_to_screen('1.- Shui - Samurai Agua', yellow, 0, 40)
            message_to_screen('2.- Tu - Samurai Tierra', yellow, 0, 60)
            message_to_screen('3.- Fei - Samurai Aire', yellow, 0, 80)
            message_to_screen('4.- Kyon - Samurai Rayo', yellow, 0, 100)
            message_to_screen('5.- Lena - Guerrero Fuego', yellow, 0, 120)
            message_to_screen('6.- Ondina - Guerrero Agua', yellow, 0, 140)
            message_to_screen('7.- Jorgen - Guerrero Tierra', yellow, 0, 160)
            message_to_screen('8.- Aren - Guerrero Aire', yellow, 0, 180)
            message_to_screen('9.- Thor - Guerrero Rayo', yellow, 0, 200)
            message_to_screen('a.- Arthit - KOer Fuego', yellow, 0, 220)
            message_to_screen('b.- Sasithorn - KOer Agua', yellow, 0, 240)
            message_to_screen('c.- Ubon - KOer Tierra', yellow, 0, 260)
            message_to_screen('d.- Sukhon - KOer Aire', yellow, 0, 280)
            message_to_screen('e.- Pakpao - KOer Rayo', yellow, 0, 300)
            message_to_screen('f.- Ryu - Asesino Fuego', yellow, 0, 320)
            message_to_screen('g.- Yoko - Asesino Agua', yellow, 0, 340)
            message_to_screen('h.- Riku - Asesino Tierra', yellow, 0, 360)
            message_to_screen('i.- Sayaka - Asesino Aire', yellow, 0, 380)
            message_to_screen('j.- Toshio - Asesino Rayo', yellow, 0, 400)
            message_to_screen('Para jugar presionar la barra esparcidora :)', yellow, 200, 450)
            message_to_screen('Personaje actual: '+personaje_actual, yellow, 300, 20)


            pygame.display.update()

        while(pantalla == 2):
            for event in pygame.event.get():
                #print(event)
                if(event.type == pygame.QUIT):
                    sys.exit()
                if(event.type == pygame.KEYDOWN):
                    if(event.unicode == '0'):
                        ataque_actual = 'GolpeFuego'
                    if(event.unicode == '1'):
                        ataque_actual = 'BolaFuego'
                    if(event.unicode == '2'):
                        ataque_actual = 'Llamarada'
                    if(event.unicode == '3'):
                        ataque_actual = 'Explosion'
                    if(event.unicode == '4'):
                        ataque_actual = 'GolpeRayo'
                    if(event.unicode == '5'):
                        ataque_actual = 'BolaRayo'
                    if(event.unicode == '6'):
                        ataque_actual = 'Relampago'
                    if(event.unicode == '7'):
                        ataque_actual = 'Tormenta'
                    if(event.unicode == '8'):
                        ataque_actual = 'GolpeAgua'
                    if(event.unicode == '9'):
                        ataque_actual = 'BolaAgua'
                    if(event.unicode == 'a'):
                        ataque_actual = 'Ciclon'
                    if(event.unicode == 'b'):
                        ataque_actual = 'Tsunami'
                    if(event.unicode == 'c'):
                        ataque_actual = 'GolpeAire'
                    if(event.unicode == 'd'):
                        ataque_actual = 'BolaAire'
                    if(event.unicode == 'e'):
                        ataque_actual = 'Ventisca'
                    if(event.unicode == 'f'):
                        ataque_actual = 'Tornado'
                    if(event.unicode == 'g'):
                        ataque_actual = 'GolpeRoca'
                    if(event.unicode == 'h'):
                        ataque_actual = 'BolaTierra'
                    if(event.unicode == 'i'):
                        ataque_actual = 'Derrumbe'
                    if(event.unicode == 'j'):
                        ataque_actual = 'Terremoto'
                    if(event.key == 32):
                        opo = random.randint(0, 20)
                        #print(opo)
                        #print(timer_1)
                        if(ataque_actual in mr):
                            pantalla = 1
                        else:
                            pantalla = 3

            if(timer_1 == 150):
                pantalla = 3

            msElapsed = clock.tick(30)

            screen.fill(black)

            message_to_screen('Oponente: '+listaOponentes[opo], yellow, 350, 50)
            message_to_screen('Ataque: '+ataque_actual, yellow, 350, 70)
            message_to_screen('Tu: '+personaje_actual, yellow, 400, 450)
            message_to_screen('Seleccione con que atacar:', yellow, 0, 0)
            message_to_screen('0.- GolpeFuego', yellow, 0, 20)
            message_to_screen('1.- BolaFuego', yellow, 0, 40)
            message_to_screen('2.- Llamarada', yellow, 0, 60)
            message_to_screen('3.- Explosion', yellow, 0, 80)
            message_to_screen('4.- GolpeRayo', yellow, 0, 100)
            message_to_screen('5.- BolaRayo', yellow, 0, 120)
            message_to_screen('6.- Relampago', yellow, 0, 140)
            message_to_screen('7.- Tormenta', yellow, 0, 160)
            message_to_screen('8.- GolpeAgua', yellow, 0, 180)
            message_to_screen('9.- BolaAgua', yellow, 0, 200)
            message_to_screen('a.- Ciclon', yellow, 0, 220)
            message_to_screen('b.- Tsunami', yellow, 0, 240)
            message_to_screen('c.- GolpeAire', yellow, 0, 260)
            message_to_screen('d.- BolaAire', yellow, 0, 280)
            message_to_screen('e.- Ventisca', yellow, 0, 300)
            message_to_screen('f.- Tornado', yellow, 0, 320)
            message_to_screen('g.- GolpeRoca', yellow, 0, 340)
            message_to_screen('h.- BolaTierra', yellow, 0, 360)
            message_to_screen('i.- Derrumbe', yellow, 0, 380)
            message_to_screen('j.- Terremoto', yellow, 0, 400)
            message_to_screen('Para atacar presionar la barra esparcidora :)', yellow, 50, 450)
            message_to_screen('Ataques recomendados: ', white, 325, 110)
            message_to_screen(mr[0], white, 325, 130)
            message_to_screen(mr[1], white, 325, 150)
            message_to_screen(mr[2], white, 325, 170)

            timer_1 += 1

            pygame.display.update()

        while(pantalla == 3):
            for event in pygame.event.get():
                #print(event)
                if(event.type == pygame.QUIT):
                    sys.exit()

            msElapsed = clock.tick(30)

            screen.fill(black)

            message_perdiste('YOU LOSE', red, 225, 225)
            message_perdiste('Puntaje: '+str(pointCounter), red, 225, 275)

            if(timer > 75):
                sys.exit()

            timer += 1

            pygame.display.update()

if(__name__ == '__main__'):
    main()
