#include <iostream>
#include "isPrime.cpp"

using namespace std;

long int n = 2;
long int largest;
int i = 1;

int main(){
    while(i <= 10001){
        if(isPrime(n)){
            i++;
            largest = n;
        }
        n++;
    }
    cout << largest;
    return 0;
}
