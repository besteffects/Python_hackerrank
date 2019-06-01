"""
Powers or exponents in Python can be calculated using the built-in power
function. Call the power function A in power of b as shown below:
>>>pow(a,b)
or >>> a**b
It's also possible to calculate A in power of b mod m.
>>> pow(a,b,m)
This is very helpful in computations where you have to print the resultant
% mod.
Note: Here, a and b can be floats or negatives, but, if a third argument is
present, cannot be negative.
Note: Python has a math module that has its own pow().
It takes two arguments and returns a float.
Frankly speaking, we will never use math.pow().

Task
You are given three integers:a,b and m, respectively. Print two lines.
The first line should print the result of pow(a,b). The second line should
print the result of pow(a,b,m).
Input Format
The first line contains a, the second line contains b, and the third line
contains m.
Constrains
1<=a<=10
1<=b<=10
2<=m<=1000

Samle input
3
4
5

Sample Output
81
1
"""
def modPower():
 if __name__ == '__main__':
  a, b, m = int(input()),int(input()), int(input()) #a,b,m = [int(input()) for _ in '123']
  print(pow(a,b),pow(a,b,m),sep='\n')
