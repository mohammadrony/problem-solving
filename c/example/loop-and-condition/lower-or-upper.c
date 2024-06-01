#include <stdio.h>
int main()
{
    int i, N = 5;
    char character;
    for (i = 1; i <= N; i++)
    {
        printf("Enter a new character: ");
        scanf("%c", &character);
        if (character >= 'a' && character <= 'z')
        {
            printf("%c is lower character", character);
        }
        else if (character >= 'A' && character <= 'Z')
        {
            printf("%c is upper character", character);
        }
        else
        {
            printf("%c is not upper not lower character");
        }
    }
    return 0;
}
