#include<stdio.h>
#include<stdlib.h>

// Dynamic memory allocation. It is done on Heap.
// Use of malloc,calloc,realloc and free

int main()
{

// Malloc has void ptr return type.Hence need to typecast.
//void ptr is generic ptr, and it cannot be derefernced.
int* ptr =(int*)malloc(sizeof(int));
printf("Address = %p\n",ptr);

*ptr = 10;
printf("Value of ptr = %d\n",*ptr);

// Always important to deallocate the memory
free(ptr);

printf("Address = %p\n",ptr);
printf("Value of ptr = %d\n",*ptr);	//This will give garbage value

ptr = (int*)malloc(sizeof(int));
*ptr=20;
printf("Value of ptr = %d\n",*ptr);	//This will give garbage value

free(ptr);

printf("========== Arrays ====================\n");

// Malloc returns NULL if it does not find any memory to allocate. We need error handling for that.

// Array of 5 elements

int* arr = (int*)malloc(5*sizeof(int));

for(int i = 0; i<5; i++)
{
	arr[i] = i+1;
}

//free(arr);
for(int i = 0; i<5; i++)
{
	printf("%d\n",arr[i]);

}

free(ptr);

printf("========== Calloc ====================\n");

int n;
printf("Enter the size of an array...\n");
scanf("%d",&n);


int* cal = (int*)calloc(n,sizeof(int));

// Calloc initializes the array values by 0.
for(int i = 0; i<n; i++)
{
	cal[i] = i+1;
}
printf("\n");

printf("========== Realloc ====================\n");

// Realloc extends the block of memory allocated thru malloc and calloc
cal = (int*)realloc(cal,2*n*sizeof(int));

//int* re = (int*)realloc(cal,2*n*sizeof(int));
//int* re = (int*)realloc(cal,0);
//int* re = (int*)realloc(NULL,2*n*sizeof(int)); //This is equivalent to malloc

//printf("Addr1 %p\n",cal);
//printf("Addr2 %p\n",re);//This will be same address

for(int i = 0; i<2*n; i++)
{
	printf("%d\t",cal[i]);
}

//free(re);

free(cal);

printf("\n");



}
