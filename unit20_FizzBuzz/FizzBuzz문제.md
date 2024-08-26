## FizzBuzz출력문제 
#### 규칙 : 3의 배수 = Fizz, 5의 배수 = Buzz, 3과 5의 공배수 = FizzBuzz가 출력되게 하라.
### 방법 1 : 논리연산자 사용하기
```python
for i in range(1, 100):
    if i%3==0 and i%5==0: # 공배수를 먼저 가장 먼저 하기
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)
```

### 방법 2 : 최소공배수 사용하기 => 가독성을 위해 비추
```python
for i in range(1, 100):
    if i%15==0: # 3과 5의 최소공배수 15사용. 주석이 없으면 같은 실무자가 의도를 모를 수도 있음
        print('FizzBuzz')
    elif i%3=0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)
```

### 방법 3 : 코드 단축(코드 골프) - True, False 응용하기 => 제일 비추
```python
for i in range(1, 100):
    print('Fizz'*(i%3==0)+'Buzz'*(i*5==0) or i)
```