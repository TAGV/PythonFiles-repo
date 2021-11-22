#include<stdio.h>
#include<stdlib.h>

void print()
{

	printf("Hello\n");


}

int* addnum(int* a, int* b)
{
	//Malloc is necessary to create space on heap.
	//Else it causes seg fault when returning address of local vars from stack itself
	int* sum = (int*)malloc(sizeof(int));
	*sum = (*a) + (*b);
	return sum;
}

int main()
{
	int a = 5;
	int b = 10;
	int* c = addnum(&a,&b);
	print();
	printf("Sum : %d\n",*c);



}
