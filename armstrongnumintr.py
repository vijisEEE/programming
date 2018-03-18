a=int(input("Enter upper limit: "))
b=int(input("Enter lower limit: "))
for num in range(a,b+1):
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum=sum+digit ** order
       temp=temp//10
   if num == sum:
       print(num)
