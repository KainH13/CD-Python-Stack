arr = [8,6,5,7,1,0,4,2,3]

def insertion_sort(arr):
    # iterate through array
    for i in range(1, len(arr)):
        key = arr[i]
        print(key)

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
        print(arr)

insertion_sort(arr)