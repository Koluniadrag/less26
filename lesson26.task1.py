def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Елемент не знайдено

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  # Знайдено елемент

    if arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)  # Пошук у лівій половині

    return binary_search_recursive(arr, target, mid + 1, high)  # Пошук у правій половині


def fibonacci_search(arr, target):
    n = len(arr)

    fib2 = 0
    fib1 = 1






