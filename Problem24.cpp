#include <iostream>

int factorial(int num) {
	if (num <= 1) return 1;
	else {
		int temp = num;
		temp *= factorial(num - 1);
		return temp;
	}
}

void findPermutation(int digits, int target, int arr[10]) {
	int numbers[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	
	if (digits <= 1 || target < 0) return;

	int quot = (target) / factorial(digits-1);
	int rem =  (target) % factorial(digits-1);
	printf("%d   %d \n", quot, digits);

	//modify array according to the quotient
	int temp = arr[digits - quot-1];
	for (int i = digits - quot-1; i < digits-1; i++) {
		arr[i] = arr[i+1];
	}
	arr[digits - 1] = temp;

	for (int i = 0; i < 3; i++) {
		printf("%d", arr[i]);
	}
	printf("\n\n");

	return(findPermutation(digits - 1, rem, arr));

}

int main() {
	int numbers[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	int target = 1;
	int digit = 3;

		findPermutation(digit, target, numbers);
		printf("\n");
	
		for (int i = 0; i < digit; i++) {
			printf("%d", numbers[i]);
	}
		printf("\n");

	system("pause");
	return 0;
}