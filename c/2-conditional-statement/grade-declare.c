#include <stdio.h>
int main()
{
    int marks;
    printf("Enter marks: ");
    scanf("%d", &marks);
    if (marks < 0)
    {
        printf("teacher had a really bad impression on you!!!\n");
    }
    else if (marks < 33)
    {
        printf("you failed in the exam!!!\n");
    }
    else if (marks < 40)
    {
        printf("your grade is D\n");
    }
    else if (marks < 50)
    {
        printf("your grade is C\n");
    }
    else if (marks < 60)
    {
        printf("your grade is B\n");
    }
    else if (marks < 70)
    {
        printf("your grade is A-\n");
    }
    else if (marks < 80)
    {
        printf("your grade is A\n");
    }
    else if (marks <= 100)
    {
        printf("your grade is A+\n");
    }
    else
    {
        printf("check your marks again!!!\n");
    }
    return 0;
}