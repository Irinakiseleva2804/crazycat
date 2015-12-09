s=input()
for i in range(0, len(s)):
    if s[i]=="T":
        t=t+1
    s=s.replace('T','U')
print (s)
