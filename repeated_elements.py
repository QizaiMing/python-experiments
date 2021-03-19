import collections

array_input = [4, 3, 2, 7, 8, 2, 3, 1]
print([item for item, count in collections.Counter(array_input).items() if count > 1])
