#include<stdio.h>

int main()
{
	int n,h,i,cmd,k;
	scanf("%d %d",&n,&h);
	
	int a[n];
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
		
	i = 0;k = 0;
	scanf("%d",&cmd);
	while( cmd != 0 )
	{
		switch(cmd)
		{
			case 1:
				if( i != 0 )
					i--;
				break;
			case 2:
				if( i != n-1 )
					i++;
				break;
			case 3:
				if( k == 0 )
				{
					if( a[i] != 0 )
					{
						k = 1;
						--a[i];
					}
				}
				break;
			case 4:
				if( k == 1 )
				{
					if( a[i] != h )
					{
						k = 0;
						++a[i];
					}
				}
				break;
		}
		scanf("%d",&cmd);
	}
	
	for(i=0;i<n;i++)
		printf("%d ",a[i]);
	
	return 0;
}
