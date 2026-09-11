s = str(input())
mirror = {'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O',
    'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
    'Y': 'Y', '1': '1', '8': '8',
    'E': '3', '3': 'E',
    'J': 'L', 'L': 'J',
    'S': '2', '2': 'S',
    'Z': '5', '5': 'Z'
}
m = 1
for i in range(len(s)):
    if mirror[s[i]] != s[len(s) - 1 - i]:
        m = 0
p = 0
if s==s[::-1]:
    p = 1
if m == 1 and p == 1:
    print(s + 'is a mirrored palindrome.')
if m == 1 and p == 0:
    print(s + 'is a mirrored string.')
if m == 0 and p == 1:
    print(s + 'is a regular palindrome.')
if m == 0 and p == 0:
    print(s + 'is not a palindrome.')
