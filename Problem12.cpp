#include <iostream>
#include <cmath>

using namespace std;

bool done = false;
int ans;
int num = 0;
int dx = 1;
int main(){
    while(!done){
    int divisors = 0;
    for(int i = 1; i <= sqrt(num); i++){
        if(num % i == 0){
            divisors++;
        }
        if(divisors >= 250){
            done = true;
            ans = num;
        }
    }
    num += dx;
    dx++;
    }
    cout << "answer: " << ans << endl;
    return 0;
}
