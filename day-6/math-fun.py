#divmod: 나누기의 몫과 나머지
#abs: 절댓값
#pow: 제곱 ->pow(4,2): 4**2
#max: 최대값
#min: 최소값
#round: 반올림
#floor: 내림
#ceil: 올림
#sqrt: 제곱근
#factorial: 팩토리얼
#pi: 원주율

res=divmod(11,3)
print(res) #3, 2
print(abs(-5)) 
print(pow(4,2))
print(max(10,30,5))
print(min(10,30,5))
print(round(23, 89))

import math 
# -> =math.~ 형식으로 작성
#from math import* #=> 함수
#math 모든 함수를 네임스페이스에 가져옴
print(math.floor(24.9))
print(math.ceil(23.8))
print(math.sqrt(16))
print(math.factorial(5))
print(math.pi)