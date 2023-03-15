prefix = ""
strs = ["flower","flow","flight"]
first = strs[0]

for i in range(len(first)+1):
    c = 0
    for word in strs:
        if first[:i] in word[:i]:
            c += 1
    if c == len(strs):
        if len(first[:i])>len(prefix):
            prefix = first[:i]

print(prefix)