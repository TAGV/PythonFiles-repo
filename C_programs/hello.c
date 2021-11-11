#include<stdio.h>
#include<stdlib.h>

int main()
{

int a;
a = 1025;
int *p;
p = &a;

// Pointer var are strongly typed: below code shows warning
int b = 1025;//This is a 2 byte number
char * d = &b;
printf("%p\n",d);
printf("%d\n",*d);//Only 1 byte will be printed


printf("hello world");
printf("\n");

printf("%d\n",a);
printf("%p\n",p);
printf("%d\n",*p);

//Pointer arithmetic

printf("%p\n",p);
printf("%lu\n",sizeof(int));
printf("%lu\n",sizeof(p));
printf("%p\n",p+1);
printf("%p\n",p+2);

printf("%p\n",p-1);
printf("%p\n",p-2);

// Not valid operators on pointers
//printf("%d\n",p*1)
//printf("%d\n",p/1)

//Typecasting

printf("===================\n");

int x = 1025;
int* q = &x;

printf("%p\n",q);
printf("%d\n",*q);

int y = 20;
*q = y;

printf("%d\n",*q);
printf("%p\n",q);

printf("======================\n");

//Pointer typecasting done here
char * z = (char*)q;

//0010 0111 0001 0000 = 10000
//0000 0100 0001 1111 = 1055
//0000 0100 0000 0001 = 1025
*q = 1000000;

printf("%d\n",x);
printf("%d\n",*z);
printf("%p\n",z);

printf("+++++++++++++++++\n");
printf("%u\n",*(z+1));
printf("%u\n",*(z+2));
printf("%u\n",*(z+3));
printf("+++++++++++++++++\n");

printf("%p\n",z+1);

//Void pointer : Generic pointer

void * v = z;
printf("%p\n",v);
printf("%p\n",v+1);

//Error conditions: derefencing/operations on  void ptr not allowed
//printf("%d\n",*v);

//Pointer to pointer

printf("======Pointer 2 pointer=====\n");
int var = 10;
int *ptr1 = &var;
int **ptr2 = &ptr1;
int ***ptr3 = &ptr2;
int ****ptr4 = &ptr3;

printf("%d\n",*ptr1);
printf("%d\n",**ptr2);
printf("%d\n",***ptr3);
printf("%d\n",****ptr4);

****ptr4 = 20;
printf("%d\n",var);
****ptr4 += 1;
printf("%d\n",var);

printf("%p\n",ptr1);
printf("%p\n",ptr2);
printf("%p\n",ptr3);
printf("%p\n",ptr4);

printf("%lu\n",sizeof(ptr1));
printf("%lu\n",sizeof(ptr2));
printf("%lu\n",sizeof(ptr3));
printf("%lu\n",sizeof(ptr4));


}
