//PROGRAMAÇÃO MODULAR 
#include <stdio.h>
int main()
{	
	// DECLARAÇÃO DAS VARIÁVEIS 	
    int teste,teste2,teste3,teste4,l,c;              
	// DECLARAÇÃO DA ARRAY(BIDIMENSIONAL)/MATRIZ
    int matriz[4][4] =  {1, 2, 3, 4, 2, 1, 4, 3, 3, 4, 1, 2, 4, 3, 2, 1};  
    
	
	// RETORNO DAS FUNÇÕES 
    	void percorrendo(int x[4][4],int teste); // FUNÇÕES QUE PERCORREM E TESTAM SE A MULTIPLICAÇÃO DOS ELEMENTOS DE LINHA E COLUNA SÃO IGUAIS 
	percorrendo(matriz,teste);
	
	void percorrendo2(int x[4][4],int teste2);
	percorrendo2(matriz,teste2);
	
	void percorrendo3(int x[][4],int teste3);
	percorrendo3(matriz,teste3);
	
	void percorrendo4(int x[][4],int teste4);
	percorrendo4(matriz,teste4);
	
	
	// FUNÇÃO QUE TESTA SE É QUADRADO HOLÂNDES 
	void seEHholandes(int teste,int teste2,int teste3,int teste4);
	seEHholandes(teste,teste2,teste3,teste4);
	

}

// FUNÇÕES QUE PERCORREM CADA LINHA E COLUNA 

void percorrendo (int x[][4],int teste)
{
	int l, c;
/*	for (l=0;l<4;++l){
		for(c=0;c<4;++c){
			printf("%d   ", x[l][c]);
		}
		printf("\n");
	}*/
	
    for ( l=0;l<1;++l){
        for (c=0;c<4;++c){
//            printf("%d,",x[l][c]);	// PRIMEIRA LINHA/COLUNA E GUARDA O RESULTADO
        }
        teste = x[0][0] * x[0][1] * x[0][2] * x[0][3];  
        printf("\n%d", teste);
    }
}    

void percorrendo2(int x[][4],int teste2)
{
    int l,c;
    for (l=0;l<2;++l){
        for(c=0;c<4;++c){
//           printf("%d  ",x[l][c]);	// SEGUNDA LINHA/COLUNA E GUARDA O RESULTADO
        }
        teste2 =  x[1][0] * x[1][1] * x[1][2] * x[1][3] ; 
       printf("\n\n%d"  ,teste2);
    }
    
}

void percorrendo3(int x[][4],int teste3)
{
    int l,c;
    for (l=0;l<3;++l){
        for(c=0;c<4;++c){
//          printf("%d  ",x[l][c]);	// TERCEIRA LINHA/COLUNA E GUARDA O RESULTADO
        }
        teste3 = x[2][0] * x[2][1] * x[2][2] * x[2][3] ;
        printf("\n\n%d"  ,teste3);
    }
    
}

void percorrendo4(int x[][4],int teste4)
{
    int l,c;
    for (l=0;l<4;++l){
        for(c=0;c<4;++c){
//          printf("%d  ",x[l][c]);   // QUARTA LINHA/COLUNA E GUARDA O RESULTADO
        }
        teste4 =  x[3][0] * x[3][1] * x[3][2] * x[3][3] ;
        printf("\n\n%d"  ,teste4);
    }
    
}

void seEHholandes(int teste,int teste2,int teste3,int teste4) // FUNÇÃO COM CONDIÇÃO PARA SER Q.H
{
    
    if (teste == teste2 == teste3 == teste4  ){
        printf("É UM QUADRADO HOLÂNDES");
    }
    
    
    else{
        printf("NÃO É UM QUADRADO HOLÂNDES");
    }

}
