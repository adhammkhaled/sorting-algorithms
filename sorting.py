import random
import time
import copy


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]





def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]


def mergeSort(arr):
    _mergeSort(arr,0,len(arr)-1)
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
def heapify(arr,n,i): #max heapify
    l=2*i+1
    r=2*i+2
    max = i
    if(l<n and arr[max]<arr[l]):
        max = l
    if(r < n and arr[max]<arr[r]):
        max = r
    if(max!=i):
        arr[max],arr[i] = arr[i],arr[max]
        heapify(arr,n,max)

def buildHeap(arr):
    for i in range(len(arr)//2,-1,-1):
        heapify(arr,len(arr),i)
def heapSort(arr):
    buildHeap(arr)
    for i in range(len(arr)-1,0,-1):
        arr[0],arr[i]  = arr[i],arr[0]
        heapify(arr,i,0)


def quickSort(arr):
    _quickSort(arr,0,len(arr)-1)
def _quickSort(arr,low,high):
    if(low>=high):
        return
    randIndex = random.randint(low,high)
    pivot = arr[randIndex] # random pivot for better complexity in worst case

    arr[randIndex],arr[high] = arr[high],arr[randIndex]
    leftPointer = partition(arr, high, low, pivot)
    _quickSort(arr,low,leftPointer-1)
    _quickSort(arr, leftPointer+1,high)


def partition(arr, high, low, pivot):
    leftPointer = low
    rightPointer = high-1
    while (leftPointer < rightPointer):
        while (arr[leftPointer] < pivot and leftPointer < rightPointer):
            leftPointer += 1
        while (arr[rightPointer] > pivot and leftPointer < rightPointer):
            rightPointer -= 1
        if(leftPointer<=rightPointer):
            arr[rightPointer], arr[leftPointer] = arr[leftPointer], arr[rightPointer]
            leftPointer += 1
            rightPointer -= 1

    if(arr[leftPointer]>arr[high]):
        arr[leftPointer], arr[high] = arr[high], arr[leftPointer]
    else:
        leftPointer=high
    return leftPointer
def generate_arr(x):
    arr=[]
    for i in range(x):
        arr.append(random.randint(0,x))
    return arr

def test_algorithms (x,nsquared):
    arr1 = generate_arr(x)
    if nsquared is True :
        arr2 = copy.deepcopy(arr1)
    arr3 = copy.deepcopy(arr1)
    arr4 = copy.deepcopy(arr1)
    arr5 = copy.deepcopy(arr1)
    if nsquared is True:
        time_start = time.time()
        insertion_sort(arr1)
        time_end = time.time()
        running_time = (time_end - time_start)*1000
        print(f'Running time for insertion sort for size {x} is {running_time} ms')

        time_start = time.time()
        selection_sort(arr2)
        time_end = time.time()
        running_time = (time_end - time_start) * 1000
        print(f'Running time for selection sort for size {x} is {running_time} ms')

    time_start = time.time()
    mergeSort(arr3)
    time_end = time.time()
    running_time = (time_end - time_start) * 1000
    print(f'Running time for merge sort for size {x} is {running_time} ms')

    time_start = time.time()
    heapSort(arr4)
    time_end = time.time()
    running_time = (time_end - time_start) * 1000
    print(f'Running time for heap sort for size {x} is {running_time} ms')

    time_start = time.time()
    quickSort(arr5)
    time_end = time.time()
    running_time = (time_end - time_start) * 1000
    print(f'Running time for quick sort for size {x} is {running_time} ms')
if __name__ == "__main__":
    test_algorithms(1000,True)
    test_algorithms(25000,True)
    test_algorithms(50000,True)
    test_algorithms(100000,True)
    test_algorithms(1000000,False)




