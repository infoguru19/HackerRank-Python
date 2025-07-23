'''
Four integers x,y,z and n, each on a separate line.
Constraints
Print the list in lexicographic increasing order.
Sample Input 0
1
1
1
2
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
'''


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    out = [[i,j,k] for i in range(0, x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(out)