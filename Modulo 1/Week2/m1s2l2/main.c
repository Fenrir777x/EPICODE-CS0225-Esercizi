#include <stdio.h>

int main() {
    int num1;
    int num2;
    int moltiplicazione;
    float media;
    
    printf("Inserisci il primo numero: \n");
    scanf("%d", &num1);
    
    printf("Inserisci il secondo numero: \n");
    scanf("%d", &num2);
    
    moltiplicazione = num1 * num2;
    printf("La moltiplicazione dei due numeri è: %d\n",moltiplicazione);
    media = (float) (num1+num2)/2;
    printf("La media dei due numeri scelti è: %f\n", media);
    
    return 0;
    
}