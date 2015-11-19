s = 'This dinner is not that bad!'
nt = s.find('not')
bd = s.find('bad')
if nt < bd:
    s = s.replace(s[nt:bd+3],'good')


print(s)