#include <stdio.h>
int main()
{
    int i = 0, N = 3, num, maximum = 0;

INPUT:
    printf("Enter a number: ");
    scanf("%d", &num);
    if (num > maximum)
        maximum = num;
    i++;

    if (i < N)
        goto INPUT;
    printf("Maximum number is %d\n", maximum);
    return 0;
}