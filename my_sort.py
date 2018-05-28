'''def my_sort1(integers):
    array = []
    for i in range(len(integers)):
        if i%2 != 0:
            odd = i
            array.append(odd)
        else:
            even = i
            array.append(even)
    return sorted(array)
print(my_sort1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))'''


def my_sort(integers):
  even = [i for i in integers if i%2 == 0]
  odd = [i for i in integers if i%2 != 0]
  return sorted(odd)+sorted(even)
print(my_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
