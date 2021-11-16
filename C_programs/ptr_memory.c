#include<stdio.h>

int main()
{

int* ptr;
long int* ptr_lng;
char* ptr_1;
float* ptr_2;
double* ptr_3;
long double* ptr_4;


printf("Memory of int pointer = %ld bytes\n",sizeof(*ptr));
printf("Memory of long int pointer = %ld bytes\n",sizeof(*ptr_lng));
printf("Memory of char pointer = %ld bytes\n",sizeof(*ptr_1));
printf("Memory of float pointer = %ld bytes\n",sizeof(*ptr_2));
printf("Memory of double pointer = %ld bytes\n",sizeof(*ptr_3));
printf("Memory of long double pointer = %ld bytes\n",sizeof(*ptr_4));

printf("============================\n");


int a = 10;

ptr = &a;
ptr_lng =(long int*)ptr;
ptr_1 =(char*)ptr;
ptr_2 =(float*)ptr;
ptr_3 =(double*)ptr;
ptr_4 =(long double*)ptr;

printf("Address of pointer= %p\n",ptr);

printf("\n======== Incrementing ptr address by 1 ====================\n");

//Incrementing ptr address increments var by size of datatype
ptr = ptr + 1;
ptr_lng += 1;
ptr_1 += 1;
ptr_2 += 1;
ptr_3 += 1;
ptr_4 += 1;

printf("Integer (%ld bytes) 	 : %p\n",sizeof(*ptr),ptr);
printf("Long Integer (%ld bytes) : %p\n",sizeof(*ptr_lng),ptr_lng);
printf("Char (%ld bytes)       	 : %p\n",sizeof(*ptr_1),ptr_1);
printf("Float (%ld bytes) 	 : %p\n",sizeof(*ptr_2),ptr_2);
printf("Double (%ld bytes) 	 : %p\n",sizeof(*ptr_3),ptr_3);
printf("Long Double (%ld bytes)  : %p\n",sizeof(*ptr_4),ptr_4);

}
