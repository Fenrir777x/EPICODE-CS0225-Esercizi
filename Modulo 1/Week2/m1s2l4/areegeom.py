import math

def area_quadrato(lato):
    if lato < 0:
        return "Errore: il lato deve essere non negativo."
    return lato ** 2

def circonferenza(raggio):
    if raggio < 0:
        return "Errore: il raggio deve essere non negativo."
    return 2 * math.pi * raggio

def area_rettangolo(base, altezza):
    if base < 0 or altezza < 0:
        return "Errore: la base e l'altezza devono essere non negative."
    return base * altezza

def perimetro_cerchio(raggio):
    if raggio < 0:
        return "Errore: il raggio deve essere non negativo."
    return 2 * math.pi * raggio

def perimetro_quadrato(lato):
    if lato < 0:
        return "Errore: il lato deve essere non negativo."
    return 4 * lato

def perimetro_rettangolo(base, altezza):
    if base < 0 or altezza < 0:
        return "Errore: la base e l'altezza devono essere non negative."
    return 2 * (base + altezza)