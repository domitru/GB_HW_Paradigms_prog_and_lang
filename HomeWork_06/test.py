def binary_search_manual_input():
    # Запросите у пользователя ввод массива
    list_str = input("Введите отсортированный массив чисел через пробел: ")
    list_num = [int(x) for x in list_str.split()]

    # Запросите у пользователя ввод индекса, который нужно найти
    to_search = int(input("Введите число, которое нужно найти: "))

    first_index = 0
    size = len(list_num)
    last_index = size - 1
    mid_index = (first_index + last_index) // 2

    is_found = True
    while is_found:
        if first_index == last_index:
            if list_num[mid_index] != to_search:
                is_found = False
                return f"-1"

        elif list_num[mid_index] == to_search:
            return f"{to_search} встречается в позиции {mid_index}"

        elif list_num[mid_index] > to_search:
            last_index = mid_index - 1
            mid_index = (first_index + last_index) // 2

        elif list_num[mid_index] < to_search:
            first_index = mid_index + 1
            mid_index = (first_index + last_index) // 2

    return f"{to_search} не встречается в списке"
# Вызов функции для поиска с вводом от пользователя
result = binary_search_manual_input()
print(result)