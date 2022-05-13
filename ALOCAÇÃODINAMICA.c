#include <stdio.h>
#include <stdlib.h> //necessário para usar as funções malloc() e free()
#include <conio.h>
int main()
{
  int *pont, n_elementos,i;

  printf("QUANTOS ELEMENTOS SERAM ARMAZENADOS: ");
  scanf("%d", &n_elementos);

  pont = (int *) malloc(n_elementos * sizeof(int));


  for ( i = 0; i < n_elementos; i++)
  {
    printf("\nELEMENTO: ", i);
    scanf("%d",&pont[i]);
  }

  printf("DADOS ARMAZENADOS  ");
  for (i = 0;i < n_elementos; i++)
  {

      printf("%d  ",pont[i]);
  }


  free(pont);

  getch();
  return 0;
}
