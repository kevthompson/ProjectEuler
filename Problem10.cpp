#include <iostream>
#include "isPrime.cpp"

using namespace std;

int main(){
    long long int sum = 2;
for(long long int i = 3; i < 2000000; i += 2){
    if(isPrime(i)){
    sum += i;
    cout << sum << endl;
    }
    }

    return 0;
}

