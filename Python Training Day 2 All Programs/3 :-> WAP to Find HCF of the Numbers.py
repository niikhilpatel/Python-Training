a = int(input('Enter the 1st Number : '))
b = int(input('Enter the 2st Number : '))
i = 1
while (i <= a and i <= b):
  if a%i == 0 and b%i == 0:    # a and B are the Input values by th user and i is the 1,2,3,4...... value to the comparison
   hcf = i
  i += 1
print('The HCF is : ',hcf)
