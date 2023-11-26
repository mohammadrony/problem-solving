#include <stdio.h>
int main()
{
    int a;
    printf("welcome to this program\nenter a number please: ");
    scanf("%d", &a);
    if (a >= 100)
    {
        printf("%d is greater than or equal to 100\n", a);
    }
    else
    {
        printf("No, %d is less than 100\n\n", a);
    }
    return 0;
}