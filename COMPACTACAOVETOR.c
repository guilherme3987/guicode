//PROGRAMAÇÃO MODULAR
#include <stdio.h>
int main() {
    int tam,tam2;
    int vet1[] = {-2,-1,0,1,2,3,4,5,6,7,8,9,10};
    
    for (int i = 0; i < 6; ++i){
        printf("%d ", vet1[i]);
    }
    printf("\n");
    
    int tamanhoV(int tam,int x[]);
    tamanhoV(tam,vet1);*/

    int tamanhoREAL(int tam2,int x[]);
    tamanhoREAL(tam2,vet1);
}

int tamanhoV(int tam,int x[])
{
    int vet1[] = {-2,-1,0,1,2,3,4,5,6,7,8,9,10};
    tam = sizeof(vet1);
    printf("%d\n",tam);
}

int tamanhoREAL(int tam2,int x[])
{
    tam2 = sizeof(int) ;
    printf("%d",tam2 );
}
