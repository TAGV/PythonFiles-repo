#include<stdio.h>

//Points to Note:
// 1. Arrays are always passed to function as pass by reference,i.e. their address is passed as an args.
// 2. Both the notations are hence applicable : int A[] = int* A

//Function to add numbers of the array

int array_sum(int A[],int size)
{
	//printf("In AYS: %d\n",A[0]);
	int sum = 0;
	for(int i = 0; i<size; i++)
	{
		sum = sum + A[i];

	}
return sum;
}

//Function to double the value of elements in the array

void double_array(int* A,int size)
{
	for(int i = 0;i<size;i++)
	{
		A[i] = A[i]*2;
	}

}

void print_array(int* A,int size)
{
	for(int i = 0;i<size;i++)
	{
		printf("%d\t",A[i]);
	}

}


int main()
{

int sumArray[] = {1,2,3,4,5,6,7,8,9,10};

int size = sizeof(sumArray)/sizeof(sumArray[0]);
printf("Size of array = %d\n",size);


printf("Total sum = %d\n",array_sum(sumArray,size));


print_array(sumArray,size);
printf("\n");
double_array(sumArray,size);
print_array(sumArray,size);
printf("\n");
printf("Total sum = %d\n",array_sum(sumArray,size));

}
