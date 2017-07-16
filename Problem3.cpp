#include <iostream>
#include <cmath>
#include "isPrime.cpp"
using namespace std;

long long int given = 600851475143;
long int num = sqrt(given);
bool done = false;


int main(){
    while(!done && (num > 0)){
        num--;
        if((given % num) == 0){
            if( isPrime(num) ){
                done = true;
                cout << num;
            }
        }
    }
    return 0;
}
