sequence = input("Введите последовательность чисел через пробел: ")
number = int(input("Введите любое число: "))

sequence_list = sequence.split()
sequence_list = [int(i) for i in sequence_list]

def sort_list(list_to_sort):
    for i in range(len(list_to_sort)):
        for j in range(len(list_to_sort)-1):
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
    return list_to_sort
print(sequence_list)
sorted_list = sort_list(sequence_list)
print(sorted_list)

def binary_search(list_to_search, number, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if list_to_search[middle] == number:
        return middle
    elif number < list_to_search[middle]:
        return binary_search(list_to_search, number, left, middle - 1)
    else:
        return binary_search(list_to_search, number, middle + 1, right)

place=binary_search(sorted_list,number, 0, len(sorted_list))
print("Позиция искомого элемента в списке:", place+1)