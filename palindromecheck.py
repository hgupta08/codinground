def ispalindrome(s):

    l=0
    r=len(s)-1

    while l<r:
        while l<r and not isalphanum(s[l]):
            l=l+1
            print("loopingx")

        while r>l and not isalphanum(s[r]):
            r = r - 1
        print(l,r)
        print(s[l])
        print(s[r])
        if s[l].lower()!=s[r].lower():
            return False
        l=l+1
        r=r-1
    return True



def isalphanum(s):
    return (ord('A')<=ord(s)<=ord('Z') or
            ord('a')<=ord(s)<=ord('z') or
            ord('0')<=ord(s)<=ord('9'))

print(ispalindrome("Was it a car or a cat I saw?"))

