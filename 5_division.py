'''The provided code stub reads two integers, 3 and 5, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  a//b . 
The second line should contain the result of float division, a /b .

No rounding or formatting is necessary.

Example
a=3
b=5

The result of the integer division .
The result of the float division is .
Print:

0
0.6
'''

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)     # Interger Divison
    print(a/b)      # Float Divison