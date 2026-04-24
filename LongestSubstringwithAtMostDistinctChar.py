k=int(input()) #if input is not given in the question
dc={}
left=0
right=-1
maxlen=0
for x in s:
    if x not in dc:
        dc[x]=1
        right+=1
    else:
        dc[x]+=1
        right+=1
    while len(dc)>k:
        toremove=s[left]
        if dc[toremove]>1:
            dc[toremove]-=1
            left+=1
        else:
            dc.pop(toremove)
            left+=1
    maxlen=max(maxlen,right-left+1)
print(maxlen)  
