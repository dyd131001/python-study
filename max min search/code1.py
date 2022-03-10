n, k, m = map(int, input().split())
s1 = [[0] * k for _ in range(n)]
s2 = [[0] * m for _ in range(k)]
s3 = [[0] * n for _ in range(k)]
for i in range(n):
    s1[i] = list(map(int, input().split()))
for i in range(k):
    s2[i] = list(map(int, input().split()))


def matrix(n, m, k):
    for i in range(n):
        for j in range(n):
            for z in range(n):
                s3[i][z] += s1[i][j] * s2[j][z]


matrix(n, m, k)
for i in range(len(s3)):
    for j in range(len(s3[i])):
        if j == len(s3[i])-1:
            print(s3[i][j])
        else:
            print(s3[i][j], end=' ')
