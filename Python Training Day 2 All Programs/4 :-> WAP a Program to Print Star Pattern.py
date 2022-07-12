for i in range(0,4):
  print(1, end = ' ')       # if you put i in the place of 1 it will print numbers in the acsending order like 1 2 3 4 upto range
  
  
for i in range(0,4):
for i in range(0,4):
  print(1, end = ' ')
print()
  
  
a = int(input('Enter a Number : '))
for x in range(a):           # this show only row
 for i in range(a):
   print(1, end = ' ')
 print()


 THIS IS THE MAIN PROGRAM
  
 a = int(input('Enter a Number : '))
for x in range(a):            # this show only row
 for i in range(a-x):
   print('*', end = ' ')
 print()
