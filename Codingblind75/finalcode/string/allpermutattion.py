# Python program to print all permutations with
# duplicates allowed

def toString(List):
    return ''.join(List)


def permute(a, l, r):

    if l == r:

        print(toString(a))
    else:
        for i in range(l, r + 1):

            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack

# Driver program to test the above function
string = "123"
n = len(string)
a = list(string)
permute(a, 0, n - 1)








