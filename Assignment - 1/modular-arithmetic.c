#include<stdio.h>

int main(){
    int a,b,n;
    printf("Enter two numbers");
    scanf("%d",&a);
    scanf("%d",&b);
    printf("\n Enter your modulus number \n");
    scanf("%d",&n);
    printf("Addition is %d\n",(a+b)%n);
    printf("Subtraction is %d\n",(a-b)%n);
    printf("Multiplication is %d\n",(a*b)%n);
}