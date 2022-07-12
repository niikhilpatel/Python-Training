a = int(input('Enter the !st Number : '))
b = int(input('Enter the 2st Number : '))
if a < b:
  a,b = b,a
  for i in range(b, (a*b)+1, b ):
    if i%a == 0:
     print('The LCM is : ',i)
     break
