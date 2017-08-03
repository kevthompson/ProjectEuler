#include <iostream>

int main() {
	double num = 0.0f;
	int index = 1;
	double Phi = (1.0f + sqrt(5.0f)) / 2.0f;
	double phi = (1.0f - sqrt(5.0f)) / 2.0f;

	while (num < 400) {
		num = log10((pow(Phi, index) - pow(phi, index))) - log10(sqrt(5.0f));
		index++;
	}
	printf("%d  %f\n", index, num);

	system("pause");

	return 0;
}