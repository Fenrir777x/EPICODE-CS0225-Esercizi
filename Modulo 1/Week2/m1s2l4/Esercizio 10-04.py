#Si scriva un programma in Python che in base alla scelta dellʼutente
# permetta di calcolare il perimetro di diverse figure geometriche

from areegeom import *
import math
def menu():
    print("\n--- Menù Matematico ---")
    print("1 - Calcola Area e Perimetro")
    print("2 - Esci")

def calcola_area_perimetro():
    while True:
        print("\n--- Calcola Area e Perimetro di ---")
        print("1 - Quadrato")
        print("2 - Cerchio")
        print("3 - Rettangolo")
        print("4 - Torna al menu principale")
        scelta_figura = input("Inserisci la tua scelta: ")

        if scelta_figura == '1':
            try:
                lato = float(input("Inserisci il lato del quadrato: "))
                area = area_quadrato(lato)
                perimetro = perimetro_quadrato(lato)
                print(f"L'area del quadrato è: {area}") if not isinstance(area, str) else print(area)
                print(f"Il perimetro del quadrato è: {perimetro}") if not isinstance(perimetro, str) else print(perimetro)
            except ValueError:
                print("Input non valido.")
        elif scelta_figura == '2':
            try:
                raggio = float(input("Inserisci il raggio del cerchio: "))
                area = math.pi * raggio**2
                perimetro = perimetro_cerchio(raggio)
                print(f"L'area del cerchio è: {area:.2f}")
                print(f"La circonferenza del cerchio è: {perimetro:.2f}") if not isinstance(perimetro, str) else print(perimetro)
            except ValueError:
                print("Input non valido.")
        elif scelta_figura == '3':
            try:
                base = float(input("Inserisci la base del rettangolo: "))
                altezza = float(input("Inserisci l'altezza del rettangolo: "))
                area = area_rettangolo(base, altezza)
                perimetro = perimetro_rettangolo(base, altezza)
                print(f"L'area del rettangolo è: {area}") if not isinstance(area, str) else print(area)
                print(f"Il perimetro del rettangolo è: {perimetro}") if not isinstance(perimetro, str) else print(perimetro)
            except ValueError:
                print("Input non valido.")
        elif scelta_figura == '4':
            break
        else:
            print("Scelta non valida.")

def main():
    while True:
        menu()
        scelta_principale = input("Inserisci la tua scelta: ")
        if scelta_principale == '1':
            calcola_area_perimetro()
        elif scelta_principale == '2':
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()