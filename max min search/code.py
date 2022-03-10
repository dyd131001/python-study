n = int(input())
arr = [0]*n
arr = list(map(int,input().split()))
small = min(arr)
large = max(arr)
print(small)
print(large)