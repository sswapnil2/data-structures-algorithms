#include<stdio.h>

int main()
{
    int i,a = 99,sum=0;
    for(i=1; i<=99; i=i+2)
    {
     sum=sum+i;
     printf("%d",sum);
    }
    return 0;
}