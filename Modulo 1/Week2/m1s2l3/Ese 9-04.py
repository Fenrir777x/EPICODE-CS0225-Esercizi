# Richiesta di Input: inserire il nome della città di origine e del proprio animale domestico
# Generare nome di una band utilizzando i nomi scritti in input stampato a video

import random

nome1=input("Inserire il nome della città di origine: ")
nome2=input("Inserire il nome dell'animale domestico: ")

band=(nome1 + " " + nome2)

print("Il nome della band potrebbe essere: ", band)

print("Utilizzando la libreria Random e le liste con i connettori si può ottenere questo")

parti=[nome1,nome2]

connettori=["dei","degli", "della", "del", "e i", "e le", "con gli", "con le"]

random.shuffle(parti)

if random.choice([True,False]):
    connettore_scelto=random.choice(connettori)
    if random.choice([True,False]):
        nome_band = f"{parti[0]} {connettore_scelto} {parti[1]}"
    else:
        nome_band = f"{parti[1]} {connettore_scelto} {parti[0]}"
else:
    nome_band = " ".join(parti)

print("Il nome della band potrebbe essere: ",nome_band)

