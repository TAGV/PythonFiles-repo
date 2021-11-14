#include<stdio.h>
#include<string.h>

void len(char* C) // ~= char* c
{
	int length_of_string = 0;
	while(*C != '\0')
	{
		//This will calculate the size of every single charcater
		int temp = sizeof(*C);
		length_of_string += temp;
		C++;
	}
	printf("Length(Not incl Null character)= %d\n",length_of_string);

}

void print(char* C)
{
	int i=0;
	//Charcter buffer to store the final string
	char ch[20]={'\0'};	//Need to initilaize it to null so as to prevent garbage value

	while (*C != '\0')
	{
		//printf("%c",*C);
		ch[i] = *C;
		C++;	//Pointer can be incremented as compared to an array
		i++;
	}
	printf("%s\n",ch);

//	char* ptr;
//	ptr = ch;
//	printf("%p\n",(ptr));
//	printf("In func  %ld\n",sizeof(ptr));
//return ptr;

}

int main()
{

char c[50]="Helloooooooooo";		//Null terminated character is applied implicitly
char str[]={'b','y','e','\0'};	//Need to explicitly apply the null charcter else it prints garbage
char astr[20]= "Rogerfhffyfy";

//printf("%s\n",c);
//printf("Size= %lu bytes\n",sizeof(c));	//This gives total size of string including the null char
//size(astr);

//int len = strlen(c);
//printf("Length= %d charachters\n",len);	//This gives total length excluding the null char

//int lenstr = strlen(str);
//printf("%s\n",str);
//printf("Size= %lu bytes\n",sizeof(str));
//printf("Length= %d charachters\n",lenstr);

len(c);
len(str);
len(astr);



//char* buff;
//buff = print(c);
//printf("%p\n",buff);
//printf("%ld bytes\n",sizeof(buff));
//printf("%ld characters\n",strlen(buff));

print(c);
print(str);
print(astr);



}
