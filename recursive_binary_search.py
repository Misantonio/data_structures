def binary_search(A, item):
    if len(A) == 0:
        return False
    else:
        middle = len(A) // 2
        if A[middle] == item:
            return True
        if item < A[middle]: #A[:middle] is a copy of the elements of A to the left of middle
            return binary_search(A[:middle], item)
        else: #A[middle+1:] is a copy of the elements of A to the right of middle
            return binary_search(A[middle + 1:], item)

numbers = [1, 2, 3, 5, 8, 22, 34, 42, 87, 103]
print(binary_search(numbers, 2))