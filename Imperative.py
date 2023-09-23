# Задача: дан список целых чисел numbers,
# необходимо написать в императивном стиле
# процедуру для сортировки числа в списке в порядке убывания


# Я решил разобрать встроенный метод sorted() из python на императивный лад
# он реализует гибридный алгоритм Timsrot Тима Петерсона
# 1. разбиваем коллекцию на подколлекцию
# 2. каждая подколлекция сотрируется алгоритмом сортировки вставками
# 3. При помощи сортировки слиянием, подколлекции сливаются в единую коллекцию
# 4. добавил метод reverse_list, потому что такой сортировкой
# предусмотрено расположение по возрастанию
numbers = [4, 2, 7, 1, 9, 5]


# merge: слияние подсписков в единый отсортированный список. Сортировка слиянием
def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] >= right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])


# timsort_helper: сортируем список используя алгоритм сортировки вставками,
# разбиваем список на подсписки(threshold)
def timsort_helper(nums, threshold):
    n = len(nums)
    for i in range(0, n, threshold):
        end = min(i + threshold - 1, n - 1)
        for j in range(i + 1, end + 1):
            key = nums[j]
            k = j - 1
            while k >= i and nums[k] > key:
                nums[k + 1] = nums[k]
                k -= 1
            nums[k + 1] = key


# императивный разворот списка, хотя можно использовать reverse()
def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1


# наша сортровка по убыванию, вызываем times_helper для сортировки вставками
# при каждой итерации while удваиваем размер подсписков(threshold) используя merge(),
# чтобы их объединить, в конце вызываем reverse_list, для того, тобы список был по убыванию
def timsort_descending(nums):
    min_run = 32
    n = len(nums)

    timsort_helper(nums, min_run)

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merged_array = merge(nums[start:mid + 1], nums[mid + 1:end + 1])
            nums[start:start + len(merged_array)] = merged_array

        size *= 2
    reverse_list(nums)
    return nums


sorted_numbers = timsort_descending(numbers)
print("Imperative Timsort sorting:")
print(sorted_numbers)
