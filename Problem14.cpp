#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

double collatz(double start, int step);

int main(){
double maxlength = 1;
double ans = 1;
for(double num = 13; num <= 1000000; num++){
    double temp = collatz(num, 1);
    //cout << temp << endl;
    if(maxlength < temp){
        ans = num;
        maxlength = temp;
        cout << ans << endl;
    }
}
cout << setprecision(10) << ans << endl;
return 0;
}

double collatz(double start, int step){
if(start == 1) return step;
//cout << start << endl;
if( fmod(start, 2) == 1) start = (start * 3) + 1;

else if(fmod(start, 2) == 0) start /= 2;
double ans = collatz(start, step+1);
return ans;
}
