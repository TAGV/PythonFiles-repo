#include<stdio.h>
#include<stdlib.h>

//qsort takes in generic arguments,hence void ptr is used and passed here by refernce
int in_ascending(const void* a,const void* b)
{
int x = *((int*)a);	//typecast and then dereference
int y = *((int*)b);

//if x-y is positive,returns 1
//if  x-y is negative,returns -1
//if x-y is equal returns 0
return x-y;
}

int in_descending(const void* a,const void* b)
{
int x = *((int*)a);	//typecast and then dereference
int y = *((int*)b);

return y-x;
}

int in_abs_ascending(const void* a,const void* b)
{
int x = *((int*)a);	//typecast and then dereference
int y = *((int*)b);

//if x-y is positive,returns 1
//if  x-y is negative,returns -1
//if x-y is equal returns 0
return abs(x)-abs(y);
}

int in_abs_descending(const void* a,const void* b)
{
int x = *((int*)a);	//typecast and then dereference
int y = *((int*)b);

//if x-y is positive,returns 1
//if  x-y is negative,returns -1
//if x-y is equal returns 0
return abs(y)-abs(x);
}


int main()
{

// Create an integer array
int arr[] = {10,4,-5,2,-11,23,0};

//Calling builtin qsort func.
// 1st arg = Name of array
// 2nd arg = No of elements
// 3rd arg = sizeof(datatype)
// 4th arg = Writing our own compare function and passing here as function pointer.

qsort(arr,7,sizeof(int),in_ascending);
//qsort(arr,7,sizeof(int),in_descending);
//qsort(arr,7,sizeof(int),in_abs_ascending);
//qsort(arr,7,sizeof(int),in_abs_descending);

//Printing the sorted array
for(int i = 0; i<7; i++)
{
printf("%d\t",arr[i]);
}

printf("\n");

}
