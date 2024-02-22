#Ques:2
#Write a program to
#accept ‘n’ numbers from user , 
#store these numbers into an array. 
#Find out maximum and minimum number from an Array.
print ('Question:2')
from array import*
arr = array('i',[])
n = int(input('Enter the length of the array : '))
for i in range (n) :
    num = int (input ('Enter the element for array : '))
    arr.append(num)   
print(arr)
max = arr[0]
for e in arr :
    if e > max :
        max = e
print(max)               





#numbers = []
#for i in range(n):
 #   num = float(input(f"Enter number {i+1}: "))
  #  numbers.append(num)
'''string = "The best of both worlds";  
count = 0;  
   
#Counts each character except space  
for i in range(0, len(string)):  
    if(string[i] != ' '):  
        count = count + 1;'''  
   
#Displays the total number of characters present in the given string  
#print("Total number of characters in a string: " ,count)