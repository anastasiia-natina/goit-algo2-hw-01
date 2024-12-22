def find_min_max(arr): 

    if len(arr) == 1:
        return arr[0], arr[0]

    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    return min(left_min, right_min), max(left_max, right_max)


numbers = [3, 7, 2, 9, 5, 1, 4, 6]


min_value, max_value = find_min_max(numbers)

print("Мінімальне значення:", min_value)
print("Максимальне значення:", max_value)
