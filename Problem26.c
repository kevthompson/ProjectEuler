#include <stdio.h>

int main()
{
	
	int answer = 999;
	int max = 0;
	int len = 6;
	unsigned long long num = 10;
	int den = 3;
	int done = 0;
	//int rem = 0;
	
	while(!done)
	{
                printf(" %llu / %d   ", num, den);
		if((den%5) != 0)
		{
			num = 1000;
			len = 3;
			//printf(" %llu / %d   ", num, 
			//printf("%d  ", rem);

			while(num != 1)
			{
				num *= 10;
				num = num % den;
				len += 1;
				//printf(" %llu %d \n", num, den);
			}
			if(max < len)
			{
				printf("%d %d \n", answer, max);
				max = len;
				answer = den;			
			}		
			if(den == 999)
			{
				done = 1;			
			}
		}
		//done = 1;
		den+=2;

	}
	printf("%d %d/n", answer, max);
	return 0;
}
