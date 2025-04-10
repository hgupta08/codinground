# Python program to check
# if a string is palindrome
# or not

#
# w = ""
# for i in x:
#     w = i + w
#     print(w)
#
#
# if (x == w):
#     print("Yes")
# else:
#     print("No")
#
def isPalindromenospace(s):
    l, r = 0, len(s) - 1


    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True


def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


def isPalindrome(s):

    newStr = ''
    for c in s:
        if c.isalnum():
            newStr = c.lower() +newStr
    return newStr == newStr[::-1]



x = "cac"
print(x[::-1])
print(isPalindromenospace(x))
 
 
