arr = [8,6,5,7,1,0,4,2,3]

def selection_sort(arr):
    starter = 0
    while (starter < len(arr)):
        print("-"*40)
        min = arr[starter]
        new_min_found = False
        for i in range(starter + 1, len(arr)):
            if arr[i] < min:
                min = arr[i]
                min_index = i
                new_min_found = True
        print(f"First Value: {arr[starter]} Min Value: {min}")
        if new_min_found == True:
            swap_value = arr[starter]
            arr[min_index] = swap_value
            arr[starter] = min
        print(arr)
        starter += 1


selection_sort(arr)