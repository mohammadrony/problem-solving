#include<stdio.h>
int main(){
    float b,h;
    printf("Enter base and height of triangle: ");
    scanf("%f %f",&b,&h);
    float triangle_area;
    triangle_area = 0.5*b*h;
    printf("Area of given triangle: %f\n",triangle_area);
    return 0;
}