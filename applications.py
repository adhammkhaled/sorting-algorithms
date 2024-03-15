import sorting


def hybrid_sort(arr , threshold):
    _hybrid_sort(arr,0,len(arr)-1 ,threshold)
    return arr
def _hybrid_sort(arr, l , h , threshold):
    if h-l <= threshold :

        insertion_sort_hybrid(arr,l,h)


    else:
           if (l < h):
                m = (l + h) // 2
                _hybrid_sort(arr, l, m,threshold)
                _hybrid_sort(arr, m + 1, h,threshold)

                sorting.merge(arr,l,h)


def insertion_sort_hybrid(arr, l, h):
    for i in range(l + 1, h + 1):
        key = arr[i]
        j = i - 1
        while j >= l and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = sorting.generate_arr(1000)
threshold = 5

sorted_arr = hybrid_sort(arr, threshold)
print("Sorted array:", sorted_arr)



#################

import random

def partition(arr, low, high):
    pivot = arr[high]
    leftPointer = low
    rightPointer = high - 1
    while leftPointer <= rightPointer:
        while leftPointer <= rightPointer and arr[leftPointer] < pivot:
            leftPointer += 1
        while leftPointer <= rightPointer and arr[rightPointer] > pivot:
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

arr = [random.randint(0, 3000) for _ in range(300)]
print(arr)
k = 3
print("Output:", find_kth_largest(arr, k))


