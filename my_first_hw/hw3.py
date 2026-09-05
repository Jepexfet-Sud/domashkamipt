#exercise number 6
def prvd(x,c):
    s=''
    while x>0:
        s=str(x%c)+s
        x=x//c
    return s
f=open('input2.txt').read()
ch=int(f[-1])
zn=f[-3]
f=open('input2.txt')
for line in f:
    nums=line
    break
nums=nums.split(' ')
a=''
for i in nums:
    a+=str(int(i,ch))+zn
a=a[:-1]
ans=eval(a)
ans=prvd(ans,ch)
f=open('input2.txt','w')
f.write(ans)
f.close()
