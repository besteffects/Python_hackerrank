#!/bin/python3
#!/bin/python3
def evenOdd():
 """
 Given an integer,n, perform the following conditional actions:
 If n is odd, print Weird
 If n is even and in the inclusive range of 2 to 5 , print Not Weird
 If n is even and in the inclusive range of 6 to 20, print Weird
 If n is even and greater than 20, print Not Weird
 """
 N = int(input())
 if N%2 !=0:
  print ("Weird")
 elif N%2==0 and N in range (2,6):
  print ("Not Weird")
 elif N%2==0 and N in range (2,21):
  print ("Weird")
 elif N%2==0 and N in range (21,101):
  print ("Not Weird")
evenOdd()
 
# elif ends process after if previous condition is true
