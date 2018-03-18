a=int(input("Enter the limit:"))
b=int(input("Enter the number:"))
print("The multiples of the number:")
for i in range(1,a+1):
  if(i%b==0):
    print(i)
