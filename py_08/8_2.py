phone_book = {"홍길동" : "010-1234-5678",
              "강감찬" : "010-1234-5679",
              "이순신" : "010-1234-5680"}
print(phone_book)

season = {'봄' : 'spring',
          '여름' : 'summer',
          '가을' : 'autumn',
          '겨울' : 'winter'}

print(season.keys())
print(season.items())
print(season.values())
 
# 메소드 keys()로 항목 순회
for key in season.keys():
    print('%s %s' %(key, season[key]))
    
for item in season.items():
    print('{} {} '.format(item[0], item[1]), end='')
    
print()
for item in season.items():
    print('{} {} '.format(*item), end='')