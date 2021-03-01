path_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temp_list = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

result = [x for x in path_list + temp_list if x not in path_list or x not in temp_list]
print(result)