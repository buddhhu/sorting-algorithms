def quick_sort(data: list) -> list:
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        less = [x for x in data[1:] if x <= pivot]
        great = [x for x in data[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(great)

# Example usage:
my_list = [12, 4, 5, 6, 7, 3, 1, 15]
sorted_list = quick_sort(my_list)
print(sorted_list)
