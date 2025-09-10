#Scrivi una funzione che calcoli la media mobile di una lista di numeri.
#La media mobile di un elemento è definita come la media degli ultimi n elementi della lista, inclusi l'elemento corrente.

def media_mobile(lista_num, n):
    if not lista_num or not isinstance(n, int) or n<=0:
        return[]
    medie_mobili=[]
    for i in range(len(lista_num)):
        finestra=lista_num[max(0, i - n + 1):i + 1]
        media=sum(finestra)/len(finestra)
        medie_mobili.append(media)
    return medie_mobili

num=[1,2,3,4,5,6,7,8,9,10]
dimf=3
medie=media_mobile(num,dimf)
print(f"Lista Originale: {num}")
print(f"Media mobile (finestra={dimf}):{medie}")

numeri_vuoti=[]
medie_v=media_mobile(numeri_vuoti,2)
print(f"Lista Originale: {numeri_vuoti}")
print(f"Media mobile (finestra=2):{medie_v}")




#Scrivere una funzione che analizza una stringa di testo e restituisca un dizionario con il conteggio delle occorrenze
#di ciascuna parola, le parole vanno considerate case-sensitive

import re

def conta_parole(testo):
    testo_minuscolo=testo.lower()
    testo_pulito=re.sub(r'[^\w\s]','',testo_minuscolo)
    parole=testo_pulito.split()
    contap={}
    for parola in parole:
        if parola in contap:
            contap[parola]+= 1
        else:
            contap[parola]= 1
    return contap

testo=input("Inserisci testo che vuoi analizzare: ")
ris=conta_parole(testo)

print(ris)