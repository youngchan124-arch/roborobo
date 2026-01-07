'''
print(abs(-5)) #절댓값
print(pow(4,2)) #거듭제곱
print(max(5,12)) #가장 큰 값
print(min(5,12)) #가장 작은 값
print(round(3.14)) # 반올림
print(round(4.678,2)) # 소수점 2번쨰 자리 반올림 

from math import * #math 모듈 모든 기능 가져가 쓰겠다 ('import math'로도 사용 가능 -> 하지만 이때는 함수들 앞에 math. 함꼐 작성)

result = floor(4.99)
print(result)
result = ceil(3.14)
print(result)
result = sqrt(16)
print(result)
'''
from random import * #random은 0이상 1미만 난수 뽑는 기능

print(random()* 10)
print(int(random()* 10))
print(int(random()* 10)+ 1)

print(int(random() *45)+ 1)
# randgrange(시작 숫자, 끝 숫자)- 끝 숫자 포함// randint(시작 숫자, 끝 숫자)- 끝 숫자 미포함

print(randrange(1,46))
print(randint(1,45))