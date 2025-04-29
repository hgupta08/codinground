from collections import defaultdict


def groupAnagrams(strs):

    # When the list class is passed as the default_factory argument,
    # then a defaultdict is created with the values that are list.
    #Note here list is passed
    #dic is like key:[value in list]

    res = defaultdict(list)
    for s in strs:
        print(s)
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
            print(count)

        print(type(res))
        res[tuple(count)].append(s)
        print(res)
    return list(res.values())

print(groupAnagrams(["act","cat"]))

