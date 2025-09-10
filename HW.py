import math

for k in range(11):
    a = k * math.pi / 5
    print(a, math.sin(a), math.cos(a))

print(' ')

def date_of_birth(ssn):
   c = (ssn[6])
   y = int(ssn[4:6])
   m = int(ssn[2:4])
   d = int(ssn[0:2])
   

   if c =='-':
       x = 1900
   elif c == 'A':
       x = 2000
   else:
       x = 1800
    
   x += y
   
   return print(x, m, d)

date_of_birth('140598-abcd')

print(' ')

def dashify_substring(s, sub):
    return print(s.replace(sub, f'-{sub}-', 1))

dashify_substring('foo', 'o')

print(' ')

def file_type(s):
    x = '.'
    y = s.rfind(x) + 1
    return(s[y:])

print(file_type('six.seven'))

while (i := input('my-calc: ')) != '':
    [astr, op, bstr] = i.split()

    x = int(astr)
    y = int(bstr)

    if op == '+':
        res = x + y
    elif op == '-':
        res = x - y
    elif op == '*':
        res = x * y
    else:
        res = 'error'

    print(res)

    print(' ')

    def max_char_rep(s):
        cur_len = 0
        max_len = 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur_len += 1
                max_len = max(cur_len, max_len)
            else:
                cur_len = 1
        return max_len
    print(max_char_rep('jfjre hfiuhrierhiruhiug        grnieuhgirehgiurh.................'))
