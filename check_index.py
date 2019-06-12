def binary_search(array, elem):
    low = 0
    high = len(array)-1

    while low <= high:
        mid = (low+high) // 2
        if elem == array[mid]:
            print("Element found at index {}".format(mid))
            return mid
        elif elem < array[mid]:
            high = mid - 1
            x = 0
        else:
            low = mid + 1
            x = 1
    print("Element not found. Its index should be {}".format(mid+x))    
    return mid + x
            
   
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 8, 10, 33, 56, 57, 60, 140, 203]
    el = 240
    # binary_search(arr, el)
    print(binary_search(arr, el))