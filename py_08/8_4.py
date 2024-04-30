# foods = {   "떡볶이" : "오뎅",
#             "짜장면" : "단무지",
#             "라면" : "김치",
#             "피자" : "피클",
#             "맥주" : "치킨"}

# while(True) :
#     print("좋아하는 음식은 ?", end="")
#     myfood = input(str(list(foods.keys()))+ " 중 좋아하는 것은? ")
#     if myfood in foods :
#         print("궁합음식은 : %s" %(foods.get(myfood)))
#     elif myfood == "끝":
#         break
#     else :
#         print("항목에 없습니다")
    
foods = {   "떡볶이" : "오뎅",
            "짜장면" : "단무지",
            "라면" : "김치",
            "피자" : "피클",
            "맥주" : "치킨"}

use={"a":"apple","r":"red"}
foods.update(use) #합병
print(foods)

while(True) :
    print("좋아하는 음식은 ?", end="")
    myfood = input(str(list(foods.keys()))+ " 중 좋아하는 것은? ")
    if myfood in foods :
        print("궁합음식은 : %s" %(foods.get(myfood)))
    elif myfood == "끝":
        break
    else :
        print("항목에 없습니다")