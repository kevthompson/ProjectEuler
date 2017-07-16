//Solved

#include <iostream>

using namespace std;

int year = 1900;
int date = 1;
int day = 1;
int month = 0;
int FebDays = 28;
int SundayCounter;

int months[] = {31,FebDays,31,30,31,30,31,31,30,31,30,31};

int main(){
while(year < 2001){
    if(date==1 && month==1 && year==1901)
        SundayCounter = 0;
    if(day == 0 && date == 1){
        SundayCounter++;
        cout << SundayCounter << endl;
    }
    date++;
    day = (day + 1) % 7;
    //cout << day << "  " << date << "  " << month << "  "  << year << endl;
    if(date == months[month]){
        date = 0;
        month++;
        if(month == 12){
            month = 0;
            year++;
            cout << year << endl;
            if(year%4 == 0 && (year%100 != 0 || year%400 == 0)){
                FebDays = 29;
            }
            else{
                FebDays = 28;
            }
        }
    }
}
cout << SundayCounter << endl;
return 0;
}
