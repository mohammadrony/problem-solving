#include <stdio.h>
int main()
{
    int i, sum = 0, N = 10, num;
    printf("Enter %d number: ", N);

    for (i = 1; i <= 10; i++)
    {
        scanf("%d", &num);
        sum = sum + num;
    }

    printf("%d is the result\n", sum);
    return 0;
}