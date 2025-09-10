def last_dot_kept(s):
    w = '.'
    c = s.count(w)
    return s.replace(w, '-dot-', c-1)

print(last_dot_kept('..............'))