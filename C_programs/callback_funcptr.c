#include<stdio.h>
#include<stdlib.h>

// Callback = Calling a function through function pointer.

void A()
{
printf("Welcome to function ptr callback\n");
}

void B(void (*ptr)())	//function ptr as argument.
{
ptr();			//callback function that ptr points to.
}


int main()
{

//void (*p)() = A;
//B(p);

//OR

B(A);	// 'A' is a callback function.

}
