from re import split

import requests
import re

url='https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt'
r=requests.get(url=url)
a=r.text


s1="abc100**[]"
expr=r"\d"+"[*]+"+"[[]+""[]]+"
a=re.sub(pattern=expr,string=a,repl="")
#
# b=re.sub(pattern=expr2,string=a,repl="")
print(a)


# s="""This is the Etext file presented by Project Gutenberg and
# is presented in cooperation with World Library Inc fro their
# Library of the Future and Shakespeare CDROMS"""

ht={}
s=split(pattern=" ",string=a)
for i in s:
    if i in ht:
        ht[i]+=1
    else:
        ht[i]=1

print(ht)
