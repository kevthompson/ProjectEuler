#include <iostream>
#include <cmath>
double kms;
using namespace std;
int main(){
for(double a = 1; a < 999; a++){
    for(double b = 1; b < 999; b++){
            double c = sqrt(a * a + b * b);
        if(modf(c, &kms) == 0){
            if(a + b + c == 1000){
                cout << a << endl << b << endl << c << endl << a*b*c << endl;
                return 0;
            }
        }

        }
    }
    return 0;
}
