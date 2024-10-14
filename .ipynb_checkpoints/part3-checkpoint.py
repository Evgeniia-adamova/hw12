def sorting(numbers):
    x = len(numbers)
    for i in range(x):
        for y in range(x - 1):
            if numbers[y] > numbers[y + 1]:
                z = numbers[y]
                numbers[y] = numbers[y + 1]
                numbers[y + 1] = z

    return numbers

list1 = [44, 82, 1, 2, 0]
list2= [11, 555, 777, 33, 333, 58267823, 9128378, 636363]
print("Sorted list1", sorting(list1.copy()))
print("Sorted list2", sorting(list2.copy()))