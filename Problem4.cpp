#include <iostream>

#include <stdlib.h>
#include <cmath>

using namespace std;
int nummax = 999;
int num1 = nummax;
int num2 = nummax;
int nummin = 900;
int largest = 0;

char num[6];
bool isPalendrome(char num[]){
    int i = 0;
    while(i < sizeof(num)/sizeof(num[0])){
        char a = num[i];
        char b = num[ sizeof(num)/sizeof(num[0]) - i+1];
       // cout << a << "<-a  b->" << b << endl;
        if (a != b ) return false;
        i++;
    }
    return true;
}

int main(){
for(num1; num1 > 900; num1--){
    for(num2; num2 > nummin; num2--){
      //  cout << num1 << "<-num1 num2->" << num2 << endl;
        int num3 = num1 * num2;
       // cout << num3 << endl;
        if(num3 > largest){
                int temp = num3;

                itoa(temp, num, 10);

            if( isPalendrome(num) ){
                largest = num3;
            }
            cout << num << "   " << largest << endl;

        }
    num2 = nummax;
    nummax --;
    }
    nummax = num1 - 1;
    num2 = nummax;

   // cout << num1 << "      " << num2 << endl;

}
    cout << "largest = " << largest;
    return 0;

}
