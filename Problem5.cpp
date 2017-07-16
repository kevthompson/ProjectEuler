#include <iostream>
using namespace std;

int n = 1;
bool done = false;

int main(){
    while(!done){
    for(int i = 1; i <= 20; i++){
        if(n % i != 0){
            n++;
            i = 21;
        }
        if (i == 20) done = true;
    }
    }
    cout << n;
    return 0;
}
