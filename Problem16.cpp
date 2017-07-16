#include <iostream>
#include <cmath>

using namespace std;

long double t;
int sum;

int main(){
    t = pow(2, 900);

    while(t != 0){
    int temp = (int) t % 10;
    sum += temp;
    t /= 10;
    cout << t << endl;
    }
    cout << sum << endl;
    return 0;
}
