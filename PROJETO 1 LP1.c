// ====== ALGORITIMO FINAL DE CORREÇÃO DE PROVAS ==========
//bibliotecas 
#include <stdio.h>
#include <stdlib.h>
#include <time.h> 
//declaração de constantes
#define TAM 9999    
#define notas 10  

// estrutura de dados da função time da biblioteca <time.h>
struct tm *data_hora_atual;
time_t segundos;



int main() {
  //variáveis 
  int quantidade_de_provas;     
  int acertos = 0;
  int numero_do_aluno = 0;
  float p;
  
  //vetores: vetor para o gabarito,respostas e frequência
  char gabarito[18]= {"AAAABBBBBB"};
  char respostas[10];      

  int freq[10];  
    

//entrada de dados 
  printf("----| CORREÇÃO DE PROVAS |---- \nDigite o numero de provas a serem corrigidas: ");
  scanf("%d", &quantidade_de_provas);
  printf("Seram corrigidas %d provas ",quantidade_de_provas);

  //condição para acesso
    if(numero_do_aluno<TAM){
        printf("\nALUNO JÁ CADASTRADO \n");

  //laço para digitar as 10 respostas de x  alunos  
        for (int x = 1; x <= quantidade_de_provas; x++) {
          
             printf("\nDigíte o número do aluno\n");
               scanf("%d",&numero_do_aluno);
               if(numero_do_aluno<TAM){
                  printf("\nALUNO CADASTRADO\nDigite as respostas do aluno %d: ", numero_do_aluno);
                  
                 //retorno da função que corriga e retorna os dados de correção  
                    void corrigindo(int numero_do_aluno,int acertos,float p,int *freq,int quantidade_de_provas,char *respostas,char *gabarito);
                        corrigindo(numero_do_aluno,acertos,p,freq,quantidade_de_provas,respostas,gabarito);
                
                }
                else{
                    printf("INVÁLIDO");
                
                }

        }
     
    }
    else{
        printf("INVÁLIDO");
    }
  
 //declarar data  
time(&segundos);
data_hora_atual = localtime(&segundos); 
printf("%d  %d  %d \n", data_hora_atual->tm_mday, data_hora_atual->tm_mon+1,data_hora_atual->tm_year+1900);  



  
}
//declaração da função   "tipo da função (tipo dos paramentros) "
void corrigindo(int numero_do_aluno,int acertos,float p,int *freq ,int quantidade_de_provas,char *respostas,char *gabarito){
  for(int y=0;y<10;y++){
        scanf(" %c", &respostas[y]); 
        if (respostas[y] == gabarito[y]){
            acertos = acertos + 1;
            freq[y] = acertos;
        }
        p = (acertos/freq[y])*100;
    }
    
    printf("\n\n----------- DADOS DA CORREÇÃO --------------");

  //condição para aprovação 
    if(acertos >=6){
        printf("\nAPROVADO");

    }
    else{
        printf("\nREPROVADO");

    }
    
        
     printf("\nPORCENTAGEM DE ACERTOS POR QUESTÃO: %0.2f",p);
    printf("\nO aluno %d fez %d pontos\n", numero_do_aluno, acertos);
    printf("------------------------------------------\n\n");
}
