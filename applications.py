import sorting


def hybrid_sort(arr , threshold):
    _hybrid_sort(arr,0,len(arr)-1 ,threshold)
    return arr
def _hybrid_sort(arr, l , h , threshold):
    if h-l <= threshold :
        newArray = arr[l:h+1]
        sorting.insertion_sort(newArray)
        arr[l:h+1] = newArray

    else:
           if (l < h):
                m = (l + h) // 2
                _hybrid_sort(arr, l, m,threshold)
                _hybrid_sort(arr, m + 1, h,threshold)

                sorting.merge(arr,l,h)


arr = sorting.generate_arr(1000)
threshold = 5
print(arr)
sorted_arr = hybrid_sort(arr, threshold)
print("Sorted array:", sorted_arr)
def find_kth_largest(arr, k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        pivot_index = sorting.partition(arr, low, high,arr[high])
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


