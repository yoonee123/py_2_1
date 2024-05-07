sports = ['축구','야구','농구','배구']
num = [11, 9, 5, 6]
print(sports)
print(num)
print('---')
for s, i in zip(sports, num):
    print('%s: %d명' %(s, i), end=' ')
print()
for tp in zip(sports, num):
    print('{} : {}명'.format(*tp), end=' ')
print()
s = dict(zip(sports,num))
print(s)
for key in s.keys():
    print('%s : %s명' %(key,s[key]), end=' ')
print()
for item in s.items():
    print('{} : {}명'.format(item[0], item[1]), end=' ')
print()
for item in s.items():
    print('{} : {}명'.format(*item), end=' ')