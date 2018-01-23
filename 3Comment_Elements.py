def common_elements(list1, list2):
    if len(list1)>=len(list2):
      longList=list1;
      shortList=list2;
    else:
      longList=list2;
      shortList=list1;

    d={};
    result = []
    for item in shortList:
      d[item]=1;
    for item in longList:
      if item in d:
        result.append(item);
    return result

list_a1 = [1, 3, 4, 6, 7, 9]
list_a2 = [1, 2, 4, 5, 9, 10]
print(common_elements(list_a1, list_a2))

list_b1 = [1, 2, 9, 10, 11, 12]
list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
print(common_elements(list_b1, list_b2))

list_c1 = [0, 1, 2, 3, 4, 5]
list_c2 = [6, 7, 8, 9, 10, 11]
print(common_elements(list_c1, list_c2))
