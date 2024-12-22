def quick_select(arr, k):
    
    def partition(arr, low, high):
        pivot = arr[high] 
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def select(arr, low, high, k):
        if low == high:
            return arr[low]

        pi = partition(arr, low, high)

        if pi - low == k - 1:
            return arr[pi]
        elif pi - low > k - 1:
            return select(arr, low, pi - 1, k)
        else:
            return select(arr, pi + 1, high, k - pi + low - 1)

    return select(arr, 0, len(arr) - 1, k)


number_list = [3, 7, 2, 9, 5, 1, 4, 6]


k = 4
k_smallest = quick_select(number_list, k)
print(f"{k}-й найменший елемент: {k_smallest}")