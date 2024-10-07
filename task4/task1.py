array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

all_elems = array_1 + array_2 + array_3
new_elems_1 = []

for elem in all_elems:
    if elem not in new_elems_1 and all(elem in array for array in [array_1, array_2, array_3]):
        new_elems_1.append(elem)
print("Решение без множеств:", new_elems_1)

new_elems_1_set = set(array_1) & set(array_2) & set(array_3)
print("Решение с множествами:", new_elems_1_set)