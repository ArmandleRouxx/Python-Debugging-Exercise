def quick_sort(numbers):
    quick_sort_helper(numbers, 0, len(numbers)-1)


def quick_sort_helper(numbers, first, last):
    if first < last:

        split_point = partition(numbers, first, last)

        quick_sort_helper(numbers, first, split_point-1)
        quick_sort_helper(numbers, split_point+1, last)


def partition(numbers, first, last):
    pivot_value = numbers[first]

    # Error: left_mark was set equal to first-1
    left_mark = first
    right_mark = last

    done = False
    while not done:

        # Error: While condition checked left_mark <= right_mark
        while left_mark < right_mark-1 and numbers[left_mark] <= pivot_value:
            # Error: was set equal right_mark + 1
            left_mark += 1

        # Error: While condition checked right_mark >= left_mark
        while numbers[right_mark] >= pivot_value and right_mark > 0:
            # Error: was set equal left_mark - 1
            right_mark -= 1

        # Error: if-condition checked right_mark < left_mark -1
        if right_mark <= left_mark:
            done = True
        else:
            temp = numbers[left_mark]
            numbers[left_mark] = numbers[right_mark]
            numbers[right_mark] = temp
    temp = numbers[first]
    numbers[first] = numbers[right_mark]
    numbers[right_mark] = temp

    return right_mark


numbers_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Before Sort: {}".format(numbers_list))
quick_sort(numbers_list)
print("After Sort: {}".format(numbers_list))
