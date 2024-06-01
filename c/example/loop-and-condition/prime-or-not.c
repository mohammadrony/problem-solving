#include <stdio.h>
int main()
{
    int N, i, isPrime = 1; // 0 means not prime 1 means prime
    printf("Please enter a number: ");
    scanf("%d", &N);
    if (N < 2)
    {
        printf("Number must be greater than or equal to 2 to check prime value.\n");
    }
    else if (N == 2)
    {
        printf("2 is Prime\n\n");
    }
    else
    {
        for (i = 2; i < N; i++)
        {
            if (N % i == 0)
            {
                isPrime = 0;
                break;
            }
        }
        if (isPrime == 0)
        {
            printf("%d is not Prime\n", N);
        }
        else
        {
            printf("%d is Prime\n", N);
        }
    }
    return 0;
}