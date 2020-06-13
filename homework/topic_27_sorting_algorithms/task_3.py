"""
One way to improve the quicksort is to use an insertion sort on lists that are small in length
(call it the “partition limit”). Why does this make sense?
Re-implement the quicksort and use it to sort a random list of integers.
Perform analysis using different list sizes for the partition limit.
"""


def partition(nums, low, high):
    # Мы выбираем средний элемент, в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент в i (слева от оси) больше, чем элемент в j (справа от оси), то поменять их местами
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Создаем вспомогательную рекурсивную функцию
    def _quick_sort(items, low, high):
        if low < high:
            # Это индекс после опорного элемента, по которому наши списки разделены
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


# Проверка, что всё работает
random_list_of_nums = [50, 12, 23, 5, 40, 33, 18, 1, 2, 98]
quick_sort(random_list_of_nums)
print(random_list_of_nums)
