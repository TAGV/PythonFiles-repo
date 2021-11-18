#include<stdio.h>

//Note
// Type of pointer matters when we want to dereference and does not matter when we just want to read the address
int main()
{

// This are two 1d arrays containing 3 integers each
//A[0]
//A[1]

int A[2][3] = {10,20,30,
	       40,50,60};

//Way to define a pointer to 1-d array of 3 integers like this
int (*ptr)[3] = A;

// Base address printing of 1st 1-d array
printf("%p\n",ptr);
printf("%p\n",A);	//'A' is returning a ptr to 1-d array of 3 integers
printf("%p\n",&A[0]);
printf("%p\n",A[0]);
printf("%p\n",*A);	//'*A' is returning the ptr to an integer
printf("%p\n",&A[0][0]);

printf("========== 2nd Array ================\n");
// Base address printing of 2nd 1-d array(increment by 3*4=12 bytes)
// Every statement returns an integer pointer
printf("%p\n",ptr+1);
printf("%p\n",A+1);
printf("%p\n",&A[1]);
printf("%p\n",A[1]);
printf("%p\n",*(A+1));
printf("%p\n",&A[1][0]);

printf("========== Pointer Arithmetic ================\n");
//Accessing the last elemnt in the 2d array
printf("%p\n",A[1]+2);
printf("%p\n",*(A+1)+2);
printf("%p\n",&A[1][2]);

printf("========== Printing Elements in the array ================\n");
printf("%d\n",*(*A)); //~10
printf("%d\n",*(*A+1)); //~20
printf("%d\n",*(*A+2)); //~30
printf("%d\n",*(*A+3)); //~40
printf("%d\n",*(*A+4)); //~50
printf("%d\n",*(*A+5)); //~60

//For any 2d array:
//B[i][j] = *(B[i]+j)
//	  = *(*(B+i)+j)
printf("========== Printing Elements in the array(Other Notations: *(B[i]+j)) ================\n");
printf("%d\n",*(A[0])); //~10
printf("%d\n",*(A[0]+1)); //~20
printf("%d\n\n",*(A[0]+2)); //~30

printf("%d\n",*(A[1])); //~40
printf("%d\n",*(A[1]+1)); //~50
printf("%d\n",*(A[1]+2)); //~60

printf("========== Printing Elements in the array(Other Notations: using ptr ================\n");
printf("%d\n",*(*ptr)); //~10
printf("%d\n",*(*ptr+1)); //~20
printf("%d\n",*(*ptr+2)); //~30
printf("%d\n",*(*ptr+3)); //~40
printf("%d\n",*(*ptr+4)); //~50
printf("%d\n",*(*ptr+5)); //~60

//2nd row printing
printf("%d\n",*(*(ptr+1))); //~40
printf("%d\n",*(*(ptr+1)+1)); //~50
printf("%d\n",*(*(ptr+1)+2)); //~60

//1st row printing in reverse
printf("%d\n",*(*(ptr+1)-1)); //~30
printf("%d\n",*(*(ptr+1)-2)); //~20
printf("%d\n",*(*(ptr+1)-3)); //~10


}
