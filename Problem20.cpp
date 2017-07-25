#include <stdlib.h>
#include <iostream>

using namespace std;


void longmultiply(int num[], int multiplier, int length) {
	int carry = 0;
	int i;
	for (i = 0; i < length; i++) {

		int temp = num[i] * multiplier + carry;

		carry = temp / 10;

		num[i] = temp % 10;
		cout << num[i] << endl;
	}
}

int getSumofDigits(int num[], int length) {
	int sum = 0;
	for (int i = 0; i < length; i++) {
		sum += num[i];
	}
	return sum;
}

int main() {
	const int length = 350;
	int num[length];
	num[0] = 1;
	for (int i = 1; i < length; i++) {
		num[i] = 0;
	}

	for (int i = 1; i <= 100; i++) {
		longmultiply(num, i, length);
	}

	int solution = getSumofDigits(num, length);

	printf("solution is %d \n", solution);

	system("pause");

	return 0;
}
