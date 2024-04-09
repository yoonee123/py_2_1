# sports = ['축구', '야구', '농구', '배구']
# num = [11, 9, 5, 6]
# print(sports)
# print(num)
# #위 두 리스트로 출력
# for i in range(len(sports)):
#     print('%s : %d명' % (sports[i], num[i]), end = ' ') # end구문은 줄바꿈을 원하지 않을 때

# sports = ['축구', '야구', '농구', '배구']
# num = [11, 9, 5, 6]
# sponum = [sports, num]
# print(sponum)
# # 2차원 리스트에서 출력
# for i in range(len(sponum[0])):
#     print('%s : %d명' %(sponum[0][i], sponum[1][i]), end = ' ')

sports = ['축구', '야구', '농구', '배구']
num = [11, 9, 5, 6]
# 다른 구조의 2차원 리스트 생성을 컴프리헨션으로 처리
psponum = [[sports[i], num[i]] for i in range(len(sports))]
print(psponum)
# 위 리스트에서 출력
for one in psponum:
    print('%s : %d명' % (one[0], one[1]), end = ' ')