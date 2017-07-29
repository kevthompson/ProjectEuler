#include <iostream>
#include <fstream>
#include <string>

//Stolen and Modified Code
void insertion_sort(char arr[][11]) {
	int j, temp;

	for (int i = 0; i < 5162; i++) {
		j = i;

		while (j > 0 && arr[j] < arr[j - 1]) {
			temp = arr[j];
			arr[j] = arr[j - 1];
			arr[j - 1] = temp;
			j--;
		}
	}
}

int main() {

	char c;
	bool isaname = false;
	int tempindex = 0;
	int index = 0;
	char temp[11];
	char names[5162][11];


	std::fstream rawtext;
	rawtext.open("names.txt");
	if (!rawtext) {
		std::cout << "Unable to open file" << std::endl;
		
		exit(1); // terminate with error
	}

	while (rawtext >> c) {

		if (c == '"') {
			if (isaname) {
				//save temporary char array as a string in names[]
				for (int j = 0; j < tempindex; j++) {
					names[index][j] = temp[j];

				}
				std::cout << std::endl;
				tempindex = 0;
				index++;
			}
			isaname = !isaname;
		}
		else if (isaname) {
			temp[tempindex] = c;

			tempindex++;
		}
	}
	rawtext.close();


	int points[5162];
	//TODO
	//sort names
	insertion_sort(names);

	//compute points of each name
	for (int j = 0; j < 5162; j++) {
		int sum = 0;
		for (int k = 0; k < 11; k++) {
			sum += names[j][k];
		}
		points[j] = sum * (j + 1);
	}


	//return total points
	int totalpoints = 0;
	for (int j = 0; j < 5162; j++) {
		totalpoints += points[j];
	}
	printf("\nThe total is %d\n", totalpoints);
	system("pause");


	return 0;
}