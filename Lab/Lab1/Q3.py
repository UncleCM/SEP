def binary_search(target, arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return False

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(target, arr, mid + 1, right)
    else:
        return binary_search(target, arr, left, mid - 1)

print(binary_search(7, [2, 3, 4, 7, 8]))