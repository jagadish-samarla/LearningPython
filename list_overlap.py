a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 89, 13]
b = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 34]
overlap_list = [i for i in a for j in b if i == j]
duplicates_removed_list = []
#for i in a:
 #   for j in b:
  #      if i == j:
   #         overlap_list.append(i)

for i in overlap_list:
    if i not in duplicates_removed_list:
        duplicates_removed_list.append(i)


print(duplicates_removed_list)