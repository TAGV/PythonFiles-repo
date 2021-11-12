#include<stdio.h>

int main()
{


//Declaring an array

int arr[] = {1,2,4,5,3,4,5};

printf("%ld\n",sizeof(arr));

int n = sizeof(arr)/sizeof(int);
printf("%d\n",n);

for(int i = 0; i<7; i++)
{
printf("%d\t",arr[i]);
}



printf("\n\n===========Pointers Start=========\n");

//Start Address
//printf("%p\n",arr);

// 1st method
for(int j = 0; j<n; j++)
{
	printf("%p\t",arr+j);//Printing the addresses
	printf("%d\t",*(arr+j));//Printing the values
	printf("\n");

}
//arr++; This is invalid

// 2nd method

printf("========================\n");

for(int j = 0; j<n; j++)
{
	printf("%p\t",&arr[j]);//Printing the addresses
	printf("%d\t",arr[j]);//Printing the values
	printf("\n");
}

// 3rd method

printf("========================\n");

int * p;
p = arr; //Base Address of the array is assigned to the pointer

//printf("%p\n",p);

for(int k = 0; k<n; k++)
{
	printf("%p\t",p+k);//Printing the addresses
	printf("%d\t",*(p+k));//Printing the values
	printf("\n");

}

//p++; This is valid notation

}
