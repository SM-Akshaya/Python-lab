m=int(input("Enter the first number:"))
n=int(input("Enter the second number:"))
def product_or_sum(m,n):
  sum=0
  rem=0
  product=m*n
  if(product > 500):
    print("The product is : ",product)
    print("It is greater than 500 ")
    while(product>0):
      rem = product % 10
      sum=sum+rem
      product=product//10
    print("Sum of their product is: ",sum)
  else:
    print("Product is : ",product)
product_or_sum(m,n)
