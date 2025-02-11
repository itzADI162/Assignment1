a=int(input("Enter first element:" ))
b=int(input("Enter second element:" ))
c=int(input("Enter third element:" ))
total =0
if(a+b+c>50):
 total=a+b+c-0.1*(a+b+c)

print(f"your final price is: {total}")

