#Ques:1
 #Write A program to accept 
#Four digit number from user and 
#count zero , odd and even digits 
#from the entered number...
print("Question1")
countzero = 0
countodd = 0
counteven = 0
n = input("Enter four digit number:")
print (type (n))
l = len(n)
if l != 4:
    print ("This is not four digit number ")    
else:   
    for i in n:
        if int (i) == 0:
            countzero = countzero+1
        elif int(i)%2!=0:
            countodd = countodd+1 
        elif int(i)%2==0:
            counteven = counteven+1
    print ('Number of Zeros',countzero)
    print ('Number of odd',countodd)
    print ('Number of even',counteven)
      
