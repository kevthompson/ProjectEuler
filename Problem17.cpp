#include <vector>
#include <iostream>
#include <string>

using namespace std;

int main() {

	string words[1001];

	words[0] = "";
	words[1] = "one";
	words[2] = "two";
	words[3] = "three";
	words[4] = "four";
	words[5] = "five";
	words[6] = "six";
	words[7] = "seven";
	words[8] = "eight";
	words[9] = "nine";
	words[10] = "ten";

	words[11] = "eleven";
	words[12] = "twelve";
	words[13] = "thirteen";
	words[14] = "fourteen";
	words[15] = "fifteen";
	words[16] = "sixteen";
	words[17] = "seventeen";
	words[18] = "eighteen";
	words[19] = "nineteen";
	words[20] = "twenty";
	words[30] = "thirty";
	words[40] = "forty";
	words[50] = "fifty";
	words[60] = "sixty";
	words[70] = "seventy";
	words[80] = "eighty";
	words[90] = "ninety";

	string hundred = "hundred";

	string thousand = "thousand";


	int num = 1;
	for (num; num <= 1000; num++) {
		string temp;

		int thousands = num / 1000;
		int hundreds = (num % 1000) / 100;
		int	tens = (num % 100) / 10;
		int ones = (num % 10);

		if (thousands != 0) {
			temp += words[thousands] + thousand;
		}
		if (hundreds != 0) {
			temp += words[hundreds] + hundred;
		}

		if( num > 100 && num % 100 != 0) temp += "and";

		if (tens != 1) {
			temp += words[tens * 10] + words[ones];
		}
		else {
				temp += words[tens * 10 + ones];
		}

		cout << temp << endl;
		
		words[num] = temp;

	}
	int sum = 0;

	for (int i = 1; i <= 1000; i++) {
		sum += words[i].length();
	}
	printf("The total letters is %d \n", sum);

	system("pause");
	return 0;
}