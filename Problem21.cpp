#include <iostream>

using namespace std;

int divisors(int num) {
	int sum = 1;
	//printf("%d   ", num);
	for (int i = 2; i <= sqrt(num); i++) {
		
		if (num % i == 0) {
			if (num / i == i) {
				sum += i;

				//printf("   %d", i);
			}
			else {
				sum += i + num / i;
				//printf("   %d   %d", i, num / i);
			}
		}
		
	}

	//printf("   %d   \n", sum);
	return sum;
}

int main() {
	int divsums[10000];
	for (int i = 0; i < 10000; i++) {
		divsums[i] = divisors(i + 1);
	}
	
	int sum = 0;

	for (int i = 0; i < 10000; i++) {
		for (int j = i+1; j < 10000; j++) {
			if (divsums[i] != 1) {
				if (divsums[i] == j+1 && divsums[j] == i+1) {
					sum += i + j + 2;

					printf("d(%d) = %d     d(%d) = %d \n", i + 1, divsums[i], j + 1, divsums[j]);
				}
			}
		}
	}
	printf("%d", sum);

	system("pause");
	return 0;
}