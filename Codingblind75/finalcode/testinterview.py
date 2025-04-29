def isanagram(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    print(s1,s2)
    ht={}
    for i in s1:
        if i in ht:
             ht[i]+=1
        else:
            ht[i]=1
            c-0
            a-0
            t-0
            s-1
            tacss

    for j in s2:
        if j in ht:
            ht[j]-=1
        else:
            ht[j]=1
    print(ht)
    count=0

    for i in ht:
        print(ht[i])
        if ht[i]!=0:
            return False
    return True







#s="listen,silent"
s1="listen"
s2="silent"
s="listen,silent"
s=s.split(',')
print(s)
t1=[]
t1.append(s[0])
print(t1)
# for i in range(len(s)):
#     isanagram(s[i],s[i+1])
isanagram("silent,cat",s2)

#outpyt-
#listen,silent
#google,gooegl