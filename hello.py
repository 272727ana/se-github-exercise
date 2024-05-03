def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

lst = [13, 6, 5, 5, 10]
result = sum_list(lst)
print(result)