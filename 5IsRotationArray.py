def is_rotation(list1, list2):
    index_1=list1.index(list2[0]);
    if len(list1)!=len(list2):
        return False;
    if index_1 <0:
        return False;
        
    index_2=0;

    while index_2<len(list2):
        if (index_1==len(list1)):
            index_1=0;
        if (list1[index_1]!=list2[index_2]):
            return False;
        index_1+=1;
        index_2+=1;
    return True



# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.

print(is_rotation(list1, list2a))
print(is_rotation(list1, list2b))
print(is_rotation(list1, list2c))
print(is_rotation(list1, list2d))
print(is_rotation(list1, list2e))
print(is_rotation(list1, list2f))
