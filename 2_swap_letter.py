'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 
'''

def swap_case(s):
    new_string = ""
    for i in s:
        if i.isupper():
            new_string += i.lower()
        else:
            new_string += i.upper()
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
 