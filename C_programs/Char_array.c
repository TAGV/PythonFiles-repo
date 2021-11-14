#include<stdio.h>
#include<string.h>


void onlyprint(char* buff)
{

for(int j = 0; j<strlen(buff);j++)
{
	printf("%c",buff[j]);

}
printf("\t");


}


void len(char C[]) // ~= char* c
{
	printf("Length of string(Not incl Null character)\t");
	onlyprint(C);
	int length_of_string = 0;
	while(*C != '\0')
	{
		//This will calculate the size of every single charcater
		int temp = sizeof(*C);
		length_of_string += temp;
		C++;
	}
	printf("%d\n",length_of_string);

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
	printf("%s\n",ch); //If this is enabled,then function need not return anything

	//char* ptr;
	//ptr = ch;
	//printf("%c\n",ptr[13]);
	//printf("%ld\n",strlen(ptr));

//return ptr;

}



int main()
{

char c[50]="Helloooooooootghfghfb";		//Null terminated character is applied implicitly
char str[]={'b','y','e','e','e','e','\0'};			//Need to explicitly apply the null charcter else it prints garbage
char astr[20]= "Rogerfhffyfy";

//printf("Size= %lu bytes\n",sizeof(c));	//This gives total size of string including the null char

//int len = strlen(c);
//printf("Length= %d charachters\n",len);	//This gives total length excluding the null char

len(c);
len(str);
len(astr);



//char* buff = print(astr);
//onlyprint(buff);

printf("\n");
print(c);
print(str);
print(astr);




}
