#include "stdio.h"
#include "stdlib.h"
#include "stdint.h"

void allocMemoryDumbWay(int **p)
{
        *p = (int *)malloc(sizeof(int));
    
}

int main()
{
    
   int *p = NULL;

   if( p == NULL)
   {
       allocMemoryDumbWay(&p);
   }
   
   if( p == NULL)
   {
    perror("Error: ");
    return -1;
   }

   printf("memory address %ld\n", p);
   printf("value in the memory address %d\n", *p);

}