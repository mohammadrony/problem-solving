#include<stdio.h>
int main() {
    int a;
    printf("Enter a number: ");
    scanf("%d",&a);
    int rem = a % 2;
    if(rem == 0) {
        printf("given number %d is even and reminder is %d\n",a, rem);
    }
    else {
        printf("input number %d is not even and reminder is %d\n",a, rem);
    }
    return 0;
}