def mergeSort(arr, p, r):
    if p < r:
        q = (p+r)//2
        mergeSort(arr, p, q)
        mergeSort(arr, q+1, r)
        merge(arr, p, q, r)
    return arr

def merge(arr, p, q, r):
    L = arr[p:q+1]
    R = arr[q+1:r+1]
    L.append(1000000001)
    R.append(1000000001)
    i = j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr = mergeSort(arr, 0, n-1)
print(arr[k-1])
