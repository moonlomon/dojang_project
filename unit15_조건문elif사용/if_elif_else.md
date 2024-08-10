## elif : else if
### 3지 선다 이상의 코드를 작성할 때 elif를 사용해주면 된다
```python
x = 1
if x == 0:
    print('x는 0')
elif x == 1:
    print('x는 1')
else:
    print('x는 2 이상')
```

### if만 쓰지 않고 굳이 elif를 쓰는 이유
```python
# if를 쓰면 매 조건 조건식을 다 검사하고 실행한다
a,b,c = 1,2,3
if a == 1:
    print(a)
if b == 2:
    print(b)
if c == 3:
    print(c) #a,b,c 다 출력됨

if a == 1:
    print(a)
elif b == 2:
    print(b)
elif c == 3:
    print(c) #a만 출력됨
```