## if가 아니면 else
### if코드 조건에 맞지 않는 경우(False) => else코드 실행
```python
x = 1
if x==0:
    print("x는 0")
else:
    print("x는 1")
```

### False: 0, None, ''
```python
# 0이 아닌 숫자, 공백이 아닌 문자
if 0x1F:
    print('참')
else:
    print('거짓')

# 0, None, ''는 모두 False
if not 0:
    print('참')
if not None:
    print('참')
if not '':
    print('참')
```

### 조건부 포현식 : if else로 변수 값을 지정하기
```python
# 정석
x = 1
y = 0
if x==1:
    y = 1
else:
    y = 2

# 고수의 코드 : 람다식
lambda y: 1 if x==1 else 2
```

### 조건식 여러 개 지정하기
```python
# 논리식으로 조건을 여러개 가능
x = 30
if x>0 and x<10:
    print('x는 10보다 작은 자연수')
else:
    print('거짓')

# 논리연산자 없이 부등호만으로도 가능
x = 30
if 0<x<10:
    print('x는 10보다 작은 자연수')
else:
    print('거짓')
```