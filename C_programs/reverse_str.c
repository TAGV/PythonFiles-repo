#include<stdio.h>
#include<stdlib.h>

void reverse(char* A)
{
//printf("%d\n",sizeof(A));

int counter = 0;	//Used to determine the size of the array
char* ptr = A;		//Storing the original pointer address
while(*A != '\0')
{
	*A++;
	counter++;
}

printf("Reversing the string.....\n");

for(int i = 1; i<=counter; i++)
{
printf("%c",ptr[counter-i]);
}
printf("\n");


}


int main()
{

char* str = "WelcomeToTheCity of the Future 2021";

printf("%s\n",str);
reverse(str);


}
