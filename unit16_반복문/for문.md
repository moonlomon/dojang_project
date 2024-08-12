## for문으로 순환하는 코드(루프)만들기
### range()의 인덱스를 꺼낼 때 마다 코드를 실행한다.
```python
# for문을 통해 레인지의 인덱스를 꺼낼 때 마다 코드를 실행한다.
for i in range(3):
    print('하이') #'하이' 3번 줄바꿔서 출력

for i in range(0,5):
    print(i) #인덱스 01234 줄바꿔서 출력

for i in range(5,0,-1):
    print(i) #d인덱스 54321 줄바꿔서 출력
```

#### * 참고 : 파이썬 2.7에서 range는 용량큼(list를 생성) => xrange()를 사용

### range 외 시퀀스도 for문 가능
```python
# 리스트
for fruits in ['사과', '바나나', '배']:
    print(fruits, end=' ') #출력: 사과 바나나 배 

# 튜플
for i in 0,1,2:
    print(i, end=' ') #출력: 0 1 2 

# 문자열 + reversed()적용
for letter in reversed('python'):
    print(letter, end='') #출력: nohtyp
```