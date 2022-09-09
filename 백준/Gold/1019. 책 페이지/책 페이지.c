#include <stdio.h>

void cal(int i, int num[], int cnt)
{
    while(i>0)
    {  
        num[i%10]+=cnt;
        i/=10;
    }
}
int main()
{
    int i,cnt=1,start=1,end;
    int num[10];
    
    for(i=0;i<10;i++)
    {
        num[i] = 0;
    }
    scanf("%d",&end);
    
    while(start<=end)
    {
        while(end%10 !=9 && start<=end)
        {
            cal(end,num,cnt);
            end--;
        }
        if(end<start)
        {
            break;
        }
        
        while(start%10!=0 && start<=end)
        {
            cal(start,num,cnt);
            start++;
        }
        start /= 10;
        end /= 10;
        
        for(i=0;i<10;i++)
        {
            num[i]+=(end-start+1)*cnt;
        }
        cnt *=10;
    }
    
    for(i=0;i<10;i++)
    {
        printf("%d ",num[i]);
    }
    return 0;
}