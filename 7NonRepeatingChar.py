# Implement your function below.
def non_repeating(given_string):
    d={};
    for eachChar in given_string:
        if (eachChar not in d):
            d[eachChar]=1
        else:
            d[eachChar]+=1;

    for eachChar in given_string:
        if d[eachChar]==1:
            return eachChar
    return None

# NOTE: The following input values will be used for testing your solution.
print(non_repeating("abcab")) # should return 'c'
print(non_repeating("abab")) # should return None
print(non_repeating("aabbbc")) # should return 'c'
print(non_repeating("aabbdbc")) # should return 'd'
