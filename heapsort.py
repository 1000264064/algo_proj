def max_heapify(arr, i, heap_size): 
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size)

def build_max_heap(arr):
    heap_size = len(arr)
    for i in range(len(arr) // 2 - 1, -1, -1):
        max_heapify(arr, i, heap_size)

def heap_sort(arr):
    build_max_heap(arr)
    heap_size = len(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        max_heapify(arr, 0, heap_size)


print ("what is the numbers you need to sort : ")
n=int (input())
arr=[]
for i in range(n):
     print (f"enter numbers [{i}]: ") 
     arr.append(int (input()))
   

heap_sort(arr)
print("Sorted array:",arr )

