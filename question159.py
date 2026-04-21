s="abbaacdc"
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
    while len(dc)>2: #this is to check for distinct characters
        toremove=s[left]  
        if dc[toremove]>1:
            dc[toremove]-=1
            left+=1
        else:
            dc.pop(toremove)
            left+=1
    maxlen=max(maxlen,right-left+1)
print(maxlen)
