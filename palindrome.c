#include<stdio.h>
#include<conio.h>
void main()
{
int a,r,rev=0,temp;
printf("Enter the number:");
scanf("%d",&a);
temp=a;
while(temp>0)
{
r=temp%10;
rev=rev*10+r;
temp=temp/10;
}
if(rev==a)
printf("%d is the palindromne number",a);
else
printf("%d is not a palindromne number",a);
getch();
}
