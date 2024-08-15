## while문 : 반복횟수가 정해지지 않은 루프
### 조건문이 True->False가 될 때까지 반복
```python
# 무한반복
while True: 
    print('hi')

x = 1 
while x > 0: 
    print('hi')

# 유한반복
x = 1 #초기식
while x > 0: #조건식
    print('hi')
    x -+ 1 #변화식
```

### 대표 유형 3가지
```python
# 식의 증가or감소
x = 0
while x == 10:
    print('유형1')
    x += 1

# 식의 증가or감소(반복 횟수 설정)
count = int(input('반복할 횟수를 입력하세요: '))
x = 0
while x < count:
    print('반복',x+1)
    x += 1

# random 함수 : 원하는 난수가 나올 때 까지
import random

x = 0
while x != 4:
    x = random.randint(1, 6)
    print(x)
```