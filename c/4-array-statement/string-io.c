#include<stdio.h>
int main() {
    char str1[] = "hello world";
    scanf("%s", str1);
    int i =0 ;
    for(i=0; str1[i] != '\0'; i++){
        printf("%d", i);
    }
    return 0;
}