test_str = "GeeksforGeeks"

# using naive method to get count  
# of each element in string  
all_freq = {}



for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

for key, value in all_freq.items():
    if value>1:
        print(key,value)

# printing result  
print("Count of all characters in GeeksforGeeks is :\n "
      + str(all_freq))