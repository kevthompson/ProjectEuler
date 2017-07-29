#include <iostream>
#include <fstream>
#include <string>

int main() {

	char c;
	bool isaname = false;
	int tempindex = 0;
	int index = 0;
	char temp[11];
	char names[5161][11];


	std::fstream rawtext;
	rawtext.open("names.txt");
	if (!rawtext) {
		std::cout << "Unable to open file" << std::endl;
		
		exit(1); // terminate with error
	}

	while (rawtext >> c) {
		
		if (c == '"') {
			if (isaname) {
				//TODO
				//save temporary char array as a string in names[]
				for (int j = 0; j < tempindex; j++) {
					names[index][j] = temp[j];
				}
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

	printf("names = %s", names[1]);

	//sort names

	//compute points of each name

	//return total points

	system("pause");


	return 0;
}