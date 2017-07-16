#include <iostream>
using namespace std;

int fib = 2;
int fib2 = 1;
int sum = 0;

int main() {
    while(fib < 4000000){
    if (fib % 2 == 0){
        sum += fib;
    }
    int temp = fib;
    fib += fib2;
    fib2 = temp;
    }
    cout << sum;
    return 0;
}
