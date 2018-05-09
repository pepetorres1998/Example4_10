import Heroe as h

def calcular_elementos_poder(h2, poder, total_damage):
    if(poder.element == 'Fuego' and h2.element == 'Agua'):
        return total_damage*0
    elif(poder.element == 'Fuego' and h2.element == 'Aire'):
        return total_damage*2
    elif(poder.element == 'Agua' and h2.element == 'Rayo'):
        return total_damage*0
    elif(poder.element == 'Agua' and h2.element == 'Fuego'):
        return total_damage*2
    elif(poder.element == 'Rayo' and h2.element == 'Tierra'):
        return total_damage*0
    elif(poder.element == 'Rayo' and h2.element == 'Agua'):
        return total_damage*2
    elif(poder.element == 'Tierra' and h2.element == 'Aire'):
        return total_damage*0
    elif(poder.element == 'Tierra' and h2.element == 'Rayo'):
        return total_damage*2
    elif(poder.element == 'Aire' and h2.element == 'Fuego'):
        return total_damage*0
    elif(poder.element == 'Aire' and h2.element == 'Tierra'):
        return total_damage*2
    else:
        return total_damage

def CalculateDamage(h1, h2, poder):
    damage = h1.ataque*poder.damage
    #print(damage)
    resistence = (h2.defensa - 1)*damage
    if(h1.element == h2.element):
        resistence = resistence*1.5
    total_damage = (damage-resistence)
    #print(total_damage)
    if(h1.element == poder.element):
        total_damage = total_damage*1.25
    #print(total_damage)
    if(poder.element == h2.element):
        total_damage = total_damage*0
    #print(total_damage)
    total_damage = calcular_elementos_poder(h2, poder, total_damage)
    return total_damage

def Recoil(total_damage, poder, h1):
    if((h1.vida - (total_damage*poder.recoil)) <= 0):
        return 0
    else:
        return 1

def EnergyLeft(h1, poder):
    if(h1.energia - poder.consumo < 0):
        return 0
    else:
        return 1

def RestLife(life, total_damage):
    #print(str(life) + ' - ' + str(total_damage))
    if life-total_damage <= 0:
        return 0
    else:
        return life-total_damage

def RestOwnLife(life, recoil):
    if life-recoil <= 0:
        return 0
    else:
        return life-recoil

def Peso(h1, h2, poder):
    #print(CalculateDamage(h1, h2, poder))
    #print(RestLife(h2.vida, CalculateDamage(h1, h2, poder)))
    d_r = CalculateDamage(h1, h2, poder)*Recoil(CalculateDamage(h1, h2, poder), poder, h1)
    peso_total = d_r*EnergyLeft(h1, poder)
    return int(peso_total)

#def CalculateEnergy(hero1, poder):

KOer_fuego = h.KOer('Arthit', 'Fuego')
KOer_agua = h.KOer('Sasithorn', 'Agua')
KOer_tierra = h.KOer('Ubon', 'Tierra')
KOer_rayo = h.KOer('Pakpao', 'Rayo')
KOer_aire = h.KOer('Sukhon', 'Aire')

Samurai_fuego = h.Samurai('Huo', 'Fuego')
Samurai_agua = h.Samurai('Shui', 'Agua')
Samurai_tierra = h.Samurai('Tu', 'Tierra')
Samurai_rayo = h.Samurai('Kyon', 'Rayo')
Samurai_aire = h.Samurai('Fei', 'Aire')

Asesino_fuego = h.Asesino('Ryu', 'Fuego')
Asesino_agua = h.Asesino('Yoko', 'Agua')
Asesino_tierra = h.Asesino('Riku', 'Tierra')
Asesino_rayo = h.Asesino('Toshio', 'Rayo')
Asesino_aire = h.Asesino('Sayaka', 'Aire')

Guerrero_fuego = h.Guerrero('Lena', 'Fuego')
Guerrero_agua = h.Guerrero('Ondina', 'Agua')
Guerrero_tierra = h.Guerrero('Jorgen', 'Tierra')
Guerrero_rayo = h.Guerrero('Thor', 'Rayo')
Guerrero_aire = h.Guerrero('Aren', 'Aire')

#FUEGO
GolpeFuego = h.GolpeFuego()
BolaFuego = h.BolaFuego()
Llamarada = h.Llamarada()
Explosion = h.Explosion()

#RAYO
Tormenta = h.Tormenta()

#print(CalculateDamage(k1, s2, Explosion))
#print(RestLife(s2.vida, CalculateDamage(k1, s2, Tormenta)))
if(__name__ == '__main__'):
    print(Peso(k1, s2, Tormenta))
    print(Peso(k1, s2, Explosion))
    print(Peso(k1, s1, Explosion))
    print(Peso(k1, s1, Llamarada))
