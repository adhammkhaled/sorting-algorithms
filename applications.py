import sorting
def hybrid_sort(arr,threshold):

    if len(arr) <= threshold :
        sorting.insertion_sort(arr)
    else :
        sorting.mergeSort(arr)
    return arr

arr = sorting.generate_arr(1000)
threshold = 5
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
