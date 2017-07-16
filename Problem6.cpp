#include <iostream>

using namespace std;

int main(){
    int sop = 1;
    int pos = 1;
    for(int i = 2; i <= 100; i++){
        sop += i * i;
        pos += i;
    }
    pos *= pos;
    cout << pos - sop;
}
