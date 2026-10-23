n = int(input("Enter value of n "));
a = int(input("Enter value of a "));
power = 2**(n-1)
cal = power%n
if(cal==1):
    print("It is a prime");

else:
    print("It is not a prime");