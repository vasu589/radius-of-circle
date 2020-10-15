#program to display the fibonacci sequence up to n-th term
ntems= int(input("How many terms? "))

#first two terms
n1,n2=0,1
count=0

#check if the number of terms is valid
if terms <= 0:
 print("Please enter the positive integers")
 elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence: ")
   while count < nterms:
   print(n1)
   nth = n1+n2
   #update values 
   n1 = n2
   n2 = nth
   count += 1
