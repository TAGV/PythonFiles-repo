#include<stdio.h>

void print_n(char* str)
{
	str[0] = 'h';
	while(*str != '\0')
	{
		printf("%c",*str);
		str++;

	}
	printf("\n");

}

void print_const(const char* str)
{
	//str[0] = 'h';	// error: assignment of read-only location ‘*str’
	while(*str != '\0')
	{
		printf("%c",*str);
		str++;

	}
	printf("\n");


}


int main()
{

//character array
char str[20]="hello";	//String is stored on stack
str[0] = 'A';
printf("%s\n",str);

//Normal print
print_n(str);

//Constant print
print_const(str);

//character pointer
char* st = "hello";	//String is stored as constant in text segment of the memory

//This gives seg fault, since we are trying to modify a constant
//*st = 'A';

printf("%s\n",st);
printf("%c\n",*(st+1));


}
