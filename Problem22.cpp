#include <iostream>
#include <fstream>
#include <string>

int main() {

	char c;
	bool isaname = false;
	int index = 0;
	std::string names[6000];


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
				
				index++;
			}
			isaname == !isaname;
		}
		else if (isaname) {
			//TODO
			//add the character to a temporary array
		}
	}
	rawtext.close();

	//sort names

	//compute points of each name

	//return total points


	return 0;
}