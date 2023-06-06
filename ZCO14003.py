# cook your dish here
l=[]
for n in range(int(input())):
    l.append(int(input()))
    
l.sort()
#print(l)
maxi=[]
for i in range(len(l),0,-1):
    maxi.append(l[len(l)-i ]*i )
    
print(max(maxi))
    
    
