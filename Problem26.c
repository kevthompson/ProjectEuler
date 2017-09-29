#include <stdio.h>

int main()
{
	int answer;
	int max = 0;
	int len = 6;
	int num = 1;
	int den = 999;
	int done = 0;
	while(!done)
	{
		if(((den%5) != 0) && ((den%2) != 0))
		{
			num = 1;
			len = 0;
			printf("%d/%d   ", num, den);
			while((num % den) != 1)
			{
				num *= 10;
				len += 1;

				//printf("%d\n", num);
			}
			if(max < len)
			{
				max = len;
				answer = den;			
			}		
			if(len > den)
			{
				done = 1;			
			}
		}
		den--;
	}
	printf("%d", answer);
	return 0;
}
