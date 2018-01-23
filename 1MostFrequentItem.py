array = [1,3,4,2,6,4,3,6,2,1,3,3,2,1,5,3,2,1,5,6];

def mostFreq(arr):
    d={};
    for x, index in range(0, len(arr)):
        if (arr[x] not in d):
            d[arr[x]]=1
        else:
            d[arr[x]]+=1

    maxItem = ""
    maxFreq = 0
    for key, value in d.items():
        print("Key is {}, Value is {}".format(key, value))
        if (maxFreq<value):
            maxFreq=value
            maxItem=key

    return maxItem;

print(mostFreq(array));
