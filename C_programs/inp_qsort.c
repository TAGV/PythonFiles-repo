#include<stdio.h>
#include<stdlib.h>

void print(int* arr,int size)
{
	for(int i = 0; i<size; i++)
	{
		printf("%d\t",arr[i]);
	}
	printf("\n");
}

int ascending(const void* A, const void* B)
{
//printf("Sorted in increasing order\n");
int x = *((int*)A);
int y = *((int*)B);
return x-y;
}

int descending(const void* A, const void* B)
{
//printf("Sorted in decreasing order\n");
int x = *((int*)A);
int y = *((int*)B);
return y-x;
}


int main()
{

int size;
printf("Enter the size of the array....\n");
scanf("%d",&size);

int* arr = (int*)malloc(size*sizeof(int));

//Take array inputs from the user.
int ele;
for(int i = 0; i<size; i++)
{
printf("Enter element %d\t : ",i+1);
scanf("%d",&ele);
arr[i] = ele;
}

//Print the array
print(arr,size);

//Sort the array
//qsort(arr,size,sizeof(int),ascending);
qsort(arr,size,sizeof(int),descending);

//Print the sorted array
print(arr,size);


free(arr);
}
