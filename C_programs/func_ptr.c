#include<stdio.h>
#include<stdlib.h>

void simpleprint()
{
	printf("Welcome to function pointers..Enjoy!!!\n");
}

void strprint(char* mesg)
{
	printf("Congratulations...%s\n",mesg);
}

int add(int a, int b)
{
	return a + b;

}

int* multiply(int* a,int* b)
{
	int* c = (int*)malloc(sizeof(int));
	*c = (*a) * (*b);
	return c;
//malloc needs not to be freed, since function exit, the memory will be deallocated
}


int main()
{
//Declaring a function ptr
// 1. declare the return type
// 2. then provide the ptr name
// 3. Give the arguments as the real function signature

void (*print)();
print = simpleprint;
print();

void (*str)(char*);
str = strprint;
str("Roger");


int (*ptr)(int,int);
ptr = add;
int result = ptr(5,5);
printf("The Sum = %d\n",result);

int c = 100;
int d = 500;
int* (*mult)(int*,int*);
mult = multiply;
int* res = mult(&c,&d);
printf("The multiplication result = %d\n",*res);


}
