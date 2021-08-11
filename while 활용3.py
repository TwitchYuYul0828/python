'''
점수를 계속 입력을 받다가 0이 입력되면 0을 제외하고
이전에 입력된 자료의 수와 합계, 평균을 출력하는 프로그램
(평균은 반올림하여 소수 둘째자리)
ex) 15 88 97 0
입력된 자료의 개수 = 3
입력된 자료의 합계 = 200
입력된 자료의 평균 = 66.67
'''
cnt = 0
sum_ = 0
num = input("점수를 입력하세요.").split()
num = list(map(int, num))

while num[cnt]  != 0:
    sum_ = sum_ + num[cnt]
    cnt = cnt + 1

avg= sum_ /cnt

print("입력한 자료의 개수 : %d" %cnt)
print("입력한 자료의 값 : %d" %sum_)
print("입력한 자료의 평균 : %.2f" %avg)

#map = list에 인덱스값을 순차적으로 들어갈수있게해줌.

cnt = 0
sum_ = 0
num = input("점수를 입력해주세요.").split()
num = list(map(int, num))

while True:
    sum_ = sum_ + num[cnt]
    if (num[cnt] >= 100) :
         break
    cnt = cnt + 1
avg = sum_ / cnt
print("입력한 자료의 합은 %d입니다." %sum_)
print("입력한 자료의 합은 %.1f입니다." %avg)


cnt = 0
sum_ = 0
odd_cnt = 0
num = list(map(int, input("정수를 입력해주세요.").split()))

while True:
  if num[cnt] == 0:
      break
  if (num[cnt] % 2 == 1):
     sum_ = sum_ + num[cnt]
     odd_cnt = odd_cnt + 1
  cnt = cnt + 1

avg = sum_ / cnt
print("입력한 자료의 합 : %d" %sum_)
print("입력한 자료의 평균 : %d" %avg)

      
