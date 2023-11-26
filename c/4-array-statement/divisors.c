#include <stdio.h>
int main()
{
    int n, i, j;
    printf("Enter a number: ");
    scanf("%d", &n);
    int divisors[n];
    for (i = 1, j = 0; i <= n; i = i + 1)
    {
        if (n % i == 0)
        {
            divisors[j] = i;
            j++;
        }
    }
    printf("Divisors\n\n");
    for (i = 0; i < j; i++)
    {
        printf("%d, ", divisors[i]);
    }
    printf("\n\n");
    return 0;
}
