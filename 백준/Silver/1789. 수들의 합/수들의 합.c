#include <stdio.h>

int main()
{
	long long input,sum=0, i=0;
	scanf("%lld",&input);
	do
	{
		sum+=i;
		if(sum>input)
		{
			i--;
			break;
		}
	}while(++i);
	printf("%d",i);
}