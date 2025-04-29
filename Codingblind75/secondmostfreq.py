from collections import Counter

def second_most_frequent_char(s):

	freqs = Counter(s)
    print(fre)
	st = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
	return st[1][0] if len(st) > 1 else None
s="geeksforgeeks"
print(second_most_frequent_char(s))

# Python3 code to demonstrate working of
# Sort a Dictionary
# Sort by Values

# initializing dictionary
test_dict = {"Gfg" : 5, "is" : 7, "Best" : 2, "for" : 9, "geeks" : 8}

for key,value in sorted(test_dict.items()):
    print(key,value)

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using items() to get all items
# lambda function is passed in key to perform sort by key
# passing 2nd element of items()
res = {key: val for key, val in sorted(test_dict.items(), key = lambda ele: ele[1])}

# printing result
print("Result dictionary sorted by values : " + str(res))

# using items() to get all items
# lambda function is passed in key to perform sort by key
# passing 2nd element of items()
# adding "reversed = True" for reversed order
res = {key: val for key, val in sorted(test_dict.items(), key = lambda ele: ele[1], reverse = True)}

# printing result
print("Result dictionary sorted by values ( in reversed order ) : " + str(res))




# Original dictionary
my_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# Sorted dictionary by keys
sorted_dict_by_keys = {k: my_dict[k] for k in sorted(my_dict)}

print(sorted_dict_by_keys)

my_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# Sorted dictionary by values in descending order
sorted_dict_by_values_desc = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}
sorted_dict_by_keys_desc = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[0], reverse=True)}

print(sorted_dict_by_values_desc)
print(sorted_dict_by_keys_desc)



