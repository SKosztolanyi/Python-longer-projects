fh=open(r'D:\romeo.txt')
lst=list()
for i in fh:
    line = i.rstrip()
    words = line.split()
    if (words[:] in lst) == False:
        lst.append(words)
    lol= sum(lst, [])
    bol= list(set(lol))
print sorted(bol)
