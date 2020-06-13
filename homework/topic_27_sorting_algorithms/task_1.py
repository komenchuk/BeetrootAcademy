"""
A bubble sort can be modified to “bubble” in both directions.
The first pass moves “up” the list and the second pass moves “down.”
This alternating pattern continues until no more passes are necessary.
Implement this variation and describe under what circumstances it might be appropriate.
"""


def bubble_sort(nums):
    # Мы устанавлиаем swapped в True, чтобы цикл проходился как минимум один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем местами элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавлваем флаг в True, чтобы снова зациклиться
                swapped = True


# Убедимся, что это работает
random_list_of_nums = [5, 12, 6, 8, 15, 1, 9, 2, 3]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)
