#include <stdio.h>
int main()
{
    char ch, upper_ch;
    printf("Enter a lower case character: ");
    scanf("%c", &ch);
    upper_ch = ch - 'a' + 'A';
    printf("lower case of \"%c\" is \"%c\" \n", ch, upper_ch);
    return 0;
}
