#include<stdio.h>

int main(){
    int a,b,q;
    printf("Enter dividend ");
    scanf("%d",&a);
    printf("Enter divisor ");
    scanf("%d",&b);
    q = a/b;
    printf("Quotient is %d\n",q);
    printf("Remainder is %d\n",a - (b*q));
}