"""
Task
Read an integer N. For all non-negative integers i<N, print I**.
See the sample for details.

Input Format
The first and only line contains the integer, N.

Constrains
1<=N<=20

Output Format
Print N lines, one corresponding to each i.
Example:
>>> 5
Output:
0
1
4
9
16
"""
def printExponentiation():
 if __name__ == '__main__':
  n = int(input())
  if 1<=n<=20:
   for i in range(0, n):     
    print (i**2)
