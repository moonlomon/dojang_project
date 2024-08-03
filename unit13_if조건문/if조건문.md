## if문
### 특정 조건에 실행하는 코드는 if문을 중간에 넣어주면 된다
```python
x = int(input('나이를 입력해주세요: '))

# if문
if x>=20: 
    print('당신은 성인입니다')
    if x>=65:
        print('당신은 성인이며 노년기에 해당됩니다.')

print('당신의 나이는: '+str(x)+'세')
```
### if문(조건문)이 참이면 출력 거짓이면 출력이 안된다.
```python
if True:
    print('1번 조건문 출력')
if False:
    print('2번 조건문 출력') #출력: 1번 조건문 출력
```
### 조건문 코드실행이 불필요할 때 pass를 써준다
```python
if x=10:
    pass # TODO: x가 10일 때 처리를 작성해야됨
```

## if문 용어
```python
if True: #조건식
    pass #if body(if 본문) => 4칸 띄어쓰기(탭 1번)
```