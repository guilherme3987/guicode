//PROGRAMAÇÃO MODULAR 
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
int main(){

    int **Pontmat,linha,coluna, i, j;


    //ENTRADAS DE DADOS
    printf("QUANTIDADDE DE LINHAS: ");
    scanf("%d  ",&linha);
    printf("\n");
    printf("QUANTIDADE DE COLUNAS:  ");
    scanf("%d  ",&coluna);

    //RETORNO DAS FUNÇÕES
    int aloc_memoria(int Pontmat,int i,int linha,int coluna);
    aloc_memoria(Pontmat,i,linha,coluna);



    int imprimir_mat(int Pontmat,int i,int j);
    imprimir_mat(Pontmat,i,j);


}
//ALOCAÇÃO DINÂMICA DE MEMÓRIA
int aloc_memoria(int Pontmat,int i,int linha,int coluna)
{
    Pontmat = malloc(linha * sizeof(int*));
    for(i = 0; i < coluna; i++){
        Pontmat[i] = malloc(coluna * sizeof(int));
    }
}

int imprimir_mat(int Pontmat,int i,int j)
{
        //MATRIZ DE NÚMEROS INTEIROS
    for(i = 0; i < linha; i++){
        for(j = 0; j < coluna; j++)
            Pontmat[i][j] = i+j;
    }
    for(i = 0; i < linha; i++){
        for(j = 0; j < coluna; j++)
            printf("%d   ", Pontmat[i][j]);
        printf("\n ");
    }

    free(Pontmat);
}
