# Implement your function below.
def is_one_away(s1, s2):
    if (abs(len(s1)-len(s2))>1):
        return False;

    elif (len(s1)==len(s2)):
        maxChange=1;
        for index, char in enumerate(s1):
            if char!= s2[index]:
                maxChange-=1;
        if maxChange < 0:
            return False

    else:
        longList=s1;
        shortList=s2;
        if (s1<s2):
            longList=s2;
            shortList=s1;
            maxAway=1;
            index=0;
            while index <len(shortList):
                if shortList[index]!=longList[index]:
                    maxAway-=1;
                    longList.pop(index);
                    index+=1;

                if (maxAway<0):
                    return False;

    return True

# NOTE: The following input values will be used for testing your solution.
print(is_one_away("abcde", "abcd"))  # should return True
print(is_one_away("abde", "abcde"))  # should return True
print(is_one_away("a", "a"))  # should return True
print(is_one_away("abcdef", "abqdef"))  # should return True
print(is_one_away("abcdef", "abccef"))  # should return True
print(is_one_away("abcdef", "abcde"))  # should return True
print(is_one_away("aaa", "abc"))  # should return False
print(is_one_away("abcde", "abc"))  # should return False
print(is_one_away("abc", "abcde"))  # should return False
print(is_one_away("abc", "bcc"))  # should return False
