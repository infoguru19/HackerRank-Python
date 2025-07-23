'''
Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))
    arr.sort()
    print(arr[-2])