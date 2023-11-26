#include <stdio.h>
#define ARRAY_SIZE 100
int main()
{
    int i, sum = 0;
    int arr[1111];
    for(i = 0 ; i<=1004 ; i++){
        printf("+ %d ",arr[i]);
        arr[i]=i;
        sum = sum + arr[i];
    }
    printf("= %d\n",sum);
    return 0;
}