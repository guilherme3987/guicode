//COMPACTAÇÃO DE MATRIZES 
#include <stdio.h>
int main() {
    int tam,tam2;
    int matriz[4][4] =  {1, 2, 3, 4, 2, 1, 4, 3, 3, 4, 1, 2, 4, 3, 2, 1};
    
    for (int i = 0; i < 4; ++i){
        for(int c = 0;c<4;++c){
            printf("%d ", matriz[i][c]);
        }
    }
    printf("\n");
    
    int tamanhoV(int tam,int x[][4]);
    tamanhoV(tam,matriz);

    int tamanhoREAL(int tam2,int x[][4]);
    tamanhoREAL(tam2,matriz);
}

int tamanhoV(int tam,int x[][4])
{
    int matriz[4][4] =  {1, 2, 3, 4, 2, 1, 4, 3, 3, 4, 1, 2, 4, 3, 2, 1};
    tam = sizeof(matriz);
    printf("%d\n",tam);
}

int tamanhoREAL(int tam2,int x[][4])
{
    tam2 = sizeof(int) ;
    printf("%d",tam2 );
}

