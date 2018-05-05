import Heroe as h

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
        total_damage = total_damage*0.25
    #print(total_damage)
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
    print(str(life) + ' - ' + str(total_damage))
    if life-total_damage <= 0:
        return 0
    else:
        return life-total_damage

def Peso(h1, h2, poder):
    #print(CalculateDamage(h1, h2, poder))
    #print(RestLife(h2.vida, CalculateDamage(h1, h2, poder)))
    d_r = CalculateDamage(h1, h2, poder)*Recoil(CalculateDamage(h1, h2, poder), poder, h1)
    peso_total = d_r*EnergyLeft(h1, poder)
    return int(peso_total)

#def CalculateEnergy(hero1, poder):

s1 = h.Samurai('Jose', 'Rayo')
k1 = h.KOer('Antonio', 'Fuego')
s2 = h.Samurai('Kid', 'Fuego')
k2 = h.KOer('Jesus', 'Rayo')

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
