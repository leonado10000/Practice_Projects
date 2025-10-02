#include<stdio.h>
#include<stdlib.h>


int main(){
    int i,j,cnt;
    cnt = 0;i = 0;
    for (j = -3; j<=3; j++) {
        if ((i++) && (j >= 0))
            cnt = cnt + j;
        
        printf("%d\n", i);
    }
    cnt = cnt +  i;
    printf("%d", cnt);
    return 0;
}