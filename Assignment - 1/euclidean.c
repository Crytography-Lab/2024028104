#include<stdio.h>

int main(){
    int a,b,temp;
    printf("Enter your numbers");
    scanf("%d",&a);
    scanf("%d",&b);
    while(b!=0){
        temp = a%b;
        a = b;
        b = temp;
    }
    printf("GCD of given numbers is %d",a);
}