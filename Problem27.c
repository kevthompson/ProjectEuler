#include <stdio.h>
int main(){
  int a, b, maxn = 0;
  for(a=-1001;a<1001;a++){
    for(b=-1001;b<1001;b++){
      n = 0;
      done = false;
      while(!done){
        n++;
        if(!isPrime(n*n+a*n+b)) done = true;
      }
      if(n>maxn){
        n = maxn;
        ans = a*b;
      }
    }
  }
  printf("Answer: %d", ans);
  return 0;
}
