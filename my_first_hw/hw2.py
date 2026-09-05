#exercise number 4
f=open('input1.txt')
num=''
for line in f:
    num=line
    break
s=open('input1.txt').read()
num=num.replace(' ',s[-1])
ans=str(eval(num))
print(num)
f=open('input1.txt', 'w')
f.write(ans)
f.close()

