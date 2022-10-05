#include <stdio.h>

int main()
{
    int n,temp,count=1;
    scanf("%d",&n);
    temp = n;
    while(count++)
    {
        n=(n%10)*10+(n/10+n%10)%10;
        if(temp==n) break;
    }
    printf("%d",count-1);
}