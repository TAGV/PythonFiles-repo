#include<stdio.h>

void inc_call_by_value(int a)
{
	a = a + 1;
	printf("Address of a in cbv = %p\n",&a);
}

void inc_call_by_ref(int *p)
{
	*p += 1;
	printf("Address of p in cbr = %p\n",p);

}

int main()
{

int a = 10;

printf("Value of a = %d\n",a);
printf("Address of a = %p\n",&a);

//Call by value
inc_call_by_value(a);
printf("Value of a after cbv = %d\n",a);

//Call by reference
inc_call_by_ref(&a);
printf("Value of a after cbr = %d\n",a);

}

