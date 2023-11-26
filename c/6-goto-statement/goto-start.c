#include <stdio.h>
int main()
{
    goto LABEL2;
    printf("First Line.\n");

LABEL1:
    printf("LABEL 1!\n");
    goto END;

LABEL2:
    printf("LABEL 2!\n");
    goto LABEL1;

END:
    return 0;
}