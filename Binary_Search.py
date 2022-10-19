
## Welcome to my binary search algorithm using my favorite programming language.

list_of_numbers = [i**2 for i in range(10)]

# The list must be sorted to use binary search
print(list_of_numbers)

def binary_search(value, begin, end, list_of_values):
    middle = begin + (end - begin)//2
    if (end >= begin):
        if list_of_numbers[middle] == value:
            return middle
        if list_of_numbers[middle] > value:
            return binary_search(value,0, middle-1, list_of_values)
        if list_of_numbers[middle] < value:
            return binary_search(value,middle + 1, end, list_of_values)
    return -1

result = binary_search( 49, 0, len(list_of_numbers), list_of_numbers)
print(result)


