#include <stdio.h>
int main()
{
    int i, n, N;
    int max = 0;
    printf("please enter how many number to input: ");
    scanf("%d", &n);
    printf("please enter some number here: ");
    for (i = 0; i < n; i++)
    {
        scanf("%d", &N);
        if (N > max)
        {
            max = N;
        }
    }
    printf("The hightest value amoung them is %d\n", max);
    return 0;
}