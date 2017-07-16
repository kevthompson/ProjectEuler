#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

#define TALL 20
#define WIDE 20

double countmoves (double moves[], int width, int height);

void clearArray(double moves[], int width, int height);


int main(){
int height = TALL;
int width = WIDE;
double moves[400];
clearArray(moves, width, height);
cout << moves[0] << endl;
double ans = countmoves(moves, width, height);
/*for(int i = 0; i < 20; i++){
    for(int j = 0; j < 20; j++){
    cout << moves[20*i + j] << "  ";
    }
    cout << endl;
}*/
cout << setprecision(15) << ans << endl;
return 0;
}


double countmoves(double moves[], int width, int height){

//cout << width << " x " << height << endl;
if(width == 0){
    //cout << "test2" << endl;
    return 1;
}
if(height == 0){
    //cout << "test3" << endl;
    return 1;
}
if(moves[TALL*(height-1) + (width-1)] > 0){
    //cout << TALL*(height-1) + (width-1) << endl;
    return moves[TALL*(height-1) + (width-1)];
}

if(moves[TALL*(height-1) + (width-1)] < 0){
    //cout << endl << "error" << endl << endl;
    return moves[TALL*(height-1) + (width-1)];
}
double num1 =  countmoves(moves, width, height - 1);
double num2 =  countmoves(moves, width - 1, height);
moves[TALL*(height-1) + (width-1)] =  num1 + num2;
if(width >= 17){
    //cout << width << " x " << height << "    " << TALL*(height-1) + (width-1) << "    " << moves[TALL*(height-1) + (width-1)] << "    " << moves[TALL*(height-2) + (width-1)] << "    " << moves[TALL*(height-1) + (width-2)] << endl;
}
double k = moves[TALL*(height-1) + (width-1)];
return k;
}


void clearArray(double moves[], int width, int height){
    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            moves[TALL*(i) + (j)] = 0;
        }
    }
    for(int i = 0; i < 20; i++){
        for(int j = 0; j < 20; j++){
       // cout << moves[20*i + j] << "  ";
        }
    cout << endl;
    }
}
