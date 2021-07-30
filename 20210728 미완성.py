
print("bmi 계산기입니다.")
weight = int(input("몸무게를 입력해주세요."))
height = int(input("키를 입력해주세요."))
height2 = height / 0.01
bmi = weight / (height2^2)
print("당신의 bmi는 %d입니다." %(bmi))
if bmi <= 18.5:
   print("저체중이시네요.")
elif 18.5 < bmi < 23:
    print("정상 몸무게입니다.")
      
score : int(input("점수를 입력하세요."))
if score >= 90:
       print("수")
elif score >= 80:
    print("우")
elif score >= 70:
    print("미")
elif score >= 60:
    print("양")
else score < 60:
    print("가")






    
