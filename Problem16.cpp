#include <stdlib.h>
#include <iostream>

using namespace std;


void longdouble(int num[], int length) {
	int carry = 0;
	int i;
	for (i = 0; i < length; i++) {
		
		int temp = num[i] * 2 + carry;
		
		carry = temp / 10;
		
		num[i] = temp % 10;
		cout << num[i] << endl;
	}
}

int getSumofDigits(int num[], int length) {
	int sum = 0;
	for (int i = 0; i < length; i++) {
		cout << num[i] << endl;
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

	for (int i = 0; i < 1000; i++) {
		longdouble(num, length);
	}

	int solution = getSumofDigits(num, length);
	
	printf("solution is %d \n", solution);

	system("pause");

	return 0;
}
