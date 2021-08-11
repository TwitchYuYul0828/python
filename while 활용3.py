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

#map = 인덱스의 값을 순차적으로 입력하게 해줌


      
