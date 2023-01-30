def mergeSort(arr, p, r):
    if p < r:
        q = (p+r)//2
        mergeSort(arr, p, q)
        mergeSort(arr, q+1, r)
        merge(arr, p, q, r)
    return arr

def merge(arr, p, q, r):
    i = p
    j = q+1
    t = 1
    temp = [0] * (r-p+1)

    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            temp[t-1] = arr[i]
            i += 1
        else:
            temp[t-1] = arr[j]
            j += 1
        t += 1

    while i <= q:
        temp[t-1] = arr[i]
        i += 1
        t += 1

    while j <= r:
        temp[t-1] = arr[j]
        j += 1
        t += 1

    global numSaves

    for i in range(p, r+1):
        numSaves += 1
        arr[i] = temp[i-p]
        if(numSaves == k):
            print(arr[i])
            exit(0)

n, k = map(int, input().split())
arr = list(map(int, input().split()))
numSaves = 0
arr = mergeSort(arr, 0, n-1)
print(-1)
