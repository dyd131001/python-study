from decimal import ROUND_DOWN


n = int(input())
arr = list(map(int, input().split()))
cnt = 0


def BinarySearch(start, finish):
    global cnt
    if(start > finish):
        return -1
    else:
        mid = int((start + finish) / 2)
        if(mid == arr[mid]):
            cnt += 1
            return mid
        elif(mid < arr[mid]):
            cnt += 1
            return BinarySearch(start, mid-1)
        else:
            cnt += 1
            return BinarySearch(mid+1, finish)


index = BinarySearch(0, n)
print(index)
print(cnt)
