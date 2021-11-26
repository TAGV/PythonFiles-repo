#include<stdio.h>
#include<stdlib.h>

void print(char* A)
{

while(*A != '\0')
{
printf("%c",*A);
*A++;
}
printf("\n");
}

int compare(char* A,char* B)
{

int flag = 0;
while(*A != '\0' || *B != '\0')
{
	if(*A != *B)
	{
		flag = 1;
		break;
	}
*A++;
*B++;
}

if (flag == 0)
{
printf("Strings are equal\n");
}
else
{
printf("Strings are not equal\n");
}

return flag;

}

int asort(const void* A,const void* B)
{

char x = *((char*)(A));
char y = *((char*)(B));
return x-y;
}

int dsort(const void* A,const void* B)
{

char x = *((char*)(A));
char y = *((char*)(B));
return y-x;

}


int main()
{

//Creates memory on heap
//char* str1=(char*)malloc(10*sizeof(char));
//char* str2=(char*)malloc(10*sizeof(char));

//Creates memory on stack
char* str1;
char* str2;

str1="Hello";
str2="Hell";

print(str1);
print(str2);

int result = compare(str1,str2);
printf("%d\n",result);

//Sorting the string
char str[] = {'A','a','B','b'};
print(str);

// Sorting in ascending order
qsort(str,4,sizeof(char),asort);
print(str);

// Sorting in descending order
qsort(str,4,sizeof(char),dsort);
print(str);


char big_str[] = "HelloBye Welcome 2021";
print(big_str);

qsort(big_str,(sizeof(big_str)-1),sizeof(char),asort);
print(big_str);

qsort(big_str,(sizeof(big_str)-1),sizeof(char),dsort);
print(big_str);

}
