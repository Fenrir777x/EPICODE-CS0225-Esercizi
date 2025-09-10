#Esercizio 1: Numero pari o dispari Scrivi un programma che chieda un numero all utente e determini se è pari o dispari

num=int(input("Inserisci un numero: "))
if num%2==0:
    print("Il numero scritto è pari")
else:
    print("Il numero scritto è dispari")


#Esercizio 2: Calcolo della media Scrivi un programma che chieda tre numeri all utente e calcoli la loro media

numeri=[]

for i in range(6):
    risposta=input("Vuoi inserire un numero(Y/N): ")
    if risposta.lower()=="Y":
        while True:
            try:
                num=int(input("Inserisci il numero: "))
                numeri.append(num)
                break
            except ValueError:
                print("Input non valido. Riprova")
    else:
        break
if numeri:
    media=sum(numeri)/len(numeri)
    print(f"I numeri inseriti sono: {numeri}")
    print(f"La madia di questi numeri è: {media}")
else:
    print("Non hai inserito numeri")

#Esercizio 3: Tabellina di un numero Scrivi un programma che chieda un numero all utente e stampi la sua tabellina fino a 10.

num=int(input("Inserisci il numero del quale vuoi la tabellina: "))
tabellina=[]

for i in range(1,11):
    mol=num*i
    tabellina.append(mol)

print(tabellina)

#Esercizio 4: Contare vocali in una stringa Scrivi un programma che chieda una stringa e conti il numero di vocali presenti.

def conta_vocali(stringa):
    vocali="aeiou"
    conta=0
    stringa_maiuscola=stringa.lower()
    for carattere in stringa_maiuscola:
        if carattere in vocali:
            conta+=1
    return conta

testo=input("Inserisci il testo: ")
numvocali=conta_vocali(testo)

print(f"Il testo inserito contiene {numvocali} vocali")

#Esercizio 5: Trova il massimo in una lista Scrivi un programma che chieda all'utente una lista di numeri e trovi il massimo.

def trova_massimo_da_input():
  numeri = []
  print("Inserisci i numeri uno alla volta. Digita 'fine' per terminare.")

  while True:
    input_str = input("Inserisci un numero (o 'fine'): ").lower()
    if input_str == 'fine':
      break
    try:
      numero = float(input_str)
      numeri.append(numero)
    except ValueError:
      print("Input non valido. Inserisci un numero o 'fine'.")

  if not numeri:
    print("Non hai inserito alcun numero.")
    return None
  else:
    massimo = numeri[0]
    for num in numeri:
      if num > massimo:
        massimo = num
    print(f"Il numero massimo inserito è: {massimo}")
    return massimo

if __name__ == "__main__":
  trova_massimo_da_input()

#Esercizio 6: Invertire una stringa Scrivi un programma che chieda una stringa e la stampi al contrario.

testo=input("Inserisci il testo: ")
inverso=testo[::-1]
print(inverso)