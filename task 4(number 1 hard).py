def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

numbers = input("Введите числа через пробел: ").split()
arr = [int(x) for x in numbers]
    
print(f"Исходный список: {arr}")
sorted_arr = bubble_sort(arr.copy())
print(f"Отсортированный список: {sorted_arr}")
