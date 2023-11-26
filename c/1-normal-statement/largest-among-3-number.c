#include <stdio.h>
int main()
{
    int a, b, c;
    printf("enter the value of a b c: ");
    scanf("%d%d%d", &a, &b, &c);
    if (a > b)
    {
        if (a > c)
        {
            printf("largest value: %d\n", a);
        }
        else
        {
            printf("largest value: %d\n", c);
        }
    }
    else
    {
        if (b > c)
        {
            printf("largest value: %d\n", b);
        }
        else
        {
            printf("largest value: %d\n", c);
        }
    }
    return 0;
}