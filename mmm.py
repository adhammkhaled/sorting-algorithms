def hyperid_sort ( arr , threshold):

    if len(arr) <= threshold :
        return  insertion_sort(arr)
    else :
       return mergeSort(arr)




def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def mergeSort(arr):
    _mergeSort(arr,0,len(arr)-1)
    return arr
def _mergeSort(arr,l,h):
    if(l<h):
        m=(l+h)//2
        _mergeSort(arr,l,m)
        _mergeSort(arr,m+1,h)

        merge(arr,l,h)

def merge(arr,l,h):
    newarr= []
    m=(l+h)//2
    i = l
    j = m+1
    k=l
    while(i<=m and j<=h):
        if(arr[i]<=arr[j]):
            newarr.append(arr[i])
            i+=1
        else:
            newarr.append(arr[j])
            j+=1
        k+=1
    while(i<=m):
        newarr.append(arr[i])
        i+=1
        k+=1
    while(j<=h):
        newarr.append(arr[j])
        j+=1
        k+=1
    for i in range(len(newarr)):
        arr[l + i] = newarr[i]

    return  arr

arr = [5, 2, 8, 3, 9, 1]
threshold = 5
sorted_arr = hyperid_sort(arr, threshold)
print("Sorted array:", sorted_arr)

#########find_the_3rd_number
def partition(arr, low, high):
    pivot = arr[high]  # Choosing the pivot element from the array
    leftPointer = low
    rightPointer = high - 1
    while leftPointer <= rightPointer:
        while leftPointer <= rightPointer and arr[leftPointer] < pivot:
            leftPointer += 1
        while rightPointer >= leftPointer and arr[rightPointer] > pivot:
            rightPointer -= 1
        if leftPointer <= rightPointer:
            arr[leftPointer], arr[rightPointer] = arr[rightPointer], arr[leftPointer]
            leftPointer += 1
            rightPointer -= 1

    arr[leftPointer], arr[high] = arr[high], arr[leftPointer]
    return leftPointer

def find_kth_largest(arr, k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        pivot_index = partition(arr, low, high)
        if pivot_index == len(arr) - k:
            return arr[pivot_index]
        elif pivot_index < len(arr) - k:
            low = pivot_index + 1
        else:
            high = pivot_index - 1
    return None

arr = [3, 55, 16, 25, 63, 52, 40]
k = 3
print("Kth largest element is:", find_kth_largest(arr, k))
