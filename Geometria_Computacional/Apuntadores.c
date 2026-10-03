#include <stdio.h>

int main(){
    int num = 10;
    printf("%d \n", num);

    int *p = &num;
    printf("%d\n", p);
    printf("%d\n", *p);
}