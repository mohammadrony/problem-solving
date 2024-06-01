#include <stdio.h>
int main()
{
    int n;
    printf("enter a number odd or even: ");
    scanf("%d", &n);
    if (n % 2 == 0)
    {
        goto EVEN;
    }
    else
    {
        goto ODD;
    }

EVEN:
    printf("%d is even\n", n);
    goto END;
ODD:
    printf("%d is odd\n", n);
END:
    return 0;
}