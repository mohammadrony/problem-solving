#include<stdio.h>
int main() {
    printf("Enter circle readius: ");
    float radius, circle_area;
    scanf("%f",&radius);
    circle_area = 3.1416 * radius*radius;
    printf("radius is %f and circle area is %f\n", radius,circle_area);
    return 0;
}
