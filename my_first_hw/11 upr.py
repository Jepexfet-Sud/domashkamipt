s=str(input())
p=0
m=0
a=len(s)
c=s[::-1][:(a//2)+a%2]
mr=s
mr=mr.replace('2','S')
mr=mr.replace('J','L')
mr=mr.replace('3','E')
mr=mr.replace('5','Z')
if mr==mr[::-1] and any(x for x in 'BCDFGKNPQR4679') not in s:
    m=1
    print(m)
if s==s[::-1]:
    p=1
    print(p)

