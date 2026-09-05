#exercise number 4
f=open('input.txt')
num=''
for line in f:
    num=line
    break
s=open('input.txt').read()
num=num.replace(' ',s[-1:])
ans=str(eval(num))
print(num)
f=open('input.txt', 'w')
f.write(ans)
f.close()

