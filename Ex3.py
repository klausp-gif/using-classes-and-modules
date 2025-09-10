def find_all(s, sub):
    lst = []
    start = 0 #starting index of next find
    while start < len(s) and (i := s.find(sub, start)) >= 0:
        lst.append(i)
        start = i + 1
    return lst

s = 'ababab'
sub = 'b'

print(find_all(s, sub))
