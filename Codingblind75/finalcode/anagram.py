s1 = "cat"
s2 = "tacss"

def validanagram(s1,s2):

    s1=s1.replace(" ","").lower()

    s2=s2.replace(" ","").lower()

    if len(s1)!=len(s2):
        return False

    ht={}

    for i in s1:
        if i in ht:
            ht[i]+=1
        else:
            ht[i]=1

    for j in s2:
        if j in ht:
            ht[j]-=1
        else:
            ht[j]=1
    print(ht)

    for i in ht:
        if ht[i] != 0:
            return False
    return True

print(validanagram(s1,s2))