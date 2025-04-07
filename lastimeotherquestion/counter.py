# Function to Find the first repeated word in a string
from collections import Counter


def firstRepeat(input):
    # first split given string separated by space
    # into words
    words = input.split(' ')

    # now convert list of words into dictionary
    a = Counter(words)
    print(a)

    # traverse list of words and check which first word
    # has frequency > 1
    for key in words:
        if a[key] > 1:
            print (key)
            return


# Driver program
if __name__ == "__main__":
    input = 'Ravi had been saying that he had been there'
    firstRepeat(input)