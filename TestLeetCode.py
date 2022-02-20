s = "cbbd"
finStr = ''
oldfinStr = ''
i =0

while i < len(s):
    if len(oldfinStr) < 1:
        finStr += s[i]
        oldfinStr = finStr
        i += 1
    elif len(oldfinStr) < len(s):
        finStr += s[i]
        if oldfinStr < finStr:
            if finStr[::-1] == finStr:
                oldfinStr = finStr
            i += 1
    if oldfinStr == '':
        i = 0

print(oldfinStr, finStr)