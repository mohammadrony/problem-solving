#include<stdio.h>
int main()
{   
    int arr_size=0;
    printf("Declare the size of array: ");
    scanf("%d",&arr_size);
    getchar();
    int arr[arr_size];

    char take_input;
    printf("Take input for this array (y/n): ");
    scanf("%c",&take_input);
    getchar();
    if(take_input == 'y' || take_input == 'Y')
    {
        int i=0;
        while(i<arr_size)
        {
            printf("taking input for arr[%d]: ",i);
            scanf("%d",&arr[i]);
            i++;
        }
    }

    printf("------------------------------------------\n");
    printf("The array value with the array index\n");
    printf("------------------------------------------\n");
    int i=0;
    for(i=0;i<arr_size;i++)
    {
        printf("arr[%d] ------- %d\n",i,arr[i]);
    }
    printf("------------------------------------------\n");
    return 0;
}