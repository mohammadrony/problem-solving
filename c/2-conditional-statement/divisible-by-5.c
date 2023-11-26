#include<stdio.h>
int main() {
    int a;
    printf("Please enter a number to check the number is divisible by 5 or not: ");
    scanf("%d",&a);
    int reminder = a%5;
    if(reminder == 0) {
        printf("%d is divisible by 5 and reminder is 0\n", a);
    }
    else {
        printf("%d is not divisible by 5 and the reminder is %d\n",a, reminder);
    }
    return 0;
}