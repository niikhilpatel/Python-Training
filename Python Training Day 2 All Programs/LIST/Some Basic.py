a = []
print(a)
print(type(a))

#first Run this Above command

a.append(1)
print(a)


a.append(2)
print(a)  

#Like this you can run more commands


# a.append(1,2,4)      #not Correct
# a.append([1,2,4})    #correct

#append is using to add value with the previous value and add in the last of the list
#Note : You can pass only one number in the append (1.2.4) like this it is not correct, but you can write ike this ([1,2,4})

# EXTEND METHOD

a = [1, 0 , 5 , -1]
a.extend([-2,6,7])
print(a)


# LIST SLICING


# List is Mutable Data Types

a = [1, 0 , 5 , -1, -2, 6, 7]   # List start from the zero index
print(a[0])      # PRINT THE value of index 0 which is 1 
print(a[3])      # PRINT THE value of index 3 which is -1
print(a[0:5])    # PRINT THE value of index 0 to 5 which is 1, 0 , 5 , -1, -2
print(a[-1:])    # PRINT THE value from the last of the list
print(a[-2:-1])
print(a[ :-1])   # print from the last of the list to the first of the list


# LIst Insert


a.insert(0,10)  # here meaning is 0 is index number and 10 is the number which is have to inset in the list
print(a)
